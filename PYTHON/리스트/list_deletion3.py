print("===== 공인중계사 합격 여부 판별 프로그램 =====")
scores = [55, 35, 40, 70, 65, 30]

total = 0
underSubject = 0
average = 0

for score in scores:
    if score < 40:
        underSubject += 1
    total += score

print('40점 미만 과목 수: ', underSubject)
average = total / len(scores)
print('평균 점수 : ', average)

# 합격 여부
if underSubject > 0 or average < 60:
    print('아쉽습니다. 불합격입니다.')
else:
    print('축하합니다. 합격입니다.')