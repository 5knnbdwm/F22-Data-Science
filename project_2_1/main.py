"""
project_2_1
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_data = pd.read_csv(
    './input/ECA_blended_custom_germany_aachen/TG_STAID000356.txt',
    names=["SOUID", "DATE", "TG", "Q_TG"],
    skiprows=20)
df_base = pd.DataFrame(csv_data)

print("---")
print("task 3")
print("---")

df_base['mean_temp'] = df_base['TG']/10

plt.plot(df_base["mean_temp"], linewidth=0.5)
plt.ylabel('Temperature')
plt.savefig("df_3.png", dpi=150)
plt.clf()

print("---")
print("task 4")
print("---")

df_base['DATE'] = df_base['DATE'].map(str)
df_base['part_year'] = df_base['DATE'].str[:4]
df_base['part_month'] = df_base['DATE'].str[4:6]
df_base['part_day'] = df_base['DATE'].str[6:]

df_base['date'] = df_base['part_year'] + "-" + df_base['part_month'] + "-" + df_base['part_day']
df_base = df_base.set_index(pd.to_datetime(df_base['date']))

plt.plot(df_base["mean_temp"], linewidth=0.5)
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.savefig("df_4.png", dpi=150)
plt.clf()

print("---")
print("task 5")
print("---")

# df_no_outliers = df_base.copy()
# df_no_outliers = df_no_outliers[df_no_outliers['mean_temp']!= -999.9]

# df_base = df_base.loc[:'1899-12-31']
# df_base = df_base.loc[:'1915-01-31']

base_index = df_base.index.to_period('M')

min_year = df_base['part_year'].astype(int).min()

for index,row in df_base.iterrows():

    if (min_year != index.year) & (row['mean_temp'] == -999.9):

        result = df_base[base_index == str(index.year - 1)+'-'+str(index.month)]['mean_temp'].mean()
        df_base.loc[index,"mean_temp"] = result

plt.plot(df_base["mean_temp"], linewidth=0.5)
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.savefig("df_5.png", dpi=150)
plt.clf()

print("---")
print("task 6")
print("---")

df_6 = df_base.copy()

df_6 = df_6.loc[:'2021-12-31']

plt.plot(df_6["mean_temp"], linewidth=0.5)
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.savefig("df_6.png", dpi=150)
plt.clf()

print("---")
print("task 7")
print("---")

df_7 = df_6.resample('Y').median()

plt.plot(df_7["mean_temp"], linewidth=0.5)
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.savefig("df_7.png", dpi=150)
plt.clf()

print("---")
print("task 8")
print("---")

df_8 = df_7.copy()

cmap = plt.get_cmap('coolwarm')

plt.figure(figsize=(15, 5))
plt.title('yearly median temperature')
heatm_plot = sns.heatmap([df_8['mean_temp']], cmap=cmap, cbar=False, yticklabels=[], xticklabels=[])

heatm_fig = heatm_plot.get_figure()
heatm_fig.savefig('df_8.png')
