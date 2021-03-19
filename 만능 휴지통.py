#입력받은 10자리 값의 10자리 1자리 순서를 바꾸고 2를 곱한다
#첫째 줄에 출력
#그 양이 50 이하이면 GOOD 초과이면 OH MY GOD
#둘때 줄에 출력

a = int(input()) #1<=a<=99
ten = a//10 #십의 자리
one = a%10 #일의 자리
num = (((one*10)+ten)*2)%100
print(num)
if num <=50:
    print("GOOD")
elif num > 50:
    print("OH MY GOD")
