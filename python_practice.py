# -*- coding: utf-8 -*-
"""
파이썬 연습문제 모음

python_test.py 에서 비어 있던 챕터(CH_2 ~ CH_7)를 채우는 연습문제입니다.
각 문제 아래에 정답 예시가 있으니, 먼저 직접 풀어본 다음 확인해 보세요.

실행 방법: python python_practice.py
"""


print("=" * 40)
print("@CH_2 문자열")
print("=" * 40)

"""
문제 2-1. 이름과 나이를 변수에 담고,
"안녕하세요, 저는 디랩이고 17살입니다." 처럼 출력해 보세요.
(format 과 f-string 두 가지 방법으로 해보기)
"""
name = "디랩"
age = 17
print("안녕하세요, 저는 {}이고 {}살입니다.".format(name, age))
print(f"안녕하세요, 저는 {name}이고 {age}살입니다.")

"""
문제 2-2. word = "python" 에서
1) 첫 글자  2) 마지막 글자  3) 앞의 세 글자  4) 거꾸로 뒤집은 문자열
을 출력해 보세요.
"""
word = "python"
print(word[0])
print(word[-1])
print(word[:3])
print(word[::-1])

"""
문제 2-3. "-" 를 20번 반복해서 구분선을 만들어 보세요.
"""
print("-" * 20)

"""
문제 2-4. sentence = "나는 파이썬이 좋아요" 에서
"파이썬" 을 "자바" 로 바꾸고, 문장의 글자 수(len)도 출력해 보세요.
"""
sentence = "나는 파이썬이 좋아요"
print(sentence.replace("파이썬", "자바"))
print(len(sentence))


print("=" * 40)
print("@CH_3 리스트")
print("=" * 40)

"""
문제 3-1. 좋아하는 과일 3개를 리스트로 만들고,
두 번째 과일을 출력해 보세요.
"""
fruits = ["사과", "바나나", "포도"]
print(fruits[1])

"""
문제 3-2. 위 리스트에 "딸기" 를 추가(append)하고,
"바나나" 를 삭제(remove)한 뒤 리스트를 출력해 보세요.
"""
fruits.append("딸기")
fruits.remove("바나나")
print(fruits)

"""
문제 3-3. scores = [85, 92, 78, 95, 60] 에서
최고 점수, 최저 점수, 합계, 평균을 출력해 보세요.
"""
scores = [85, 92, 78, 95, 60]
print(max(scores), min(scores), sum(scores), sum(scores) / len(scores))

"""
문제 3-4. scores 를 작은 순서대로, 큰 순서대로 정렬해서 출력해 보세요.
"""
print(sorted(scores))
print(sorted(scores, reverse=True))


print("=" * 40)
print("@CH_4 제어문 - 조건문(if)")
print("=" * 40)

"""
문제 4-1. 숫자 num 이 짝수면 "짝수", 홀수면 "홀수" 를 출력해 보세요.
"""
num = 7
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

"""
문제 4-2. 점수 score 에 따라 학점을 출력해 보세요.
90점 이상 A, 80점 이상 B, 70점 이상 C, 나머지는 F
"""
score = 83
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

"""
문제 4-3. 나이 age 가 8살 미만이거나 65살 이상이면 "무료",
그렇지 않으면 "1500원" 을 출력해 보세요. (or 사용하기)
"""
age = 70
if age < 8 or age >= 65:
    print("무료")
else:
    print("1500원")

"""
문제 4-4. "바나나" 가 fruits 리스트 안에 있으면 "있어요",
없으면 "없어요" 를 출력해 보세요. (in 사용하기)
"""
if "바나나" in fruits:
    print("있어요")
else:
    print("없어요")


print("=" * 40)
print("@CH_5 미션 챕터")
print("=" * 40)

"""
미션 5-1. 편의점 계산기
아이스티 3000원 2개, 과자 1500원 3개를 샀습니다.
총 금액을 구하고, 10000원을 냈을 때 거스름돈을 출력해 보세요.
총 금액이 10000원을 넘으면 "돈이 부족해요" 를 출력하세요.
"""
total = 3000 * 2 + 1500 * 3
paid = 10000
print("총 금액:", total)
if total > paid:
    print("돈이 부족해요")
else:
    print("거스름돈:", paid - total)

"""
미션 5-2. 영화 평점 리스트에서 9점 이상인 영화의 개수를 세어 보세요.
"""
ratings = [9.97, 8.86, 9.3, 8.55, 9.34]
count = 0
for r in ratings:
    if r >= 9:
        count += 1
print("9점 이상인 영화:", count, "개")


print("=" * 40)
print("@CH_6 제어문 - 반복문")
print("=" * 40)

"""
문제 6-1. 1부터 10까지 출력해 보세요. (range 사용)
"""
for i in range(1, 11):
    print(i, end=" ")
print()

"""
문제 6-2. 1부터 100까지 더한 값을 출력해 보세요.
"""
total = 0
for i in range(1, 101):
    total += i
print(total)

"""
문제 6-3. 구구단 3단을 "3 x 1 = 3" 형식으로 출력해 보세요.
"""
for i in range(1, 10):
    print(f"3 x {i} = {3 * i}")

"""
문제 6-4. 1부터 20까지 중에서 3의 배수만 출력해 보세요.
"""
for i in range(1, 21):
    if i % 3 == 0:
        print(i, end=" ")
print()

"""
문제 6-5. 별(*)로 아래 모양을 만들어 보세요.
*
**
***
****
*****
"""
for i in range(1, 6):
    print("*" * i)


print("=" * 40)
print("@CH_7 무한반복과 딕셔너리")
print("=" * 40)

"""
문제 7-1. while 문으로 10부터 1까지 거꾸로 세고,
마지막에 "발사!" 를 출력해 보세요.
"""
n = 10
while n > 0:
    print(n, end=" ")
    n -= 1
print("발사!")

"""
문제 7-2. while True 와 break 를 사용해서
2를 계속 곱하다가 1000을 넘으면 멈추고, 그 값을 출력해 보세요.
"""
x = 1
while True:
    x *= 2
    if x > 1000:
        break
print(x)

"""
문제 7-3. 학생 이름과 점수를 담은 딕셔너리를 만들고,
모든 학생의 이름과 점수를 "이름: 점수점" 형식으로 출력해 보세요.
"""
students = {"민수": 88, "지영": 95, "현우": 72}
for key, value in students.items():
    print(f"{key}: {value}점")

"""
문제 7-4. 위 딕셔너리에서 점수가 가장 높은 학생의 이름을 출력해 보세요.
"""
best = max(students, key=students.get)
print("1등:", best)

"""
문제 7-5. 문장 속 글자가 각각 몇 번 나왔는지 딕셔너리로 세어 보세요.
"""
text = "banana"
counter = {}
for ch in text:
    if ch in counter:
        counter[ch] += 1
    else:
        counter[ch] = 1
print(counter)

"""
도전 문제. 나만의 단어장 (input 사용 - 직접 실행해서 해보세요)
사용자가 "그만" 을 입력할 때까지 영어 단어와 뜻을 입력받아
myDict 에 추가하고, 마지막에 전체 단어장을 출력하세요.

myDict = {}
while True:
    k = input("영어 단어 (그만 입력시 종료): ")
    if k == "그만":
        break
    v = input("뜻: ")
    myDict[k] = v
print(myDict)
"""
