#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df= pd.read_csv("IPL Dataset.csv",sep=",")
df


# In[5]:


df.head(-5)


# In[7]:


df.info()


# In[12]:


# "Which batting team has the highest average runs per match across all seasons? How does this vary when considering specific venues?"
average_runs_per_match = df.groupby('batting_team')['run'].mean()
batting_team_with_highest_average_runs = average_runs_per_match.idxmax()
average_runs_per_match.plot(kind='bar')
plt.title('Average Runs per Match by Batting Team')
plt.xlabel('Batting Team')
plt.ylabel('Average Runs per Match')
plt.show()


# In[15]:


# Question 2
# What is the distribution of runs scored off the bat versus extras across different innings of a match?
runs_off_bat_distribution = df.groupby('innings')['runs_off_bat'].sum()
extras_distribution = df.groupby('innings')['extras'].sum()
fig, ax = plt.subplots()
width = 0.35
ind = range(len(runs_off_bat_distribution))
p1 = ax.bar(ind, runs_off_bat_distribution, width, label='Runs off Bat')
p2 = ax.bar(ind, extras_distribution, width, bottom=runs_off_bat_distribution, label='Extras')
ax.set_title('Distribution of Runs Scored off the Bat vs Extras by Innings')
ax.set_xlabel('Innings')
ax.set_ylabel('Runs')
ax.legend()
plt.show()


# In[17]:


# Question 3
# Are there any noticeable trends in the number of wides and no-balls bowled by the bowling team over different seasons?
wides_per_season = df.groupby('season')['wides'].sum()
noballs_per_season = df.groupby('season')['noballs'].sum()
plt.plot(wides_per_season.index, wides_per_season, label='Wides')
plt.plot(noballs_per_season.index, noballs_per_season, label='No-balls')
plt.title('Wides and No-balls Bowled per Season')
plt.xlabel('Season')
plt.ylabel('Number of Wides/No-balls')
plt.legend()
plt.show()


# In[19]:


# Question 4
# How does the average number of runs scored per over vary throughout a match?
average_runs_per_over = df.groupby(['match_id', 'over'])['run'].sum().groupby('over').mean()

# Line plot for average number of runs scored per over throughout a match
average_runs_per_over.plot()
plt.title('Average Runs per Over Throughout a Match')
plt.xlabel('Over')
plt.ylabel('Average Runs per Over')
plt.show()


# In[22]:


# Question 5
# Is there a correlation between the number of runs scored by a team and the number of wickets taken by the opposing team?
correlation_runs_wickets = df.groupby('match_id')[['run', 'player_dismissed']]

# Correlation between runs scored by a team and wickets taken by the opposing team
plt.scatter(df['run'], df['player_dismissed'])
plt.title('Correlation between Runs Scored and Wickets Taken')
plt.xlabel('Runs Scored by Team')
plt.ylabel('Wickets Taken by Opposing Team')
plt.show()


# In[24]:


# Question 6
# Which bowler has the highest average number of wickets per match?
average_wickets_per_match = df.groupby('bowler')['player_dismissed'].count() / df.groupby('bowler')['match_id'].nunique()
top_bowler_by_average_wickets = average_wickets_per_match.idxmax()

# Bar plot for average number of wickets per match by bowler
average_wickets_per_match.plot(kind='bar')
plt.title('Average Wickets per Match by Bowler')
plt.xlabel('Bowler')
plt.ylabel('Average Wickets per Match')
plt.show()


# In[25]:


# Question 7
# Are there any particular overs where batting teams tend to score significantly more runs?
average_runs_per_over = df.groupby('over')['run'].mean()
overs_with_highest_average_runs = average_runs_per_over[average_runs_per_over > average_runs_per_over.mean() + 1.5 * average_runs_per_over.std()].index.tolist()
 
    # Bar plot for overs where batting teams tend to score significantly more runs
plt.bar(overs_with_highest_average_runs, average_runs_per_over[overs_with_highest_average_runs])
plt.title('Overs with Highest Average Runs')
plt.xlabel('Over')
plt.ylabel('Average Runs')
plt.show()


# In[29]:


# Question 8
# What is the average number of runs scored per over for each batting team, and how does this compare to their overall average across all matches?
average_runs_per_over_by_team = df.groupby(['batting_team', 'over'])['run'].mean().groupby('batting_team').mean()
overall_average_runs_per_team = df.groupby('batting_team')['run'].mean()

# Bar plot for average number of runs scored per over for each batting team
average_runs_per_over_by_team.plot(kind='bar')
plt.title('Average Runs per Over by Batting Team')
plt.xlabel('Batting Team')
plt.ylabel('Average Runs per Over')
plt.show()


# In[30]:


# Question 9
# Do certain types of dismissals tend to occur more frequently in specific overs of a match?
dismissals_per_over = df.groupby(['over', 'wicket_type']).size().unstack(fill_value=0)

# Stacked bar plot for types of dismissals occurring in specific overs
dismissals_per_over.plot(kind='bar', stacked=True)
plt.title('Types of Dismissals per Over')
plt.xlabel('Over')
plt.ylabel('Number of Dismissals')
plt.legend(title='Dismissal Type')
plt.show()


# In[32]:


# Question 10
# Is there a relationship between the start date of a match and the total runs scored or the number of wickets taken?
df['start_date'] = pd.to_datetime(df['start_date'])
runs_per_date = df.groupby('start_date')['run'].sum()
wickets_per_date = df.groupby('start_date')['player_dismissed'].count()

# Line plot for total runs scored and number of wickets taken per match date
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(runs_per_date.index, runs_per_date, 'g-')
ax2.plot(wickets_per_date.index, wickets_per_date, 'b-')
ax1.set_xlabel('Match Date')
ax1.set_ylabel('Total Runs Scored', color='g')
ax2.set_ylabel('Number of Wickets Taken', color='b')
plt.title('Total Runs Scored vs Number of Wickets Taken per Match Date')
plt.show()


# In[ ]:




