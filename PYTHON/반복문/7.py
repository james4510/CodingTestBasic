import sys
print("===== 구구단 출력 프로그램 =====")

n = int(input("몇단? : "))

if n<10 or n>1:
    print("구구단 %d단을 출력합니다."%n)
    for t in range(1, 10, 1):
        print("%d * %d = %d"%(n, t, n*t))
else:
    print("잘못된 입력입니다.")
    sys.exit()
print("프로그램 종료")