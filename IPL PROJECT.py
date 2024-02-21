#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df= pd.read_csv("IPL Dataset.csv")
df


# In[7]:


df.info()


# In[26]:


# Question 1: What is the total number of matches in the dataset?
total_matches = len(df)
print("Total number of matches:", total_matches)


# In[14]:


# Question 2: How many seasons are covered in the dataset,
# and what are their start and end dates?
seasons_info =df['season'].describe()
plt.hist(df['season'], bins=len(df['season'].unique()))
plt.xlabel('Season')
plt.ylabel('Frequency')
plt.title('Distribution of Seasons')
plt.show()


# In[15]:


# Question 3: What are the unique venues where matches have been played?
unique_venues = df['venue'].unique()
# Visualization for  Unique venues where matches have been played
plt.figure(figsize=(10,6))
plt.barh(range(len(unique_venues)), df['venue'].value_counts())
plt.yticks(range(len(unique_venues)), unique_venues)
plt.xlabel('Number of Matches')
plt.ylabel('Venue')
plt.title('Number of Matches Played at Each Venue')
plt.show()


# In[28]:


# Question 4: How many innings are included in the dataset,
# and what is the average number of innings per match?
total_innings = df['innings'].count()
average_innings_per_match = total_innings / total_matches
print("total_innings are:",total_innings)
print("average_innings_per_matches are:",average_innings_per_match)


# In[32]:


# Question 5: Which batting team has appeared the most in the dataset,
# and how many matches have they played?
batting_team_appearances = df['batting_team'].value_counts()
most_appearances_batting_team = batting_team_appearances.idxmax()
matches_played_most_appearances_batting_team = batting_team_appearances.max()
print("batting_team_appearances:",batting_team_appearances)

print("most_appearances_batting_team:",most_appearances_batting_team)
print("matches_played_most_appearances_batting_team:",matches_played_most_appearances_batting_team)


# In[33]:


# Question 6: Similarly, which bowling team has appeared the most,
# and how many matches have they played?
bowling_team_appearances = df['bowling_team'].value_counts()
print("bowling_team_appearances:",bowling_team_appearances)

most_appearances_bowling_team = bowling_team_appearances.idxmax()
print("most_appearances_bowling_team:",most_appearances_bowling_team)

matches_played_most_appearances_bowling_team = bowling_team_appearances.max()
print("matches_played_most_appearances_bowling_team:",matches_played_most_appearances_bowling_team)


# In[34]:


# Question 7: What is the average number of runs scored per match?
average_runs_per_match =df['run'].mean()
print("average_runs_per_match:",average_runs_per_match)


# In[35]:


# Question 8: What is the average number of wickets taken per match?
average_wickets_per_match = df['player_dismissed'].count() / total_matches
print("average_wickets_per_match:",average_wickets_per_match)


# In[11]:


# Most run Scored by IPL team 
df.groupby(['batting_team'])['run'].sum().sort_values(ascending=False)


# In[23]:


# Question 9: What is the distribution of runs scored off the bat versus extras across all matches?
runs_off_bat_total =df['runs_off_bat'].sum()
extras_total = df['extras'].sum()
# Visualization for  Distribution of runs scored off the bat versus extras
labels = ['Runs off Bat', 'Extras']
sizes = [runs_off_bat_total, extras_total]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Distribution of Runs Scored off the Bat vs Extras')
plt.show()


# In[36]:


# Question 10: Which player has scored the highest number of runs in a single match, and in which match did this occur?
max_runs_in_single_match = df.groupby('match_id')['run'].sum().max()
print("max_runs_in_single_match:",max_runs_in_single_match)


# In[ ]:


#most IPL run by batsman


# In[12]:


#Question11- Avg Run by Teams in powerplay
df[df['over']<6].groupby(['match_id','batting_team']).sum()['run'].groupby('batting_team').mean().sort_values(ascending=False)[2:]


# In[18]:


# Question 12-Most Ipl century by a player
runs=df.groupby(['striker','match_id'])['runs_off_bat'].sum()
runs[runs>=100].droplevel(level=1).groupby('striker').count().sort_values(ascending=False)[:10]


# In[ ]:




