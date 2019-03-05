import SpriteManager
class Bullet:

    
    diameter = 15
    c = color(0)
    
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        if (self.x < 0 - self.diameter or self.x > width + self.diameter or self.y < 0 - self.diameter or self.y > height + self.diameter):
            SpriteManager.destroy(self)
        
    #def destroy(self):
        #if self.x > width
        #if self.x < width
        #if self.y > height
        #if self.y< height
        #destroyed.append(self)
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
    
    
