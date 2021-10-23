sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Food, function (sprite, otherSprite) {
    if (sprite.x > otherSprite.x + 5 || sprite.x < otherSprite.x - 5) {
        sprite.vx = invert(sprite.vx)
    } else {
        sprite.vy = invert(sprite.vy)
    }
    sprite.setVelocity(plusN(sprite.vx, 1), plusN(sprite.vy, 1))
    otherSprite.destroy()
    if (sprites.allOfKind(SpriteKind.Food).length > 0) {
        info.changeScoreBy(1)
        if (Math.percentChance(5)) {
            let mySprite: Sprite = null
            projectile = sprites.createProjectileFromSprite(BonusList[randint(0, 10)], mySprite, 50, 50)
        }
    } else {
        game.over(true)
    }
})
function invert (num: number) {
    return 0 - num
}
function plusN (num: number, num2: number) {
    if (num >= 0) {
        return num + num2
    } else {
        return num - num2
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    timer.throttle("action", 500, function () {
        otherSprite.vy = invert(otherSprite.vy)
        otherSprite.vx += otherSprite.x - sprite.x
        otherSprite.vx = plusN(otherSprite.vx, 5)
    })
})
let projectile: Sprite = null
let Brick: Sprite = null
let BonusList: Image[] = []
let BrickList = [
img`
    5 5 5 5 5 5 5 5 5 2 
    5 4 4 4 4 4 4 4 4 2 
    5 4 4 4 4 4 4 4 4 2 
    5 4 4 4 4 4 4 4 4 2 
    5 4 4 4 4 4 4 4 4 2 
    5 4 4 4 4 4 4 4 4 2 
    2 2 2 2 2 2 2 2 2 2 
    `,
img`
    b b b b b b b b b c 
    b a a a a a a a a c 
    b a a a a a a a a c 
    b a a a a a a a a c 
    b a a a a a a a a c 
    b a a a a a a a a c 
    c c c c c c c c c c 
    `,
img`
    d d d d d d d d d 6 
    d 7 7 7 7 7 7 7 7 6 
    d 7 7 7 7 7 7 7 7 6 
    d 7 7 7 7 7 7 7 7 6 
    d 7 7 7 7 7 7 7 7 6 
    d 7 7 7 7 7 7 7 7 6 
    6 6 6 6 6 6 6 6 6 6 
    `,
img`
    d d d d d d d d d 4 
    d 5 5 5 5 5 5 5 5 4 
    d 5 5 5 5 5 5 5 5 4 
    d 5 5 5 5 5 5 5 5 4 
    d 5 5 5 5 5 5 5 5 4 
    d 5 5 5 5 5 5 5 5 4 
    4 4 4 4 4 4 4 4 4 4 
    `
]
BonusList = [img`
    . . 2 2 2 2 . . 
    . . 2 2 2 2 . . 
    2 2 2 2 2 2 2 2 
    2 2 2 2 2 2 2 2 
    2 2 2 2 2 2 2 2 
    2 2 2 2 2 2 2 2 
    . . 2 2 2 2 . . 
    . . 2 2 2 2 . . 
    `, img`
    . . . . . 5 5 2 
    . . . . 5 . . . 
    . . . 5 . . . . 
    . b b b b b b . 
    b b f b f b b b 
    b b b b b b b b 
    b b f f f b b b 
    . b b b b b b . 
    `, img`
    . 1 1 1 . . 
    1 1 d d d . 
    1 d d d d . 
    d d d d b . 
    . d b b . . 
    . . . . . . 
    `]
let Ball = sprites.create(img`
    . 1 1 1 . 
    1 1 d d d 
    1 d d d d 
    d d d d b 
    . d b b . 
    `, SpriteKind.Enemy)
let Player = sprites.create(img`
    . . . . . . . . . . . . . . . . . . . . . . . . . 
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 6 
    9 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 8 
    9 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 8 
    6 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
    `, SpriteKind.Player)
Player.setPosition(80, 110)
Player.setStayInScreen(true)
controller.moveSprite(Player, 100, 0)
Ball.setPosition(80, 103)
Ball.setBounceOnWall(true)
for (let Y = 0; Y <= 4; Y++) {
    for (let X = 0; X <= 13; X++) {
        Brick = sprites.create(BrickList[randint(0, BrickList.length - 1)], SpriteKind.Food)
        Brick.setPosition(8 + X * 11, 5 + Y * 8)
    }
}
game.splash("START!")
Ball.setVelocity(randint(-45, 45), -30)
