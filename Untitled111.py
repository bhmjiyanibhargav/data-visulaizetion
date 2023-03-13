#!/usr/bin/env python
# coding: utf-8
Question 1 : Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot.

Answer : Seaborn is a powerful Python library used for creating informative and attractive visualizations. Here are five common types of plots that can be created using Seaborn and their uses:

Scatter Plot: Scatter plots are used to display the relationship between two continuous variables. They are useful for identifying patterns and trends in data, as well as identifying outliers.

Line Plot: Line plots are used to display trends over time or ordered categories. They are useful for showing changes in data over time or across categories.

Histogram: Histograms are used to display the distribution of a single continuous variable. They are useful for showing the shape of the data, as well as identifying outliers and skewness.

Bar Plot: Bar plots are used to display the relationship between a categorical variable and a continuous variable. They are useful for comparing groups or categories.

Heatmap: Heatmaps are used to display the relationship between two categorical variables or a categorical and a continuous variable. They are useful for identifying patterns and trends in complex data sets.Question 2 : Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using x = "timepoint" and y = "signal" for different events and regions.

Note: timepoint, signal, event, and region are columns in the fmri dataset.
# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset('fmri')

# create the line plot
sns.lineplot(data=fmri, x='timepoint', y='signal')

# add labels and title
plt.xlabel('timepoint')
plt.ylabel('signal')
plt.title('Question 1')

# show the plot
plt.show()

Question 3 : Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using x = 'pclass', y = 'age' and y = 'fare'.

Note: pclass, age, and fare are columns in the titanic dataset.
# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt

# load the titanic dataset
titanic = sns.load_dataset('titanic')

# create a subplot with two box plots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))

# plot age by pclass
sns.boxplot(x='pclass', y='age', data=titanic, ax=ax1)
ax1.set_title('Age by Passenger Class')

# plot fare by pclass
sns.boxplot(x='pclass', y='fare', data=titanic, ax=ax2)
ax2.set_title('Fare by Passenger Class')

# adjust spacing
fig.tight_layout()

# show the plot
plt.show()

Question 4 : Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue parameter for the 'cut' column of the diamonds dataset.
# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt

fig, ax1  = plt.subplots(ncols=1, figsize=(14, 5))

# load the titanic dataset
diamonds = sns.load_dataset('diamonds')

# create the histogram
sns.histplot(data=diamonds, x='price', hue='cut', ax= ax1)

plt.title('Question 4')
plt.show()

Question 5 : Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column of the iris dataset.Question 5 : Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column of the iris dataset.
# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt

# load the iris dataset
iris = sns.load_dataset('iris')

# create a pair plot
sns.pairplot(data = iris, hue="species")

# show the plot
plt.show()

Question 6 : Use the "flights" dataset from seaborn to plot a heatmap.
# In[5]:


import seaborn as sns

# load the flights dataset
flights = sns.load_dataset('flights')

# pivot the dataset to wide format
flights_wide = flights.pivot(index='month', columns='year', values='passengers')

# create the heatmap
sns.heatmap(flights_wide, cmap='coolwarm', annot=True, fmt='d')

# add labels and title
plt.xlabel('Year')
plt.ylabel('Month')
plt.title('Number of Passengers by Month and Year')

# show the plot
plt.show()


# In[ ]:




