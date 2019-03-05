import platform
from Bullet import Bullet
from Enemy import Enemy
from Raindrop import Raindrop
from Player import Player
from ScreensaverBot import ScreensaverBot
from JiggleBot import JiggleBot
#from Lobber import Lobber
import SpriteManager

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
    
                           
def draw():
    background(255)
    SpriteManager.animate()
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
