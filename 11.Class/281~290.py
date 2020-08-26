### 281~290


# 281 클래스 정의
# 다음 코드가 동작하도록 차 클래스를 정의하세요.
#
# >> car = 차(2, 1000)
# >> car.바퀴
# 2
# >> car.가격
# 1000
class Vehicle:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
car = Vehicle(2, 1000)
car.wheel
car.price


# 282 클래스 상속
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.
class Vehicle:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
class Bicycle(Vehicle):
    pass

bicycle = Bicycle(2, 1000)
bicycle.wheel
bicycle.price


# 283 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
#
# >> bicycle = 자전차(2, 100)
# >> bicycle.가격
# 100
class Vehicle:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class Bicycle(Vehicle):
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

bicycle = Bicycle(2, 100)
bicycle.wheel
bicycle.price


# 284 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
#
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.구동계
# 시마노
class Vehicle:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class Bicycle(Vehicle):
    def __init__(self, wheel, price, 구동계):
        super().__init__(wheel, price)
        self.구동계 = 구동계

bicycle = Bicycle(2, 100, '시마노')
bicycle.wheel
bicycle.price
bicycle.구동계


# 285 클래스 상속
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
#
# >> car = 자동차(4, 1000)
# >> car.정보()
# 바퀴수 4
# 가격 1000
class Vehicle:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class Sedan(Vehicle):
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def info(self):
        print('바퀴수: ', self.wheel)
        print('가격: ', self.price)


car = Sedan(4, 1000)
car.info()


# 286 부모 클래스 생성자 호출
# 다음 코드가 동작하도록 자전차 클래스를 수정하세요.
#
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
class Vehicle:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class Bicycle(Vehicle):
    def __init__(self, wheel, price, 구동계):
        super().__init__(wheel, price)
        self.구동계 = 구동계

    def info(self):
        print('바퀴수: {}'.format(self.wheel))
        print('가격: {}'.format(self.price))

bic = Bicycle(2, 100, "시마노")
bic.info()


# 287 부모 클래스 메서드 호출
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
#
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
# 구동계 시마노
class Vehicle:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


class Bicycle(Vehicle):
    def __init__(self, wheel, price, 구동계):
        super().__init__(wheel, price)
        self.구동계 = 구동계

    def info(self):
        print('바퀴수: {}'.format(self.wheel))
        print('가격: {}'.format(self.price))
        print('구동계: {}'.format(self.구동계))


bic = Bicycle(2, 100, "시마노")
bic.info()


# 288 메서드 오버라이딩
# 다음 코드의 실행 결과를 예상해보세요.
#
# class 부모:
#   def 호출(self):
#     print("부모호출")
#
# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
# 나 = 자식()
# 나.호출()
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()


# 289 생성자
# 다음 코드의 실행 결과를 예상해보세요.
#
# class 부모:
#   def __init__(self):
#     print("부모생성")
#
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
# 나 = 자식()
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
나 = 자식()


# 290 부모클래스 생성자 호출
# 다음 코드의 실행 결과를 예상해보세요.
#
# class 부모:
#   def __init__(self):
#     print("부모생성")
#
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()
#
# 나 = 자식()
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()