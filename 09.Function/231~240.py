### 231~240


# 231
# 아래 코드를 실행한 결과를 예상하라.
#
# def n_plus_1 (n) :
#     result = n + 1
#
# n_plus_1(3)
# print (result)
# 정답: print(result)에서 에러가 난다. 함수 안에서 사용한 변수는 함수 밖에서 사용할 수 없다.
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print(result)


# 232
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
#
# make_url("naver")
# www.naver.com
def make_url(string):
    url = 'www.' + string + '.com'
    return url
make_url("naver")


# 233
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
#
# make_list("abcd")
# ['a', 'b', 'c', 'd']
def make_list(string):
    list = []
    for value in string:
        list.append(value)
    return list
make_list("abcd")


# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
#
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]
def pickup_even(list):
    my_list = []
    for num in list:
        if num % 2 == 0:
            my_list.append(num)
    return my_list
pickup_even([3, 4, 5, 6, 7, 8])


# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
#
# convert_int("1,234,567")
# 1234567
def convert_int(string):
    return int(string.replace(',', ''))
convert_int("1,234,567")


# 236
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수(num) :
#     return num + 4
#
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)
#  정답: 14, 18, 22
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)


# 237
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수(num) :
#     return num + 4
#
# c = 함수(함수(함수(10)))
# print(c)
#  정답: 22
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)


# 238
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     return num * 10
#
# a = 함수1(10)
# c = 함수2(a)
# print(c)
#  정답: 140
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)


# 239
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
#
# c = 함수2(10)
# print(c)
#  정답: 16
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)


# 240
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수0(num) :
#     return num * 2
#
# def 함수1(num) :
#     return 함수0(num + 2)
#
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
#
# c = 함수2(2)
# print(c)
# 정답: 28
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)