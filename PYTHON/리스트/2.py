balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
ball = ['야구공, 축구공, 탁구공, 골프공, 농구공']

print(len(balls))
print(len(ball))
print(len(['Hello World']))

for item in balls:  # balls 의 length 만큼 반복, balls의 아이템이 한 개씩  변수 item에 들어감
    print('item: ', item)

for n in range (5, 51, 5): # 초기값, 종료시점, 증감값
    print("Count: %d"%n)