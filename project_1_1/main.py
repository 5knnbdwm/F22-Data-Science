"""
project_1_1
"""
import pandas as pd

if __name__ == "__main__":
    csv_data = pd.read_csv("./national/yob2021.txt", names=["name", "gender", "amount"])
    df = pd.DataFrame(csv_data, )

    print("---")
    print("task 3")
    print("---")

    print(df.head(10))

    print("---")
    print("task 4")
    print("---")

    print("columns:", df.shape[1])
    print("rows:", df.shape[0])

    print("---")
    print("task 5")
    print("---")

    total_sum = df["amount"].sum()
    print("sum:", total_sum)

    print("---")
    print("task 6")
    print("---")

    male_df = df[df["gender"]=="M"]
    male_sum = male_df["amount"].sum()
    female_df = df[df["gender"]=="F"]
    female_sum = female_df["amount"].sum()

    print("male sum:", male_sum)
    print("female sum:", female_sum)

    print("---")
    print("task 7")
    print("---")

    print(df[df.eq("Samuel").any(1)])

    print("---")
    print("task 8")
    print("---")

    print("male percentage:", "{:.2%}".format(male_sum/total_sum))
    print("female percentage:", "{:.2%}".format(female_sum/total_sum))

    print("---")
    print("task 9")
    print("---")

    male_top5_df = male_df.sort_values(by=["amount"]).tail(5)
    female_top5_df = female_df.sort_values(by=["amount"]).tail(5)
    top5_df = pd.concat([male_top5_df, female_top5_df])

    print(top5_df)

    print("---")
    print("task 10")
    print("---")

    top5_df.to_excel('output/top5_male_female.xlsx')
    print("created file")
