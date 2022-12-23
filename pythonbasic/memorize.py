import random
import os
clear =lambda: os.system('cls')

eng = ["dog", "cat", "mouse", "bat", "hen", "day", "puppy", "way", "moon", "snack"]
kor = ["개", "고양이", "쥐", "박쥐", "암탉", "하루", "강아지", "길", "달", "뱀"] 

select = 0
answer = 0
mode = 0

while True:
    clear() 
    print("*" * 24)
    print("OMS 깜지봇 III")
    print("*" * 24)
    print(f"수록 영단어 갯수 : {len(eng)}")
    print("*" * 24)
    mode = input("원하는 작업 선택: 단어시험 / 단어입력 / 종료 =>")
    print("*" * 24)

    if mode == "단어시험":
        while len(kor) != 0:
            clear()
            select = random.randint(0, len(eng) - 1)
            answer = input(f"{kor[select]} - 이 단어를 영어로 하면? : ")
            if answer == eng[select]:
                print(f"정답입니다! {kor[select]} = {eng[select]} 이죠! 코딩쌤보다 코딩쌤하시세요!")
                eng.pop(select)
                kor.pop(select)
            else:
                print("틀렸어요. 님 코딩쌤임?")
        print("10개의 준비된 단어를 다 맞추셨습니다.")

    elif mode == "종료":
         print("영어 빵점을 기원합니다! 안녕히 가세요!")
         break

    elif mode == "단어입력":
        while True:
            eng.append(input("영어단어를 입력하세요 : "))
            kor.append(input("한글단어를 입력하세요 : "))
            if input("입력을 더 하시겠습니까? (예/아니오)"):
                print("단어입력을 마쳤습니다.")
                break  