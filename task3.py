import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Quotes_Dataset.csv")
author_counts = df["Author"].value_counts()

plt.figure(figsize=(8,5))

author_counts.plot(kind="bar")

plt.title("Number of Quotes by Each Author")

plt.xlabel("Authors")

plt.ylabel("Number of Quotes")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("BarChart_Quotes.png")

plt.show()

# Pie Chart

plt.figure(figsize=(8,8))

author_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Percentage of Quotes by Each Author")

plt.ylabel("")

plt.tight_layout()

plt.savefig("PieChart_Quotes.png")

plt.show()

plt.figure(figsize=(8,5))

author_counts.plot(kind="barh")

plt.title("Horizontal Bar Chart of Quotes by Author")

plt.xlabel("Number of Quotes")

plt.ylabel("Authors")

plt.tight_layout()

plt.savefig("HorizontalBarChart.png")

plt.show()

plt.figure(figsize=(8,5))

author_counts.plot(kind="line", marker="o")

plt.title("Line Chart of Quotes by Author")

plt.xlabel("Authors")

plt.ylabel("Number of Quotes")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("LineChart.png")

plt.show()