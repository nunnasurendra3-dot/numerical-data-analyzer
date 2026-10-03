import pandas as pd

# Load dataset
df = pd.read_csv("../data/sample.csv")

print(df.head())

columns = [
    "Math_Score",
    "Reading_Score",
    "Writing_Score",
    "Attendance"
]

for col in columns:

    print(f"\n===== {col} =====")

    print("Mean:", round(df[col].mean(), 2))
    print("Median:", df[col].median())
    print("Min:", df[col].min())
    print("Max:", df[col].max())
    print("Std Dev:", round(df[col].std(), 2))

    # IQR Outlier Detection
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[col][
        (df[col] < lower) |
        (df[col] > upper)
    ]

    print("Outliers:", outliers.tolist())