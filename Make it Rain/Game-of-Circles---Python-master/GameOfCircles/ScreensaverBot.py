from Sprite import Sprite
class ScreensaverBot(Sprite):
    
    xspeed = 10
    yspeed = 7
    diameter = 45
    c = color(0,100,255)
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
    
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
