print("===== 윤년 판별 프로그램 =====")
year = int(input("년도 입력: "))

if year % 400 == 0:
    print("윤년입니당.")
elif year % 100 == 0:
    print("윤년아닙니당.")
elif year % 4 == 0:
    print("윤년입니당.")
else:
    print("윤년아닙니당.")
print("프로그램 종료")