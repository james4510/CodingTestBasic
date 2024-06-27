print("===== 장학금 판별 프로그램 =====")
점수 = int(input("점수를 입력해주세요: "))

if 점수>=90:
    print("A학점입니다.")
    print("축하합니다. 장학금 대상자입니다.")
elif 점수<90 and 점수>=80:
    print("B학점입니다.")
elif 점수<80 and 점수>=70:
    print("C학점입니다.")
elif 점수<70 and 점수>=60:
    print("D학점입니다.")
else:
    print("F학점입니다.")

print("프로그램 종료")