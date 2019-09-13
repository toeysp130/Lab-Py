import pgzrun
import time

WIDTH = 800
HEIGHT = 600

alien = Actor("alien")


def draw():
    screen.fill("red")
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos,button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        set_alien_hurt()
        
    else :
        print("you missed")

def set_alien_hurt():
    print("EEK")
    sounds.eep.play()
    alien.image = "alien_hurt"
    clock.schedule( set_alien_normal, 0.1)

def set_alien_normal():
    alien.image = "alien"
    
        

pgzrun.go()        
