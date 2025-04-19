from pygame import*

#parentclass for sprites
class GameSprite(sprite.Sprite):
    #class construcktor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #every sprite must store the image property 
        self.image = transform.scale(image.load(player_image), (65, 55))
        self.speed = player_speed
        #every sprite musthave the rect property - the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x> 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x< 695:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y< 695:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1 
        self.color_2 = color_2 
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN!", True, (255, 215,0))
lose = font.render("YOU lOSE!", True, (180, 0, 0))

clock = time.Clock()
FPS = 60

#adegan permainan
win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Game Characters
packman = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png',win_width - 80, 280, 2)
wall_1 = Wall(192,192,192, 50, 10, 20, 410)
wall_2 = Wall(192, 192, 192, 120, 50, 200,20)
wall_3 = Wall(192, 192, 192, 320, 50, 20,300)
wall_4 = Wall(192, 192, 192, 200, 420, 240,20)
wall_5 = Wall(192, 192, 192, 150, 150, 20,350)
wall_6 = Wall(192, 192, 192, 235, 150, 20,200)
wall_7 = Wall(192, 192, 192, 150, 200, 20,100)
wall_8 = Wall(192, 192, 192, 250, 250, 80,20)
wall_9 = Wall(192, 192, 192, 400, 50, 20,350)
wall_10 = Wall(192, 192, 192, 500, 100, 200,20)
wall_11 = Wall(192, 192, 192, 450, 250, 20,150)
              
final= GameSprite('trophy.png', win_width - 120, win_height - 80 , 0)

game = True

#musik
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
money = mixer.Sound('money.ogg')
kick= mixer.Sound('kick.ogg')

finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if sprite.collide_rect(packman, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()
        if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, wall_1) or sprite.collide_rect(packman, wall_2)or sprite.collide_rect(packman, wall_3)or sprite.collide_rect(packman, wall_4)or sprite.collide_rect(packman, wall_5)or sprite.collide_rect(packman, wall_6)or sprite.collide_rect(packman, wall_7)or sprite.collide_rect(packman, wall_8)or sprite.collide_rect(packman, wall_9)or sprite.collide_rect(packman, wall_10)or sprite.collide_rect(packman, wall_11):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
        window.blit(background, (0, 0))
        packman.update()
        packman.reset()
        monster.update()
        monster.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        wall_9.draw_wall()
        wall_10.draw_wall()
        wall_11.draw_wall()
        final.reset()
    display.update()
    clock.tick(FPS)