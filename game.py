# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:44:43 2018

@author: md2rt
"""

import pygame
import numpy as np
import time
import pandas as pd

pygame.init() #initialize the python game

#Initialization of Global variables
displayWidth = 1000
displayHeight = 600 #Game Screen Dimensions

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (34,139,34)
blue = (42,11,245)

click = 0 #to know the position of user click
totalReward = 0 #total score of the user
totalSelects = 10 #number of chances user is given
defaultReward = 0
individualReward = dict.fromkeys(['1','2','3','4'],defaultReward) #Hash to store individual rewards from arms
numOfSelects = dict.fromkeys(['1','2','3','4'],defaultReward)
probRewardBandit1 = [0.36,0.64]
probRewardBandit2 = [0.58,0.42]
probRewardBandit3 = [0.87,0.13]
probRewardBandit4 = [0.26,0.74]
possibleRewards = [0,1]

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight)) #setting up game window
pygame.display.set_caption("CLICK AND EARN")
clock = pygame.time.Clock()
slotMach1 = pygame.image.load('slotmach1.png')
slotMach2 = pygame.image.load('slotmach1.png')
slotMach3 = pygame.image.load('slotmach1.png')
slotMach4 = pygame.image.load('slotmach1.png')

#Add the slot machine to display at particular location(x,y)
def slotMach(img,x,y):
    gameDisplay.blit(img,(x,y))
    
#funciton to generate points
def generatePoints(banditPicked):
    global totalReward,numOfSelects,individualReward,totalEpisodes
    if banditPicked == 1:
        individualReward['1'] = individualReward['1'] + np.random.choice(possibleRewards,1,p=probRewardBandit1)
        numOfSelects['1'] = numOfSelects['1'] + 1
    elif  banditPicked == 2:
        individualReward['2'] = individualReward['2'] + np.random.choice(possibleRewards,1,p=probRewardBandit2)
        numOfSelects['2'] = numOfSelects['2'] + 1
    elif banditPicked == 3:
        individualReward['3'] = individualReward['3'] + np.random.choice(possibleRewards,1,p=probRewardBandit3)
        numOfSelects['3'] = numOfSelects['3'] + 1
    else:
        individualReward['4'] = individualReward['4'] + np.random.choice(possibleRewards,1,p=probRewardBandit4)
        numOfSelects['4'] = numOfSelects['4'] + 1
    totalReward = sum(individualReward.values())
    totalEpisodes = sum(numOfSelects.values())
    #print(totalReward,totalEpisodes,individualReward['1'],numOfSelects['1'],individualReward['2'],numOfSelects['2'],individualReward['3'],numOfSelects['3'],individualReward['4'],numOfSelects['4'])
    
    
  
def displayScoreBandit1():
    font = pygame.font.SysFont("monospace",15)
    #Bandit 1
    pygame.draw.rect(gameDisplay,white,(10,315,170,50),0)
    ScoreBandit1 = font.render("Score:"+str(individualReward['1']),1,black)
    gameDisplay.blit(ScoreBandit1,(10,320))
    SelectsBandit1 = font.render("Selected:"+str(numOfSelects['1']),1,black)
    gameDisplay.blit(SelectsBandit1,(10,335))
    avgBandit1 = font.render("Average:"+str(np.round_(individualReward['1']/numOfSelects['1'],2)),1,black)
    gameDisplay.blit(avgBandit1,(10,350))
    pygame.display.update()
    
def displayScoreBandit2():
    #Bandit 2
    font = pygame.font.SysFont("monospace",15)
    pygame.draw.rect(gameDisplay,white,(251,315,170,50),0)
    ScoreBandit2 = font.render("Score:"+str(individualReward['2']),1,black)
    gameDisplay.blit(ScoreBandit2,(251,320))
    SelectsBandit2 = font.render("Selected:"+str(numOfSelects['2']),1,black)
    gameDisplay.blit(SelectsBandit2,(251,335))
    avgBandit2 = font.render("Average:"+str(np.round_(individualReward['2']/numOfSelects['2'],2)),1,black)
    gameDisplay.blit(avgBandit2,(251,350))
    pygame.display.update()

def displayScoreBandit3():    
    #Bandit 3
    font = pygame.font.SysFont("monospace",15)
    pygame.draw.rect(gameDisplay,white,(497,315,170,50),0)
    ScoreBandit3 = font.render("Score:"+str(individualReward['3']),1,black)
    gameDisplay.blit(ScoreBandit3,(497,320))
    SelectsBandit3 = font.render("Selected:"+str(numOfSelects['3']),1,black)
    gameDisplay.blit(SelectsBandit3,(497,335))
    avgBandit3 = font.render("Average:"+str(np.round_(individualReward['3']/numOfSelects['3'],2)),1,black)
    gameDisplay.blit(avgBandit3,(497,350))
    pygame.display.update()
    
def displayScoreBandit4():
    #Bandit 4
    font = pygame.font.SysFont("monospace",15)
    pygame.draw.rect(gameDisplay,white,(750,315,170,50),0)
    ScoreBandit4 = font.render("Score:"+str(individualReward['4']),1,black)
    gameDisplay.blit(ScoreBandit4,(750,320))
    SelectsBandit4 = font.render("Selected:"+str(numOfSelects['4']),1,black)
    gameDisplay.blit(SelectsBandit4,(750,335))
    avgBandit4 = font.render("Average:"+str(np.round_(individualReward['4']/numOfSelects['4'],2)),1,black)
    gameDisplay.blit(avgBandit4,(750,350))
    pygame.display.update()
    
def displayTotalScore():
    font = pygame.font.SysFont("arial",25)
    pygame.draw.rect(gameDisplay,white,(displayWidth/3,450,480,100),0)
    TotalScore = font.render("Total Score:"+str(sum(individualReward.values())),1,black)
    gameDisplay.blit(TotalScore,(displayWidth/3,450))
    TotalSelects = font.render("Total Selections:"+str(sum(numOfSelects.values())),1,black)
    gameDisplay.blit(TotalSelects,(displayWidth/3,480))
    TotalAverage = font.render("Average Score/Selection:"+str(np.round_(sum(individualReward.values())/sum(numOfSelects.values()),2)),1,black)
    gameDisplay.blit(TotalAverage,(displayWidth/3,510))
    pygame.display.update()
    
def displaySelects():
    font = pygame.font.SysFont("Serif",15)
    pygame.draw.rect(gameDisplay,white,(715,125,500,50),0)
    TotalScore = font.render("Remaining Selections:"+str(totalSelects - sum(numOfSelects.values())),1,black)
    gameDisplay.blit(TotalScore,(715,125))
    pygame.display.update()

def savescore():
    dataFrame = pd.DataFrame(data={'Episodes':[totalSelects],'Score':[int(sum(individualReward.values()))]})
    print(dataFrame)
    dataFrame.to_csv("rewards.csv",mode="a",header=False,index=False)
    
    
def startGame():
    stopGame = False #variable used to stop the game
    
    x1 = 1
    y1 = (displayHeight * 0.3)
    x2 = 243
    y2 = (displayHeight * 0.3)
    x3 = (243 * 2)
    y3 = (displayHeight * 0.3)
    x4 = ((243 * 3) + 10)
    y4 = (displayHeight * 0.3) #coordinates for slot machines position
    
    gameDisplay.fill(white)
    #title display
    font = pygame.font.SysFont("harrington",35,bold=True)
    pygame.draw.rect(gameDisplay,white,(displayWidth/3,60,425,95),0)
    gameTitle = font.render("CLICK AND EARN",1,green)
    gameDisplay.blit(gameTitle,(displayWidth/3,60))
    #instructions display
    font = pygame.font.SysFont("arial",10,italic=True)
    pygame.draw.rect(gameDisplay,white,(9,572,950,15),0)
    gameTitle = font.render("**Instrucitons: Click on any arm and get points. Every Arm generates either 0 or 1. Try to Score maximum. Number of chances left is displayed on the top right corner. Game will be stopped as soon as number of chances are completed.",1,black)
    gameDisplay.blit(gameTitle,(9,572))
    #slot machines display
    slotMach(slotMach1,x1,y1)
    slotMach(slotMach2,x2,y2)
    slotMach(slotMach3,x3,y3)
    slotMach(slotMach4,x4,y4)
    #Buttons
    buttonBandit1 = pygame.draw.circle(gameDisplay,red,(225,253),15)
    buttonBandit2 = pygame.draw.circle(gameDisplay,red,(471,251),15)
    buttonBandit3 = pygame.draw.circle(gameDisplay,red,(717,251),15)
    buttonBandit4 = pygame.draw.circle(gameDisplay,red,(965,253),15)
    pygame.display.update()
    
    while not stopGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopGame = True
            if (totalSelects - sum(numOfSelects.values())) == 0:
                gameDisplay.fill(black)
                font = pygame.font.SysFont("Serif",50)
                pygame.draw.rect(gameDisplay,black,((displayWidth/3),(displayHeight/2),250,50),0)
                TotalScore = font.render("Game Over! Score: "+str(sum(individualReward.values())),1,green)
                gameDisplay.blit(TotalScore,((displayWidth/3),(displayHeight/2)))
                pygame.display.update()
                time.sleep(1)
                stopGame = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if buttonBandit1.collidepoint(pygame.mouse.get_pos()) == 1:
                    generatePoints(1)
                    displayScoreBandit1()
                    displayTotalScore()
                    displaySelects()
                elif buttonBandit2.collidepoint(pygame.mouse.get_pos()) == 1:
                    generatePoints(2)
                    displayScoreBandit2()
                    displayTotalScore()
                    displaySelects()
                elif buttonBandit3.collidepoint(pygame.mouse.get_pos()) == 1:
                    generatePoints(3)
                    displayScoreBandit3()
                    displayTotalScore()
                    displaySelects()
                elif buttonBandit4.collidepoint(pygame.mouse.get_pos()) == 1:
                    generatePoints(4)
                    displayScoreBandit4()
                    displayTotalScore()
                    displaySelects() 

#main loop
startGame()
savescore()
pygame.quit()
