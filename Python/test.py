from Rass import *

while True:
        print("enter command")
        key = input()
        if key == 'w':
                forwards()
        elif key == 'x':
                stop()
        elif key == 's':
                backwards()
        elif key == 'd':
                right()
        elif key == 'a':
                left()
        elif key == 'z':
                break
        else:
                print("Wrong command! Try again.")

