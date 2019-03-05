from Sprite import Sprite
class JiggleBot(Sprite):
    
    xspeed = 5
    yspeed = 12
    diameter = 75
    c = color(100,255,255)
    
    def move(self):
        self.y += random(-self.yspeed, self.yspeed)
        self.x += random(-self.xspeed, self.xspeed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
    
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
