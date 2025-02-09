import random

def main():

    get_level()
    score = 10

    for i in range(10):
        attempts = 0
        generate_integer(level)
        while attempts < 3:
            get_solution = int(input(f'{x} + {y} = '))
            if get_solution == (x+y):
                break
            else:
                print('EEE')
                attempts += 1
        if attempts == 3:
            score -= 1
            print(f'{x} + {y} = {x+y}')

    print('Score:',score)


def get_level():
    while True:
        try:
            global level
            level = int(input('Level: '))
            if level in [1,2,3]:
                return True
        except ValueError:
            pass



def generate_integer(level):
    global x,y

    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)

    if level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    if level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)

if __name__ == "__main__":
    main()
