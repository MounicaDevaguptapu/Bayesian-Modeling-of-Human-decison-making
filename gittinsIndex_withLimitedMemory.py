# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:12:12 2018

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

def selectbanditWithLimitedMemory():
    global discountedReward,discountedFactor
    for i in range(totalBandit):
        discountedReward = 0
        discountedFactor = 0
        if numOfSelects[i] >= memoryLimitation:
            number = memoryLimitation
        else:
            number = numOfSelects[i]
        for j in range(number):
            discountedReward = discountedReward + ((discountFactor ** j) * individualReward[i][numOfSelects[i]-j])
            discountedFactor = discountedFactor + (discountFactor ** j)
        gittinIndex[i] = (discountedReward/discountedFactor)
    return max(gittinIndex,key=gittinIndex.get)
    
def playGameWithLimitedMemory():
    #re initializing because previous values must be cleared

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
            banditSelected = selectbanditWithLimitedMemory()
            numOfSelects[banditSelected] = numOfSelects[banditSelected] + 1
            pointsRewarded = generateReward(banditSelected)
            individualTotalReward[banditSelected]= individualTotalReward[banditSelected] + pointsRewarded
            individualReward[banditSelected][numOfSelects[banditSelected]-1] = pointsRewarded
            
#Main loop
playGameWithLimitedMemory()
saveScore('rewards_gittinsIndex_withLimitedmemory.csv')