def convertUnit(lengthCm):
    print(lengthCm, 'cm = ', lengthCm*0.393701, 'inch')

length = int(input("길이를 입력하세요: "))
convertUnit(length)