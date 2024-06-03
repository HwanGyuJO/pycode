import random

random_number = random.randint(1, 100)

while True:
    while True:
        try:
            user_input = int(input("1에서 100 사이의 숫자를 입력하세요: "))
            break
        except ValueError:
            print("유효한 숫자를 입력하세요.")


