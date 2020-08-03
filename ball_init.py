class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'

    def __str__(self):
        msg = 'Hi, I\'m a ' + self.size + ' ' + self.color + ' ball!'
        return msg

my_ball = Ball('blue', 'small', 'left')
cartersBall = Ball('red', 'small', 'down')
print(my_ball)
print('I created a ball')
print('My ball color is', my_ball.color)
print('My ball size is', my_ball.size)
print('My ball direction is', my_ball.direction)
print('carter ball', cartersBall.color, cartersBall.size, cartersgBall.direction)
