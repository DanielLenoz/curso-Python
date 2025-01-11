y = 5

def modify_x():
    print(y)
    x = 10 + y
    print(f"Inside modify_x: x = {x}")

modify_x()

print(y)