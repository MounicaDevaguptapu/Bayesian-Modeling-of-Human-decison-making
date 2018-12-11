# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("rewards.csv")

df1 = pd.read_csv('rewards_gittinsIndex.csv')
df2 = pd.read_csv('rewards_gittinsIndex_withLimitedmemory.csv')
df3 = pd.read_csv('rewards_bernoulli.csv')
df4 = pd.read_csv('rewards_bernoulli_MemLim_LALim.csv')
dff = df.merge(df1,on='Episodes').merge(df2,on='Episodes')
#dfff = dff.merge(df3,on='Episodes')
df_final = dff.merge(df4,on='Episodes')
fig, ax = plt.subplots()
df_final.plot(x=['Episodes'],y=['Score_x','Score_y'],kind='bar',width=0.8,ax=ax)
ax.legend(['Human','Gittins Index','Gittins Index with Memory Restriction','Bernoulli Reward with Memory and Look Ahead res.'])



df_1 = df.merge(df1,on='Episodes')
df_1.plot(x=['Episodes'],y=['Score_x','Score_y'],kind='line')

df_2 = df.merge(df2,on='Episodes')
df_2.plot(x=['Episodes'],y=['Score_x','Score_y'],kind='line')

df_3 = df.merge(df3,on='Episodes')
df_3.plot(x=['Episodes'],y=['Score_x','Score_y'],kind='line')

df_4 = df.merge(df4,on='Episodes')
df_4.plot(x=['Episodes'],y=['Score_x','Score_y'],kind='line')

