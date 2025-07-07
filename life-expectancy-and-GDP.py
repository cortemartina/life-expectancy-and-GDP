import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

all_data = pd.read_csv('/Users/martinacorte/Codecademy/Data Scientist/Projects/Life-Expectancy-and-GDP-Starter/all_data.csv')

# print(all_data.head())
print(all_data.describe())
print(all_data.info())
print(all_data['Country'].unique())

# Task 1
# Has life expectancy increased over time in the six nations?
sns.lineplot(data=all_data, x='Year', y='Life expectancy at birth (years)', hue='Country', palette='pastel', marker='o')
plt.xlabel('Time')
plt.ylabel('Years')
plt.title('Life expectancy over time')
plt.show()

# Task 2
# Has GDP increased over time in the six nations?
sns.lineplot(data=all_data, x='Year', y='GDP', hue='Country', palette='pastel', marker='o')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('GDP over time')
plt.show()

# Task 3
# Is there a correlation between GDP and life expectancy of a country?
countries = all_data['Country'].unique()
fig, axes = plt.subplots(3, 2, figsize=(12, 18))
axes = axes.flatten()
colors = sns.color_palette('pastel', n_colors=len(countries))
for i, country in enumerate(countries):
    country_data = all_data[all_data['Country'] == country]

    sns.lineplot(
        data=country_data,
        x='GDP',
        y='Life expectancy at birth (years)',
        marker='o',
        ax=axes[i],
        color=colors[i]
    )

    axes[i].set_title(f'Life Expectancy vs GDP - {country}')
    axes[i].set_xlabel('GDP')
    axes[i].set_ylabel('Life Expectancy at Birth (years)')

plt.tight_layout()
plt.show()

# Task 4 
# What is the average life expectancy in these nations?
for country in countries:
    country_data = all_data[all_data['Country'] == country]
    avg_life_expectancy_country = country_data['Life expectancy at birth (years)'].mean()
    print(f'Average life expectancy in {country}: {avg_life_expectancy_country:.1f} years.')

# Task 5
# What is the distribution of that life expectancy?
plt.figure(figsize=(12,8))
sns.boxplot(x='Country', y=all_data['Life expectancy at birth (years)'], data=all_data, palette='pastel')
plt.title('Boxplot of Life Expectancy')
plt.show()

# Conclusions
# This project was able to make quite a few data visualizations with the data even though there were only 96 rows and 4 columns. 

# The project was also able to answer some of the questions posed in the beginning:

# Has life expectancy increased over time in the six nations?
# Yes, with Zimbabwe having the greatest increase.

# Has GDP increased over time in the six nations?
# GDP has also increased for all countries in our list, especially for China.

# Is there a correlation between GDP and life expectancy of a country?
# Yes, there is a positive correlation between GDP and life expectancy for countries in our list.

# What is the average life expectancy in these nations?
# Average life expectancy was between mid to high 70s for the countries except for Zimbabwe which was 50.

# What is the distribution of that life expectancy?
# The life expectancy had a left skew, or most of the observations were on the right side.








