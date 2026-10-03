import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/sample.csv")

# Remove Student_ID
data = df.drop("Student_ID", axis=1)

# Correlation matrix
corr_matrix = data.corr()

print(corr_matrix)

# Heatmap
plt.figure(figsize=(8,6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Student Performance Correlation Heatmap")

plt.savefig("../reports/correlation_heatmap.png")
plt.show()