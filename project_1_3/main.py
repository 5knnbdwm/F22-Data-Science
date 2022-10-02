"""
project_1_3
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from heatmap import heatmap, annotate_heatmap
import string
import random

if __name__ == "__main__":

    print("---")
    print("task 1")
    print("---")

    df_all = pd.DataFrame()

    for year in range(1880,2022):
        filename = "./national/yob" + str(year) + ".txt"
        csv_data = pd.read_csv(filename, names=["name", "gender", "amount"])
        df_year = pd.DataFrame(csv_data)
        df_year['year'] = year
        df_all = pd.concat([df_all, df_year])

    df_all.reset_index()

    print("---")
    print("task 2")
    print("---")

    df_all['last_char'] = df_all['name'].str[-1]

    print(df_all.head())

    print("---")
    print("task 3")
    print("---")

    df_all_years = df_all.copy()
    df_all_years['last_char_count']=df_all_years.groupby('last_char')['last_char'].transform('count')
    df_all_last_char_count = df_all_years.groupby('last_char')['last_char_count'].max()
    df_all_last_char = df_all_years.groupby('last_char')['last_char'].max()

    plt.bar(df_all_last_char, df_all_last_char_count)
    plt.xlabel("Letter")
    plt.ylabel("Occurance")
    plt.title("Number each letter is the last letter of birth names in all years")
    plt.savefig("df_all_last_char.png", dpi=150)

    plt.clf()

    print("---")
    print("task 4")
    print("---")

    letter = random.choice(string.ascii_letters).lower()

    print('choosen letter: ' + letter)

    df_single_letter = df_all[df_all["last_char"]==letter]
    df_single_letter['last_char_count']=df_single_letter.groupby(['year','last_char'])['last_char'].transform('count')
    df_single_letter_last_char_count = df_single_letter.groupby('year')['last_char_count'].max()

    plt.plot(df_single_letter_last_char_count)
    plt.xlabel("Year")
    plt.ylabel("Occurance")
    plt.title(f"Number of occurances for the letter {letter} as last letter in birth names")
    plt.savefig("df_all_last_char_select_letter.png", dpi=150)

    plt.clf()

    print("---")
    print("task 5")
    print("---")

    df_all_5 = df_all.copy()

    df_all_5_unstacked = df_all_5.groupby(['last_char', 'year'])['amount'].count().unstack(0)

    print(df_all_5_unstacked.head())
    plt.plot(df_all_5_unstacked)
    plt.legend(df_all_5_unstacked)
    plt.xlabel("Year")
    plt.ylabel("Occurance")
    # plt.title(f"Number of occurances for the letter {letter} as last letter in birth names")
    plt.savefig("df_all_5.png", dpi=150)

    plt.clf()

    # print("---")
    # print("task 6")
    # print("---")

    # df_all_6 = df_all.copy()

    # df_all_6['first_char'] = df_all_6['name'].str[1]

    # df_all_6['name'].str.upper()

    # df_6_unstacked = df_all_6.groupby(['first_char', 'last_char'])['amount'].corr().unstack()
    
    # print(df_6_unstacked)

    # # fig, ax = plt.subplots()

    # # im, cbar = heatmap(df_6_unstacked, df_6_unstacked['first_char'], df_6_unstacked['first_char'], ax=ax,
    # #                 cmap="YlGn", cbarlabel="harvest [t/year]")
    # # texts = annotate_heatmap(im, valfmt="{x:.1f} t")

    # # fig.tight_layout()
    # # plt.show()

    # # # plt.setp(df_6_unstacked)
    # # # # plt.legend(df_all_5_unstacked)
    # # # # plt.xlabel("Year")
    # # # # plt.ylabel("Occurance")
    # # # # # plt.title(f"Number of occurances for the letter {letter} as last letter in birth names")
    # # # plt.savefig("df_6_heat.png", dpi=150)

    # # # plt.clf()