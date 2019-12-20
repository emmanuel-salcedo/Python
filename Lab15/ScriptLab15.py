import matplotlib.pyplot as plt
import pandas as pd

pokemon = pd.read_csv('/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/pokemon.csv')
pokemon = pokemon.set_index(['#'])
# print(pokemon.columns)
# print(pokemon.head())
# print(pokemon.shape)
#
## Read each Column
# print(pokemon[['Name', 'Type 1', 'HP']])
#
# # Read Each Row
# print(pokemon.iloc[0:4])
# for index, row in pokemon.iterrows():
#     print(index, row['Name'])

# All pokemon
plt.rcdefaults()
fig1, ax1 = plt.subplots(figsize=(6, 6))
type1 = pd.value_counts(pokemon['Type 1'])
y_pos = type1
ax1.bar(type1.index, type1, align='center', color='red')
ax1.set_xlabel('Types')
ax1.set_title('Pokemon by Primary type')
plt.xticks(fontsize=6, rotation=90)

Gen1 = pokemon.loc[pokemon['Generation'] == 1]
Gen2 = pokemon.loc[pokemon['Generation'] == 2]
Gen3 = pokemon.loc[pokemon['Generation'] == 3]
Gen4 = pokemon.loc[pokemon['Generation'] == 4]
Gen5 = pokemon.loc[pokemon['Generation'] == 5]
Gen6 = pokemon.loc[pokemon['Generation'] == 6]

# gen 1 Types
fig2, ax2 = plt.subplots(figsize=(6, 6))
type2 = pd.value_counts(Gen1['Type 1'])
ax2.bar(type2.index, type2, align='center', color='green')
ax2.set_xlabel('Types')
ax2.set_title('Gen1 by Primary type')
plt.xticks(fontsize=6, rotation=90)

# gen2 types
fig3, ax3 = plt.subplots(figsize=(6, 6))
type3 = pd.value_counts(Gen2['Type 1'])
ax3.bar(type3.index, type3, align='center', color='purple')
ax3.set_xlabel('Types')
ax3.set_title('Gen2 by Primary type')
plt.xticks(fontsize=6, rotation=90)

fig4, ax4 = plt.subplots(figsize=(6, 6))
type4 = pd.value_counts(Gen3['Type 1'])
ax4.bar(type4.index, type4, align='center', color='blue')
ax4.set_xlabel('Types')
ax4.set_title('Gen3 by Primary type')
plt.xticks(fontsize=6, rotation=90)

fig5, ax5 = plt.subplots(figsize=(6, 6))
type5 = pd.value_counts(Gen4['Type 1'])
ax5.bar(type5.index, type5, align='center', color='orange')
ax5.set_xlabel('Types')
ax5.set_title('Gen4 by Primary type')
plt.xticks(fontsize=6, rotation=90)

plt.show()

## Read a specific location (R,C)
# print(pokemon.iloc[2, 1])

# plt.plot([1, 2, 3], [5, 7, 4])
# plt.show()
#
# AvgDrinksByCont = drinks.sort_values('continent').groupby('continent').beer_servings.mean().plot(kind='hist')
# plt.show(AvgDrinksByCont)
#
# days = [1, 2, 3, 4, 5, 6, 7]
#
# sleeping = [5, 5, 5, 5, 5, 7, 9]
# eating = [2, 2, 2, 2, 2, 3, 4]
# working = [12, 12, 12, 12, 12, 0, 0]
# playing = [4, 4, 4, 4, 4, 14, 11]
#
# plt.stackplot(days, sleeping, eating, working, playing, colors=['black', 'red', 'blue', 'c'])
# plt.show()
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [5, 7, 9, 11, 13, 10, 5, 3, 2, 18]
#
# plt.scatter(x, y, label='Random Scatter', color='r', marker='*')
# plt.show()
