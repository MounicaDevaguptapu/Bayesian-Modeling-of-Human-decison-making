# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:58:11 2018

@author: md2rt
"""

import pandas as pd
import numpy as np

#initialization
totalBandit = 4
totalSelects = 25
defaultReward = 0
defaultIndex = 0
discountFactor =0.36
discountedReward = 0
discountedFactor = 0
standardReward = 1

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
  
def calcGittinsIndex(bandit):
  discountedReward = 0
  discountedFactor = 0
  for j in range(totalSelects):
    discountedReward = discountedReward + ((discountFactor ** j) * individualReward[bandit][j])
    discountedFactor = discountedFactor + (discountFactor ** j)
  ratio = (discountedReward/discountedFactor)
  return ratio

def calculateGittinsIndex(bandit,standardReward,alpha,beta):
    #print("Alpha,Beta:",alpha,beta)
    if ((alpha + beta) == totalSelects):
      return calcGittinsIndex(bandit)
    else:
        first_part = standardReward / ( 1 - discountFactor )
        second_part = ((alpha * ( 1 + (discountFactor * calculateGittinsIndex(bandit,standardReward,alpha+1,beta)))) + beta * discountFactor * calculateGittinsIndex(bandit,standardReward,alpha,beta+1)) / (alpha + beta)
    if first_part > second_part:
        return first_part
    elif second_part > first_part:
        return second_part
    else:
        return standardReward
    
def selectBandit():
    for i in range(totalBandit):
        gittinIndex[i] = calculateGittinsIndex(i,standardReward,individualTotalReward[i],numOfSelects[i]-individualTotalReward[i])
    return max(gittinIndex,key=gittinIndex.get)
  
def playGame():
    for i in range(totalBandit):
        banditSelected = i
        #print("Bandit Selected",i)
        numOfSelects[banditSelected] = numOfSelects[banditSelected] + 1
        pointsRewarded = generateReward(banditSelected)
        #print("Points Awarded",pointsRewarded)
        individualTotalReward[banditSelected]= individualTotalReward[banditSelected] + pointsRewarded
        individualReward[int(banditSelected)][numOfSelects[banditSelected]-1] = pointsRewarded
        
    stopGame = False
    while not stopGame:
        if totalSelects - sum(numOfSelects.values()) == 0:
            stopGame = True
        else:
            banditSelected = selectBandit()
            #print("Bandit Selected",banditSelected)
            numOfSelects[banditSelected] = numOfSelects[banditSelected] + 1
            pointsRewarded = generateReward(banditSelected)
            #print("Points Awarded",pointsRewarded)
            individualTotalReward[banditSelected]= individualTotalReward[banditSelected] + pointsRewarded
            individualReward[banditSelected][numOfSelects[banditSelected]-1] = pointsRewarded


playGame()
saveScore('rewards_bernoulli.csv')
