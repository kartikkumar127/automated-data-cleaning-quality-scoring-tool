import streamlit as st
import pandas as pd
import io

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Data Cleaning Automation Tool",
    layout="wide"
)

st.title("Data Cleaning Automation Tool")
st.write("Clean CSV & Excel files easily with multiple options.")

# KPI FUNCTION
def data_quality_score(df):
    total_cells = df.shape[0] * df.shape[1]
    if total_cells == 0:
        return 0

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    space_issues = 0
    for col in df.select_dtypes(include="object"):
        space_issues += df[col].astype(str).str.contains(r"^\s|\s$", regex=True).sum()

    missing_penalty = (missing / total_cells) * 50
    duplicate_penalty = (duplicates / max(len(df), 1)) * 30
    format_penalty = (space_issues / total_cells) * 20

    score = 100 - (missing_penalty + duplicate_penalty + format_penalty)
    return round(max(score, 0), 2)

# SIDEBAR OPTIONS
st.sidebar.header("⚙️ Cleaning Options")

remove_nulls = st.sidebar.checkbox("Remove Rows with Missing Values")
remove_duplicates = st.sidebar.checkbox("Remove Duplicate Rows")

fill_method = st.sidebar.selectbox(
    "Fill Missing Values",
    ["None", "Mean", "Median", "Mode"]
)

lowercase_columns = st.sidebar.checkbox("Convert Column Names to Lowercase")
strip_spaces = st.sidebar.checkbox("Remove Extra Spaces from Text")
change_dtype = st.sidebar.checkbox("Convert Numeric Columns")
drop_columns = st.sidebar.checkbox("Drop Selected Columns")

# FILE UPLOAD
uploaded_files = st.file_uploader(
    "📂 Upload CSV or Excel Files",
    type=["csv", "xlsx"],
    accept_multiple_files=True
)

# PROCESS FILES
if uploaded_files:
    for uploaded_file in uploaded_files:
        st.markdown("---")
        st.subheader(f"📄 File: {uploaded_file.name}")

        # Load data
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        original_df = df.copy()

        # KPIs BEFORE CLEANING
        st.markdown("### 📊 Data Quality (Before Cleaning)")
        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric("Rows", df.shape[0])
        c2.metric("Columns", df.shape[1])
        c3.metric("Duplicates", df.duplicated().sum())
        c4.metric("Missing Values", df.isnull().sum().sum())
        c5.metric("Quality Score", f"{data_quality_score(df)} / 100")

        st.markdown("### 🔍 Original Data Preview")
        st.dataframe(df.head())

        cleaned_df = df.copy()

        # CLEANING STEPS
        if lowercase_columns:
            cleaned_df.columns = cleaned_df.columns.str.lower()

        if strip_spaces:
            for col in cleaned_df.select_dtypes(include="object"):
                cleaned_df[col] = cleaned_df[col].str.strip()

        if fill_method != "None":
            for col in cleaned_df.select_dtypes(include="number"):
                if fill_method == "Mean":
                    cleaned_df[col].fillna(cleaned_df[col].mean(), inplace=True)
                elif fill_method == "Median":
                    cleaned_df[col].fillna(cleaned_df[col].median(), inplace=True)

            for col in cleaned_df.select_dtypes(include="object"):
                if fill_method == "Mode":
                    cleaned_df[col].fillna(cleaned_df[col].mode()[0], inplace=True)

        if remove_nulls:
            cleaned_df = cleaned_df.dropna()

        if remove_duplicates:
            cleaned_df = cleaned_df.drop_duplicates()

        if change_dtype:
            for col in cleaned_df.columns:
                cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors="ignore")

        if drop_columns:
            cols_to_drop = st.multiselect(
                "Select columns to drop",
                cleaned_df.columns,
                key=uploaded_file.name
            )
            cleaned_df = cleaned_df.drop(columns=cols_to_drop)

        # KPIs AFTER CLEANING
        st.markdown("### 📊 Data Quality (After Cleaning)")
        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric("Rows After", cleaned_df.shape[0])
        c2.metric("Rows Removed", original_df.shape[0] - cleaned_df.shape[0])
        c3.metric("Duplicates Removed", original_df.duplicated().sum())
        c4.metric("Missing After", cleaned_df.isnull().sum().sum())
        c5.metric("Quality Score", f"{data_quality_score(cleaned_df)} / 100")

        st.markdown("### ✅ Cleaned Data Preview")
        st.dataframe(cleaned_df.head())

        # DOWNLOAD
        buffer = io.BytesIO()
        if uploaded_file.name.endswith(".csv"):
            cleaned_df.to_csv(buffer, index=False)
            mime = "text/csv"
        else:
            cleaned_df.to_excel(buffer, index=False)
            mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        st.download_button(
            "⬇️ Download Cleaned File",
            buffer.getvalue(),
            file_name=f"cleaned_{uploaded_file.name}",
            mime=mime
        )

    st.success("🎉 All files cleaned successfully!")

else:
    st.info("👆 Upload files to start cleaning.")
