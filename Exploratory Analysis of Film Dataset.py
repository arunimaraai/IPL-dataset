#!/usr/bin/env python
# coding: utf-8

# In[5]:


pwd


# In[6]:


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\LENOVO\movies.csv")
print(data)


# In[7]:


size=df.size
print("Size={}".format(size))


# In[8]:


df.info()


# In[11]:


shape=df.shape
print("Shape={}".format(shape))


# In[12]:


df.info()


# In[4]:


df.head(-5)


# In[14]:


# 1. What is the distribution of films across different genres?
genre_distribution = df['Genre'].value_counts()
print("Distribution of films across different genres:")
print(genre_distribution)
print()

# visualisation of films across different genres
plt.figure(figsize=(10, 6))
sns.countplot(x='Genre', data=df)
plt.title('Distribution of Films Across Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[15]:


# 2. Which lead studio has the highest number of films in the dataset?
lead_studio_counts = df['Lead Studio'].value_counts()
max_lead_studio = lead_studio_counts.idxmax()
print("Lead studio with the highest number of films:", max_lead_studio)
print()

# visualisation of Number of films produced by each lead studio
plt.figure(figsize=(10, 6))
sns.countplot(x='Lead Studio', data=df)
plt.title('Number of Films Produced by Lead Studio')
plt.xlabel('Lead Studio')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[16]:


# 3. What is the average audience score percentage for the films?
avg_audience_score = df['Audience score %'].mean()
print("Average audience score percentage:", avg_audience_score)
print()

# visualisation of Average audience score percentage for the films
plt.figure(figsize=(8, 5))
sns.barplot(x='Audience score %', y='Film', data=df)
plt.title('Average Audience Score Percentage for Films')
plt.xlabel('Audience Score %')
plt.ylabel('Film')
plt.show()


# In[17]:


# 4. What is the average profitability of the films?
avg_profitability = df['Profitability'].mean()
print("Average profitability:", avg_profitability)
print()

# visualisation of Average profitability of the films
plt.figure(figsize=(8, 5))
sns.barplot(x='Profitability', y='Film', data=df)
plt.title('Average Profitability of Films')
plt.xlabel('Profitability')
plt.ylabel('Film')
plt.show()


# In[18]:


# 5. How does the audience score percentage correlate with the Rotten Tomatoes percentage?
correlation = df['Audience score %'].corr(df['Rotten Tomatoes %'])
print("Correlation between Audience Score % and Rotten Tomatoes %:", correlation)
print()

# visualisation of Relationship between Audience Score Percentage and Rotten Tomatoes Percentage
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Audience score %', y='Rotten Tomatoes %', data=df)
plt.title('Audience Score vs Rotten Tomatoes')
plt.xlabel('Audience Score %')
plt.ylabel('Rotten Tomatoes %')
plt.show()


# In[19]:


# 6. Is there any relationship between profitability and audience score percentage?
profitability_vs_audience_score = df[['Profitability', 'Audience score %']].corr().iloc[0, 1]
print("Correlation between Profitability and Audience Score %:", profitability_vs_audience_score)
print()

# visualisation of Relationship between Profitability and Audience Score Percentage
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Profitability', y='Audience score %', data=df)
plt.title('Profitability vs Audience Score')
plt.xlabel('Profitability')
plt.ylabel('Audience Score %')
plt.show()


# In[24]:


# 7. How does the worldwide gross vary across different genres?
worldwide_gross_by_genre = df.groupby('Genre')['Worldwide Gross'].sum()
df['Worldwide Gross'] = df['Worldwide Gross'].replace('[\$,]', '', regex=True).astype(float)


print("Worldwide gross by genre:")
print(worldwide_gross_by_genre)
print()

#visualisation of Boxplot of Worldwide Gross across different genres
plt.figure(figsize=(10, 6))
sns.boxplot(x='Genre', y='Worldwide Gross', data=df)
plt.title('Worldwide Gross Across Genres')
plt.xlabel('Genre')
plt.ylabel('Worldwide Gross')
plt.xticks(rotation=45)
plt.show()


# In[21]:


# 8. What is the trend in audience score percentage over the years?
trend_audience_score_year = df.groupby('Year')['Audience score %'].mean()
print("Trend in audience score percentage over the years:")
print(trend_audience_score_year)
print()

# visualisation of Trend in Audience Score Percentage over the years
plt.figure(figsize=(8, 5))
sns.lineplot(x='Year', y='Audience score %', data=df)
plt.title('Trend in Audience Score Percentage Over the Years')
plt.xlabel('Year')
plt.ylabel('Audience Score %')
plt.show()


# In[22]:


# 9. Are there any outliers in the profitability of films?
q1 = df['Profitability'].quantile(0.25)
q3 = df['Profitability'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df['Profitability'] < lower_bound) | (df['Profitability'] > upper_bound)]
print("Outliers in profitability:")
print(outliers)
print()

#  Boxplot of Profitability to identify outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x='Profitability', data=df)
plt.title('Boxplot of Profitability')
plt.xlabel('Profitability')
plt.show()


# In[23]:


# 10. Which genre has the highest average Rotten Tomatoes percentage?
avg_rotten_tomatoes_genre = df.groupby('Genre')['Rotten Tomatoes %'].mean()
max_avg_rotten_tomatoes_genre = avg_rotten_tomatoes_genre.idxmax()
print("Genre with the highest average Rotten Tomatoes percentage:", max_avg_rotten_tomatoes_genre)

# visualisation of  Average Rotten Tomatoes percentage by genre
plt.figure(figsize=(10, 6))
sns.barplot(x='Genre', y='Rotten Tomatoes %', data=df)
plt.title('Average Rotten Tomatoes Percentage by Genre')
plt.xlabel('Genre')
plt.ylabel('Rotten Tomatoes %')
plt.xticks(rotation=45)
plt.show()

