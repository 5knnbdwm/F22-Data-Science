import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame(
    {"size": [33, 33, 33], "explode": [0.1] * 3}, index=["code review", "Q&A", "recap"]
)

plt.pie(
    df["size"],
    labels=df.index,
    explode=df["explode"],
    normalize=True,
    shadow=True,
    autopct="%1.1f%%",
)
plt.title("Classroom Activities in DS:F22")
plt.savefig("piechart.png", dpi=150)
