# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:21:02 2018

@author: md2rt
"""

import numpy as np
import pandas as pd

#initialization
totalBandit = 4
totalSelects = 1000
defaultReward = 0
defaultIndex = 0
discountFactor = 0.36
discountedReward = 0
discountedFactor = 0

numOfSelects = dict.fromkeys([0,1,2,3],defaultReward)
individualTotalReward = dict.fromkeys([0,1,2,3],defaultReward)
individualReward = [ [defaultReward] * totalSelects for i in range(totalBandit) ]
gittinIndex = dict.fromkeys([0,1,2,3],defaultIndex)
memoryLimitation = 10

probRewardBandit1 = [0.36,0.64]
probRewardBandit2 = [0.58,0.42]
probRewardBandit3 = [0.87,0.13]
probRewardBandit4 = [0.26,0.74]
possibleRewards = [0,1]

def saveScore(file_name):
    dataFrame = pd.DataFrame(data={'Episodes':[totalSelects],'Score':[int(sum(individualTotalReward.values()))]})
    print(dataFrame)
    dataFrame.to_csv(file_name,mode="a",header=False,index=False)

def generateReward(banditSelected):
    if banditSelected == 0:
        reward = np.random.choice(possibleRewards,1,p=probRewardBandit1)
    elif banditSelected == 1:
        reward = np.random.choice(possibleRewards,1,p=probRewardBandit2)
    elif banditSelected == 2:
        reward = np.random.choice(possibleRewards,1,p=probRewardBandit2)
    elif banditSelected == 3:
        reward = np.random.choice(possibleRewards,1,p=probRewardBandit3)
    
    return int(reward)
    

def selectBandit():
    global discountedReward,discountedFactor
    for i in range(totalBandit):
        discountedReward = 0
        discountedFactor = 0
        for j in range(numOfSelects[i]):
            discountedReward = discountedReward + ((discountFactor ** j) * individualReward[i][j])
            discountedFactor = discountedFactor + (discountFactor ** j)
        gittinIndex[i] = (discountedReward/discountedFactor)
    return max(gittinIndex,key=gittinIndex.get)

    
def playGame():
    for i in range(totalBandit):
        banditSelected = i
        numOfSelects[banditSelected] = numOfSelects[banditSelected] + 1
        pointsRewarded = generateReward(banditSelected)
        individualTotalReward[banditSelected]= individualTotalReward[banditSelected] + pointsRewarded
        individualReward[int(banditSelected)][numOfSelects[banditSelected]-1] = pointsRewarded
       
    stopGame = False
    while not stopGame: 
        if totalSelects - sum(numOfSelects.values()) == 0:
            stopGame = True
        else:
            banditSelected = selectBandit()
            numOfSelects[banditSelected] = numOfSelects[banditSelected] + 1
            pointsRewarded = generateReward(banditSelected)
            individualTotalReward[banditSelected]= individualTotalReward[banditSelected] + pointsRewarded
            individualReward[banditSelected][numOfSelects[banditSelected]-1] = pointsRewarded

            
#Main loop
playGame()
saveScore('rewards_gittinIndex.csv')
