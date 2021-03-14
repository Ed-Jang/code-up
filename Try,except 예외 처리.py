try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0}/{1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러 발생")
except ZeroDivisionError as err:
    print(err)
except Exception as err: #위에 설정한 에러 제외 나머지 에러처리
    print("알 수 없는 에러가 발생")
    print(err)
