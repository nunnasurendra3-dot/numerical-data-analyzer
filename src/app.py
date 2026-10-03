import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Student Analytics Portal",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Statistics",
        "Rankings",
        "At Risk Students",
        "Reports"
    ]
)

# Portal Header
st.markdown("""
<h1 style='text-align:center;color:#1E88E5;'>
🎓 Student Performance Analytics Portal
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center;'>
Department of Artificial Intelligence & Machine Learning
</h4>
""", unsafe_allow_html=True)

st.markdown("---")

uploaded_file = st.file_uploader(
    "📂 Upload Student Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.markdown("""
    <h2 style='text-align:center;'>
    📊 Dashboard Overview
    </h2>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👨‍🎓 Students",
            len(df)
        )

    with col2:
        st.metric(
            "🏆 Top Math Score",
            df["Math_Score"].max()
        )

    with col3:
        st.metric(
            "📐 Avg Math Score",
            round(df["Math_Score"].mean(), 2)
        )

    with col4:
        st.metric(
            "📅 Avg Attendance",
            f"{round(df['Attendance'].mean(), 1)}%"
        )

    st.markdown("---")

    st.subheader("📋 Dataset Preview")
    st.dataframe(df)

    numerical_cols = df.select_dtypes(include="number").columns

    st.markdown("---")

    st.subheader("📊 Statistical Analysis")

    for col in numerical_cols:

        st.write(f"### {col}")

        stats = {
            "Mean": round(df[col].mean(), 2),
            "Median": df[col].median(),
            "Minimum": df[col].min(),
            "Maximum": df[col].max(),
            "Standard Deviation": round(df[col].std(), 2)
        }

        st.write(stats)

    st.markdown("---")

    st.subheader("🔥 Correlation Heatmap")

    corr = df[numerical_cols].corr()

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("🏆 Student Ranking System")

    df["Total_Score"] = (
        df["Math_Score"]
        + df["Reading_Score"]
        + df["Writing_Score"]
    )

    top_student = df.loc[
        df["Total_Score"].idxmax()
    ]

    st.success(
        f"Top Performer: Student {top_student['Student_ID']} | Total Score: {top_student['Total_Score']}"
    )

    st.markdown("---")

    st.subheader("🥇 Top 10 Students")

    top10 = df.sort_values(
        by="Total_Score",
        ascending=False
    )

    st.dataframe(
        top10[
            [
                "Student_ID",
                "Math_Score",
                "Reading_Score",
                "Writing_Score",
                "Total_Score"
            ]
        ].head(10)
    )

    st.markdown("---")

    st.subheader("⚠️ At-Risk Students")

    at_risk = df[
        (df["Math_Score"] < 60)
        |
        (df["Attendance"] < 75)
    ]

    st.dataframe(at_risk)

    st.markdown("---")

    st.subheader("📈 Subject Performance Comparison")

    subjects = [
        "Math",
        "Reading",
        "Writing"
    ]

    averages = [
        df["Math_Score"].mean(),
        df["Reading_Score"].mean(),
        df["Writing_Score"].mean()
    ]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        subjects,
        averages,
        color=[
            "blue",
            "green",
            "orange"
        ]
    )

    ax.set_title("Average Subject Scores")
    ax.set_ylabel("Average Marks")

    st.pyplot(fig)

    st.markdown("---")

    report_text = f"""
STUDENT PERFORMANCE REPORT

Total Students: {len(df)}

Average Math Score:
{round(df['Math_Score'].mean(), 2)}

Average Attendance:
{round(df['Attendance'].mean(), 2)}

At Risk Students:
{len(at_risk)}
"""

    st.download_button(
        "📥 Download Report",
        report_text,
        file_name="student_report.txt"
    )

    st.markdown("---")

    st.subheader("🤖 AI Insights")

    st.info(
        f"Average Math Score of all students is {round(df['Math_Score'].mean(), 2)}."
    )

    st.info(
        f"Average Attendance is {round(df['Attendance'].mean(), 2)}%."
    )

    st.info(
        f"{len(at_risk)} students require academic attention."
    )

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px 0;
        color: #777;
        font-size: 14px;
        background-color: transparent;
    }
    </style>

    <div class="footer">
        © 2026 <strong>NUNNA SURENDRA</strong> · Numerical Data Analyzer
    </div>
    """,
    unsafe_allow_html=True
)