import pgzrun

WIDTH = 1590	
HEIGHT = 830
def draw():
    screen.fill('pink');
    screen.draw.text("Hello World",topleft = (795,10),fontsize=30)
   # screen.draw.rect(rect,(80,280),(150,100))
    screen.draw.line((40,20),(600,460),(255,0,0))
    screen.draw.filled_circle((450,180),80,'red')
    screen.draw.filled_rect( Rect((200,180),(150,80)),'magenta')

pgzrun.go()
