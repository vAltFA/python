class Computer:
    def touchpad(self):
        if self.enter == '0':
            self.enter = '1'

mtouchpad = Computer()
mtouchpad.size = '2x2'
mtouchpad.buttons = '2 buttons'
mtouchpad.enter = '0'

print('I created a touchpad')
print('My touchpad size is', mtouchpad.size)
print('My touchpad have buttons', mtouchpad.buttons)
print('My touchpad button is', mtouchpad.enter)

mtouchpad.touchpad()
print('My touchpad button here is', mtouchpad.enter)
