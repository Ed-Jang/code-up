# 주민번호를 받은 후 2012년기준 나이 출력
id, mf = input().split()  # ex) 970109 1

if mf == "1" or mf== "2": #90s 남녀구분
    age = 2012 - (int(1900)+int(id[:2])) + 1
    print(age)
elif mf == "3" or mf== "4": #00s 남녀구분
    age = 2012 - (int(2000)+int(id[:2])) + 1
    print(age)
    

