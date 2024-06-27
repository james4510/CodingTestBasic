print("===짝수홀수 판별 프로그램===")
숫자 = int(input("정수를 입력하세요: "))
print("정수 ", 숫자, "를 입력했군요")
if 숫자>0:
    숫자 = 숫자 % 2
    
    if 숫자 == 0:
        print("짝수")
    else:
        print("홀수")

else:
    print("오류")
print("프로그램 종료")
