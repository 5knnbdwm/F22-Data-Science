"""
project_1_2
"""
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print("---")
    print("task 1")
    print("---")

    csv_data = pd.read_csv("./national/yob2000.txt", names=["name", "gender", "amount"])
    df_2000 = pd.DataFrame(csv_data)

    df_2000['percentage'] = df_2000['amount'] / df_2000['amount'].sum() * 100
    print(df_2000["percentage"].sort_values(ascending=False))

    print("---")
    print("task 2")
    print("---")

    df_all = pd.DataFrame()

    for year in range(1880,2022):
        filename = "./national/yob" + str(year) + ".txt"
        # print(filename)
        csv_data = pd.read_csv(filename, names=["name", "gender", "amount"])
        df_year = pd.DataFrame(csv_data)
        df_year['year'] = year
        # print(df_year)
        df_all = pd.concat([df_all, df_year])
        # pd.concat([male_top5_df, female_top5_df])

    df_all.reset_index()


    print("---")
    print("task 3")
    print("---")

    df_all_year = df_all.groupby(['year']).sum()

    plt.plot(
        df_all_year,
    )
    plt.xlabel("Amount")
    plt.ylabel("Year")
    plt.title("Number of Birth per year")
    plt.savefig("df_all_year.png", dpi=150)

    plt.clf()

    print("---")
    print("task 4")
    print("---")

    df_all_year_samuel = df_all.loc[df_all['name']=='Samuel']

    plt.plot(df_all_year_samuel['year'], df_all_year_samuel['amount'])
    plt.xlabel("Amount")
    plt.ylabel("Year")
    plt.title("Number of Birth per year named Samuel")
    plt.savefig("df_all_year_samuel.png", dpi=150)

    plt.clf()

    print("---")
    print("task 5")
    print("---")


    fig, ax = plt.subplots()

    names = ['Madonna', 'Lance', 'Barack', 'Katrina', 'Luke', 'Leia', 'Frida', 'Arielle', 'Harley', 'Tyrion', 'Khaleesi']

    for name in names:
        df_all_year_name = df_all.loc[df_all['name']==name]
        ax.plot(df_all_year_name['year'], df_all_year_name['amount'], label=name)
        ax.legend()

    plt.savefig("df_all_year_names.png", dpi=150)
