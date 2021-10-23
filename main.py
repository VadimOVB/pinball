def on_on_overlap(sprite, otherSprite):
    global projectile
    if sprite.x > otherSprite.x + 5 or sprite.x < otherSprite.x - 5:
        sprite.vx = invert(sprite.vx)
    else:
        sprite.vy = invert(sprite.vy)
    sprite.set_velocity(plusN(sprite.vx, 1), plusN(sprite.vy, 1))
    otherSprite.destroy()
    if len(sprites.all_of_kind(SpriteKind.food)) > 0:
        info.change_score_by(1)
        if Math.percent_chance(5):
            mySprite: Sprite = None
            projectile = sprites.create_projectile_from_sprite(BonusList[randint(0, 10)], mySprite, 50, 50)
    else:
        game.over(True)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.food, on_on_overlap)

def invert(num: number):
    return 0 - num
def plusN(num2: number, num22: number):
    if num2 >= 0:
        return num2 + num22
    else:
        return num2 - num22

def on_on_overlap2(sprite2, otherSprite2):
    
    def on_throttle():
        otherSprite2.vy = invert(otherSprite2.vy)
        otherSprite2.vx += otherSprite2.x - sprite2.x
        otherSprite2.vx = plusN(otherSprite2.vx, 5)
    timer.throttle("action", 500, on_throttle)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
Brick: Sprite = None
BonusList: List[Image] = []
BrickList = [img("""
        5 5 5 5 5 5 5 5 5 2 
            5 4 4 4 4 4 4 4 4 2 
            5 4 4 4 4 4 4 4 4 2 
            5 4 4 4 4 4 4 4 4 2 
            5 4 4 4 4 4 4 4 4 2 
            5 4 4 4 4 4 4 4 4 2 
            2 2 2 2 2 2 2 2 2 2
    """),
    img("""
        b b b b b b b b b c 
            b a a a a a a a a c 
            b a a a a a a a a c 
            b a a a a a a a a c 
            b a a a a a a a a c 
            b a a a a a a a a c 
            c c c c c c c c c c
    """),
    img("""
        d d d d d d d d d 6 
            d 7 7 7 7 7 7 7 7 6 
            d 7 7 7 7 7 7 7 7 6 
            d 7 7 7 7 7 7 7 7 6 
            d 7 7 7 7 7 7 7 7 6 
            d 7 7 7 7 7 7 7 7 6 
            6 6 6 6 6 6 6 6 6 6
    """),
    img("""
        d d d d d d d d d 4 
            d 5 5 5 5 5 5 5 5 4 
            d 5 5 5 5 5 5 5 5 4 
            d 5 5 5 5 5 5 5 5 4 
            d 5 5 5 5 5 5 5 5 4 
            d 5 5 5 5 5 5 5 5 4 
            4 4 4 4 4 4 4 4 4 4
    """)]
BonusList = [img("""
        . . 2 2 2 2 . . 
            . . 2 2 2 2 . . 
            2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 
            . . 2 2 2 2 . . 
            . . 2 2 2 2 . .
    """),
    img("""
        . . . . . 5 5 2 
            . . . . 5 . . . 
            . . . 5 . . . . 
            . b b b b b b . 
            b b f b f b b b 
            b b b b b b b b 
            b b f f f b b b 
            . b b b b b b .
    """),
    img("""
        . 1 1 1 . . 
            1 1 d d d . 
            1 d d d d . 
            d d d d b . 
            . d b b . . 
            . . . . . .
    """)]
Ball = sprites.create(img("""
        . 1 1 1 . 
            1 1 d d d 
            1 d d d d 
            d d d d b 
            . d b b .
    """),
    SpriteKind.enemy)
Player = sprites.create(img("""
        . . . . . . . . . . . . . . . . . . . . . . . . . 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 6 
            9 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 8 
            9 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 8 
            6 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    """),
    SpriteKind.player)
Player.set_position(80, 110)
Player.set_stay_in_screen(True)
controller.move_sprite(Player, 100, 0)
Ball.set_position(80, 103)
Ball.set_bounce_on_wall(True)
for Y in range(5):
    for X in range(14):
        Brick = sprites.create(BrickList[randint(0, len(BrickList) - 1)], SpriteKind.food)
        Brick.set_position(8 + X * 11, 5 + Y * 8)
game.splash("START!")
Ball.set_velocity(randint(-45, 45), -30)