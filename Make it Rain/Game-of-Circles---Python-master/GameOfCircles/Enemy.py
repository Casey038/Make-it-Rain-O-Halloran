mark = 0
wait = 1000
go = True

import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
class Enemy(Sprite):
    
    speed = 8
    diameter = 50
    c = color(0,0,255)
    
    #def __init__(self, x, y, team):
        #self.x = x
        #self.y = y
        #self.team = team
        
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    #def display(self):
        #fill(self.c)
        #ellipse(self.x, self.y, self.diameter, self.diameter)
        
    #def animate(self):
        #self.move()
        #self.display()
        
    def aim(self, target) :
        global go, mark, wait
        #solve unit vector problem too
        xdist = target.x - self.x
        ydist = target.y - self.y
        d = (((xdist)**2 + (ydist)**2))**.5
        xVec = xdist/2 * .1
        yVec = ydist/2 * .1
        return PVector(xVec, yVec)
        return PVector(0, 10)

        
                   
    def fire(self, vector):
        global go, mark, wait
        
        if(millis() - mark > wait):
            go = not go
            mark = millis()
        if(go):
            go = False
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
    
