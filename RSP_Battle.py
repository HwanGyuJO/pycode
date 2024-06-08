import random

def get_user_choice():
    user_input = input("가위, 바위, 보 중 하나를 입력하세요!: ")
    return user_input

def get_computer_choice():
    choices = ["가위", "바위", "보"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        return "사용자 승리"
    else:
        return "사용자 패배"

user_choice = get_user_choice()
computer_choice = get_computer_choice()

print(f"사용자 선택: {user_choice}")
print(f"컴퓨터 선택: {computer_choice}")

result = determine_winner(user_choice, computer_choice)
print(f"결과: {result}")
