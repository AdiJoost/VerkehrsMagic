import numpy as np
from random import randint

class Street():

    EMPTY_CELL = -1

    def __init__(self, gridsize=500, dally=0.2, spawnRate=0.2, tunnel=None, maxSpeed=5):
        self.gridsize = gridsize
        self.dally = dally
        self.spawnRate = spawnRate
        self.tunnel = tunnel
        self.maxSpeed = maxSpeed
        self.respawn()


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
            if (dist < targetSpeed) and self.oldGridLeft[i] == Street.EMPTY_CELL:
                self.changeToLeft(i)
            else:
                newSpeed = min(dist, targetSpeed)
                self.newGridRight[(i + newSpeed) % self.gridsize] = newSpeed
        
    def changeToLeft(self, pos):
        self.oldGridLeft[pos] = self.oldGridRight[pos]

    def updateLeft(self):
        for i in range(self.gridsize):
            if self.oldGridLeft[i] == Street.EMPTY_CELL:
                continue
            dist = self.calcEmptyFieldsLeft(i)
            targetSpeed = min(self.maxSpeed, self.oldGridLeft[i] + 1)
            newSpeed = min(dist, targetSpeed)
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