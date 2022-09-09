# random 모듈을 불러온다.
import  random
# 1~100사이의 랜덤한 숫자를 생성
random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        my_number = int(input("1~100까지의 정수를 입력하세요"))

        if my_number > random_number:
            print("DOWN")
        elif my_number < random_number:
            print("UP")
        elif my_number == random_number:
            print(f"축하합니다. {game_count}회 만에 맞췄습니다!! ")
            break

        game_count = game_count + 1
    except:
        print("Error!")
