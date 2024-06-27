weatherInfo = ['The', 'weather', 'very']

for item in weatherInfo:
    print(item, ' ', end='')
else:
    print()

weatherInfo.insert(2, 'is')
weatherInfo.append('cold')
for item in weatherInfo:
    print(item, ' ', end='')
else:
    print()