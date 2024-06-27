import sys

print("===== 조건문 예제 1 =====")
n = int(input("양의 정수를 입력해주세요: "))

if n<=0:
    print("잘못된 입력입니다.")
    sys.exit()  # 프로그램 종료 코드

if n % 3 == 0:
    print("3의 배수입니다.")
else:
    print("3의 배수가 아닙니다.")
print("프로그램 종료")