from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="Student Analytics API"
)

# Load dataset once
df = pd.read_csv("../data/sample.csv")

@app.get("/")
def home():

    return {
        "message": "Student Analytics API Running Successfully"
    }


@app.get("/statistics")
def statistics():

    return {
        "students": len(df),
        "avg_math": round(df["Math_Score"].mean(), 2),
        "avg_reading": round(df["Reading_Score"].mean(), 2),
        "avg_writing": round(df["Writing_Score"].mean(), 2),
        "avg_attendance": round(df["Attendance"].mean(), 2)
    }


@app.get("/top-performer")
def top_performer():

    df["Total_Score"] = (
        df["Math_Score"]
        + df["Reading_Score"]
        + df["Writing_Score"]
    )

    top_student = df.loc[
        df["Total_Score"].idxmax()
    ]

    return {
        "student_id": int(top_student["Student_ID"]),
        "total_score": float(top_student["Total_Score"])
    }


@app.get("/at-risk")
def at_risk_students():

    at_risk = df[
        (df["Math_Score"] < 60)
        |
        (df["Attendance"] < 75)
    ]

    return {
        "at_risk_count": len(at_risk),
        "students": at_risk.to_dict(
            orient="records"
        )
    }