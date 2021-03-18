a,b,c = map(int,input().split()) #map 으로 문자열을 한번에 int로 변환
num = []
num.append(a)
num.append(b)
num.append(c)
for i in num :
    if i%2 == 0:
        print("even")
    else:
        print("odd")
