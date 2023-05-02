"""
dictionary:
-PYTHON에서 사용하는 자료구조중 하나
-KEY와 VALUE 쌍으로 사용함
-문법:{중괄호}와 :를 이용
-indexing가능->key를 이용해서
-indexing method 이용 가능(get)
-VALUE를 수정하는 법
1.indexing을 이용하는 방법
2.update method이용하는법
=key와value 쌍을 추가하는 방법
indexing을 이용
=key와value 쌍을 삭제하는 방법
1.del 이용
-dict 구조 안에 key 가 있는지 확인할때 "key in dict"사용
"""

height = {"윤성": 145, "도윤": 158, "아인": 151}
print(type(height))
print(height["도윤"])


# print('윤성이 말했다."왜?"')
print(height["아인"])
print(height.get("아인"))

height["도윤"] = 185
print(height)

height.update({"윤성": 195})
print(height)

height["선생남"] = 178
print(height)

height.update({"보리": 50})
print(height)

del height["선생남"]
print(height)

del height["보리"]
print(height)

print(height.keys())
print(height.values())

print("윤성" in height)
print("보리" in height)

fruits = {"orange": 50, "banana": 100, "apple": 250}
fruit = input("This is fruit store.What do you want?:")
print(f"We have {fruit}.{fruits[fruit]}left")
