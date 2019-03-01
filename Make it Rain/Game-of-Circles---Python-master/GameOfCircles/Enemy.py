import SpriteManager
from Bullet import Bullet
class Enemy:

    
    speed = 8
    diameter = 50
    c = color(0,0,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
        
    def aim(self, target) :
        #solve unit vector problem too
        xdist = self.x - target.x
        ydist = self.y - target.y
        d = ((xdist)**2 + (ydist)**2)**.5
        xVec = xdist/d
        yVec = ydist/d
        return PVector(xVec, yVec)
        return PVector(0, 10)
        
        
                   
    def fire(self, vector):
        SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
