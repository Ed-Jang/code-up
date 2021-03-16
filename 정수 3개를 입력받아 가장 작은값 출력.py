a,b,c = map(int,input().split()) #map 으로 문자열을 한번에 int로 변환
num = a<b and a or b #a<b 가 참이면 a 거짓이면 b (결국 작은값이 저장)
print( num<c and num or c) #num<c 이 참이면 num 거짓이면 c (결국 작은값 출력)
