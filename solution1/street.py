import numpy as np
from random import randint
from pseudocode import showMagic, saveMagic

class Street():

    EMPTY_CELL = -1

    def __init__(self, gridsize=500, dally=0.2, spawnRate=0.2, tunnel=None, maxSpeed=5, tunnelSpeedLimit=3, doubleSpawn=False, doubleDally=False):
        self.gridsize = gridsize
        self.dally = dally
        self.spawnRate = spawnRate
        self.tunnel = tunnel
        self.tunnelSpeedLimit = tunnelSpeedLimit
        self.maxSpeed = maxSpeed
        self.doubleSpawn = doubleSpawn
        self.doubleDally = doubleDally
        self.respawn()

    def run(self, itterations, plotName=None):
        trafficLeft = np.zeros((itterations, self.gridsize), dtype=np.int32)
        trafficRight = np.zeros((itterations, self.gridsize), dtype=np.int32)
        for i in range(itterations):
            trafficLeft[i,:] = self.oldGridLeft[:]
            trafficRight[i,:] = self.oldGridRight[:]
            self.update()
        if not plotName:
            showMagic(trafficLeft, trafficRight)
        else:
            saveMagic(trafficLeft, trafficRight, self, plotName)
        
    def runRight(self, itterations, plotName=None):
        #dont use this
        trafficRight = np.zeros((itterations, self.gridsize), dtype=np.int32)
        trafficLeft = np.zeros((itterations, self.gridsize), dtype=np.int32)
        for i in range(itterations):
            trafficRight[i,:] = self.oldGridRight[:]
            self.update()
        if not plotName:
            showMagic(trafficLeft, trafficRight)
        else:
            saveMagic(trafficLeft, trafficRight, self, plotName)

    def calcEmptyFieldsRight(self, pos):
        for i in range(1, self.maxSpeed + 1):
            if self.oldGridRight[(pos + i)%self.gridsize] != Street.EMPTY_CELL:
                return i - 1
        return self.maxSpeed

    def calcEmptyFieldsLeft(self, pos):
        for i in range(1, self.maxSpeed + 1):
            if self.oldGridLeft[(pos + i)%self.gridsize] != Street.EMPTY_CELL:
                return i - 1
        return self.maxSpeed

    def update(self):
        self.updateRight()
        self.updateLeft()
        self.oldGridRight = self.newGridRight.copy()
        self.oldGridLeft = self.newGridLeft.copy()
        self.newGridRight = self.getEmptyGrid()
        self.newGridLeft = self.getEmptyGrid()

    def updateRight(self):
        for i in range(self.gridsize):
            if self.oldGridRight[i] == Street.EMPTY_CELL:
                continue
            dist = self.calcEmptyFieldsRight(i)
            targetSpeed = min(self.maxSpeed, self.oldGridRight[i] + 1)
            if self.tunnel:
                if self.tunnel[0] <= i <= self.tunnel[1]:
                    targetSpeed = min(targetSpeed, self.tunnelSpeedLimit)
            if (dist < targetSpeed) and self.oldGridLeft[i] == Street.EMPTY_CELL:
                self.changeToLeft(i)
            else:
                newSpeed = min(dist, targetSpeed)
                if (randint(1,100) <= self.dally * 100):
                    newSpeed = max(newSpeed - 1, 0)
                self.newGridRight[(i + newSpeed) % self.gridsize] = newSpeed
        
    def changeToLeft(self, pos):
        self.oldGridLeft[pos] = self.oldGridRight[pos]
    
    def checkLaneChange(self, pos, targetSpeed):
        for i in range(0, targetSpeed + 1):
            if self.newGridRight[(i + pos) % self.gridsize] != Street.EMPTY_CELL:
                return False
            if self.oldGridRight[(i + pos) % self.gridsize] != Street.EMPTY_CELL:
                return False
        return True

    def changeToRight(self, pos, newSpeed):
        self.newGridRight[(pos + newSpeed)% self.gridsize] = newSpeed

    def updateLeft(self):
        for i in range(self.gridsize):
            if self.oldGridLeft[i] == Street.EMPTY_CELL:
                continue
            dist = self.calcEmptyFieldsLeft(i)
            targetSpeed = min(self.maxSpeed, self.oldGridLeft[i] + 1)
            if self.doubleDally:
                if (randint(1,100) <= self.dally * 100):
                    targetSpeed = max(targetSpeed - 1, 0)
            newSpeed = min(dist, targetSpeed)
            if self.tunnel:
                if self.tunnel[0] <= i <= self.tunnel[1]:
                    newSpeed = min(newSpeed, self.tunnelSpeedLimit)
            if self.checkLaneChange(i, newSpeed):
                self.changeToRight(i, newSpeed)
            else:
                self.newGridLeft[(i + newSpeed) % self.gridsize] = newSpeed

    def getEmptyGrid(self):
        return np.full((self.gridsize), Street.EMPTY_CELL, dtype=np.int32)
    
    def respawn(self):
        self.oldGridLeft = self.getEmptyGrid()
        self.oldGridRight = self.getEmptyGrid()
        self.newGridLeft = self.getEmptyGrid()
        self.newGridRight = self.getEmptyGrid()
        self.spawn()
    
    def spawn(self):
        for i in range(self.gridsize):
            if randint(1,100) <= self.spawnRate * 100:
                self.oldGridRight[i] = randint(0, self.maxSpeed)
        if self.doubleSpawn:
            for i in range(self.gridsize):
                if randint(1,100) <= self.spawnRate * 100:
                    self.oldGridRight[i] = randint(0, self.maxSpeed)

    def to_string(self):
        returnValue = ""
        for i in range(self.gridsize):
            if self.oldGridLeft[i] == Street.EMPTY_CELL:
                returnValue += "-"
            else:
                returnValue += str(self.oldGridLeft[i])
        returnValue +="\n"
        for i in range(self.gridsize):
            if self.oldGridRight[i] == Street.EMPTY_CELL:
                returnValue += "-"
            else:
                returnValue += str(self.oldGridRight[i])
        return returnValue