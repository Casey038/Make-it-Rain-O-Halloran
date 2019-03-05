import platform
from Bullet import Bullet
from Enemy import Enemy
from Raindrop import Raindrop
from Player import Player
from SpriteManager import sprites
from ScreensaverBot import ScreensaverBot
from JiggleBot import JiggleBot
#from Lobber import Lobber
import SpriteManager
mark = 0
wait = 1000
#butt

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width, height, playerTeam)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(200, 50, enemyTeam))
    SpriteManager.spawn(Enemy(300, 100, enemyTeam))
    #sprites.append(player)
    #sprites.append(Enemy(50, 50, enemyTeam))
    #sprites.append(Enemy(150, 150, enemyTeam))
    #sprites.append(Raindrop(70, 80, enemyTeam))
    #sprites.append(Raindrop(100, 80, enemyTeam))
    #sprites.append(Raindrop(90, 80, enemyTeam))
    #sprites.append(Raindrop(110, 80, enemyTeam))
    #sprites.append(Raindrop(140, 80, enemyTeam))
    #sprites.append(Raindrop(160, 80, enemyTeam))
    #sprites.append(Raindrop(150, 80, enemyTeam))
    #sprites.append(Raindrop(130, 80, enemyTeam))
    #sprites.append(Raindrop(220, 80, enemyTeam))
    #sprites.append(Raindrop(20, 80, enemyTeam))
    #sprites.append(Raindrop(200, 80, enemyTeam))
    #sprites.append(Raindrop(20, 80, enemyTeam))
    #sprites.append(Raindrop(210, 80, enemyTeam))
    #sprites.append(Raindrop(240, 80, enemyTeam))
    #sprites.append(Raindrop(260, 80, enemyTeam))
    #sprites.append(Raindrop(250, 80, enemyTeam))
    #sprites.append(Raindrop(230, 80, enemyTeam))
    #sprites.append(Raindrop(220, 80, enemyTeam))
    #sprites.append(JiggleBot(100, 80, enemyTeam))
    #sprites.append(ScreensaverBot(200, 40, enemyTeam))
    
                           
def draw():
    global player, sprites
    background(255)
    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
