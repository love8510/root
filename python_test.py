# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:57:15 2022

@author: gravi
"""

"""
@CH_1 프로그래밍과 파이썬 

@정답을  만들수 있는 숫자를 알려줘!_ 5또는 5.0 이 출력될수 있게 해라 
print(20%15)
print(10.0//2.0)


@5년후 나의 나이는 ?
age = 15
age += 5 
print(age)

people = 100
people *= 3.5
print(people)

age = 15
people = 3
total_ = 0

age *= people
total_ = age


@변수의 이름_ 성과 이름을 구성한다. 
한국사람 이름도 정할때 규칙이 있듯 변수도 이름을 정하는 규칙이 있다.

# 아래 4가지 변수는 모두 규칙에 맞지 않는 이름의 변수입니다.
# my age - 나의 나이
# 2_class_num - 2학년 때 반 번호
# apple+orange - 오늘 판매한 사과와 오렌지 개수
# 10 - 10살 때 살았던 동네주소

myage = 15
print(myage)

class_num_2 = 5
print(class_num_2)

apple_orange = 45
print(apple_orange)

주소_10 = "경기도 판교"
print(주소_10)

@icetea 아이스티 가격이 담겨 있었습니다.
500원 올랐다고 하네요. 사칙연산을 사용해서 출력해보세요. 
icetea = 3000
icetea += 500
print(icetea)


@ 미션 문제  
변수의 점수를 정의하고 평균값을 만들자 

디콘이의_세포들 = 9.97
디랩일기 = 8.86
파이썬독학 = 9.3
샤이왕 = 8.55
하이드혁명 = 9.34

total = 디콘이의_세포들 + 디랩일기 + 파이썬독학 + 샤이왕 + 하이드혁명 
print(total /5)

"""

"""
@CH_2 문자열 

"""

"""
@CH_3 리스트 

"""

"""
@CH_4 제어문 - 조건문(if)

"""

"""
@CH_5 미션 챕터  

"""

"""
@CH_6 제어문 - 반복문 

"""

"""
@CH_7 무한반복과 딕셔너리 

"""

"""
1. 나는 엘이야 몇번 출력될까요?

i = 0
while i < 5:
    print('나는 엘{}이야'.format(i))
    i += 1


2. 조건의 결과가 항상 참 이라면 ? 


while True:
    print("D.LAB")


3. 무한반복의 구조를 알아보자. 

조건이 항상 참이어서 while문 내부 명령이 무한히 실행되는 것을 
무한반복이라고 한다.


text = ""
text2 = []


while True:

    add = input("추가할 내용 :")
    text += add 
    print(text)



while True:

    add = input("추가할 내용 :")
    text.append(add)
    print(text)


4. 무한반복의 break 를 사용해 보자.



text = ""

while True :

    if len(text) >= 15:
        break

    add = input("추가할 내용:")
    text += add 
    print(text)



5. 딕셔너리_ 리스트와의 차이점 꼭 구분해주기 
    변수가 여러개의 방에 담겨있는것이 리스트라면 
    딕셔너리는 key value 를 갖는다. 
    insert/delete 개념 

    딕셔너리 만드는 방법 
    1.처음과 끝을 중괄호{} 감싸기 
    2.중괄호 안에  key value가 콜론으로: 연결된 한쌍의 아이템이다.
    3.각 아이템은 콤마로 구분된다. 



myInfo = {}

myInfo = {'name':'dlab','age':17,'school':'디랩학원'}
print(myInfo,type(myInfo))


6. 실습 딕셔너리를 조금더 연습하지 

테이블로 구성된 딕셔너리 
key->apple:500
     banana:2500
     orange:2000



fruits = {'apple':500,'banana':2500,'orange':2000}
print("바나나의 가격은 {}원 입니다.".format(fruits['banana']))

fruits['banana'] += 50000

print(fruits['banana'])



boolean 값으로 반환된다. 여부 확인...

print('orange' in fruits)


del fruits['banana']
print(fruits)
print('banana' in fruits)


7. 실습 

1)
key
value ---> 값으로 확인할수 있다. 
2) update 문을 사용하여 추가한다.->여러개 추가 가능 .

중복되는 여부에 대해서 확인하고 중복될시 
추가되지 않는 부분 알려준다. 
배열의 모든값을 sum 함수가 합할수 잇다. 


temp = {'서울':20.4,'강릉':22.8,'부산':24.0,'대전':26.8,'대구':23.7}
print(temp.keys())
print(temp.values())
temp.update({'서울d':20.4,'강s릉':22.8})
print(temp)


temp['제주'] = 27.5
temp['대구'] = 30.2
temp['대전'] = 33.2
temp['강릉'] = 78.2

print(sum(temp.values()))


8. 미션 파트_ 딕셔너리로 나만의 사전을 만들어 보자. 

1.사용자에게 영어 단어를 입력받아 변수 k에 대입하세요
2.사용자에게 단어 뜻을 입력 받아, 변수 v 에 때입하세요
3. 변수 myDict 변수 k 를 key로 변수 v를 value 로 한 아이템을 추가하자 
4.잘 추가 되었는지 myDict를 출력하자 


myInfo = {}

for i in range(0,5):

    k = inpu 릋퉆ㅇ누피ㅜ퍼ㅏㄴ풏터ㅣ ㅍ느타ㅣ 
    v = input("뜻")ㅎㅍㅎfor n in [1,3,5,7,9]:


2.반복할 명령 

for n in [1,3,5,7,9]

     print(n)


3.반복할 명령_ 원하는 문장도 같이 출력하자

for n in [1,3,5,7,9] :

    print(n)
    print("for문 반가워!")



"""



