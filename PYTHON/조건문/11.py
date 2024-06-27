print("===== BMI 지수 계산 프로그램 =====")
몸무게 = float(input("몸무게 (kg): "))
신장 = float(input("신장 (cm): "))
신장 = 신장 / 100

BMI = 몸무게 / 신장 ** 2

if BMI < 20:
    print("저체중입니다.")
elif BMI > 20 and BMI < 25:
    print("정상입니다.")
elif BMI > 25 and BMI < 30:
    print("과체중입니다. (1도 비만)")
elif BMI > 30 and BMI <= 40:
    print("비만입니다. (2도 비만)")
elif BMI > 40:
    print("고도비만입니다. (3도 비만)")
print("프로그램 종료")