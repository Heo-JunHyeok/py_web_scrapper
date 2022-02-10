# 1.7 keyword Arguements
#       # positional Argument - 위치에 의존하는 인자
# def plus(a,b):
#     return a+b

# result=plus(2,4)
# print(result)

#       # keyword Argument - Argument의 이름으로 쌍을 이루는 것
# def plus(a,b):
#     return a-b

# result=plus(b=30,a=1)
# print(result)

# def say_hello(name,age):
#     #string 안에 변수를 넣고 싶을 때 f"string~{변수}~"
#     return f"Hello {name} you are {age} years old"
#     #return "Hello" + name + "you are" + age + "years old"

# hello = say_hello(age="12",name="hyeok")
# print(hello)
# ===============================================================

# 1.8 module
#     from (module) import (function) as (alias_name)
# ===============================================================

# 3.1 *args, **kwargs

#     매개변수를 제한없이 넣고 싶을 때 사용
#     *args : tuple로 지정, position argument
#     **kwargs : dictionary로 지정, keyword argument

# def plus(*args):
#     result = 0
#     for number in args:
#         result += number
#     print(result)

# plus(1, 1, 1, 2, 3, 5, 5, 2, 3, 1, 1, 3)
# ===============================================================

# 3.2 Object Oriented Programming(객체 지향 프로그래밍)

# class: 설계도, 기본 틀
# instance: 설계도로 만든 제품, porche, ferrari

# class Car():
#     wheels = 4
#     doors = 4
#     windows = 4
#     seats = 4

# porche = Car()
# porche.color = "Red"

# ferrari=Car()
# ferrari.color="Yellow"

# mini=Car()
# mini.color="White"
# ===============================================================

# 3.3 Methods part One
#     class 안에 있는 function

# class Car():
#     wheels = 4
#     doors = 4
#     windows = 4
#     seats = 4

#     # method의 첫번재 argument는 method를 호출하는 instance 자신(porche)
#     def start(self):
#         print(self.doors)
#         print("I started")


# porche = Car()
# porche.color = "Red Sexy Red"
# porche.start(porche)
# ===============================================================

# 3.4 Methods part TWO

# class Car():
#     def __init__(self, *args, **kwargs):
#         self.wheels = 4
#         self.doors = 4
#         self.windows = 4
#         self.seats = 4
#         self.color = kwargs.get("color", "black")  # kwargs가 있으면 왼쪽 없으면 오른쪽
#         self.price = kwargs.get("price", "$20")

#     def __str__(self):
#         return f"Car with {self.wheels} wheels"

# # print(dir(Car))# classdp 있는 모든 properties
# # ex) __str__: 호출될 때마다 그 class의 instance를 출력


# porche = Car(color="green", price="$40")
# print(porche.color, porche.price)

# mini = Car()
# print(mini.color, mini.price)
# ===============================================================

# 3.5 Extending Class

class Car():
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"


class Convertible(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # super: 부모클래스를 호출하는 함수
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"


class Something(Convertible):
    pass


porche = Convertible(color="green", price="$40")
print(porche.time)

# method를 extend할 때 그냥 하면 overriding(재정의)되기 때문에 super를 사용하여 부모클래스를 호출
# overloading과 overriding 헷갈리지 말기
# overloading: 여러 method가 같은 이름을 갖고 있으나 인자의 수나 자료형이 다른 경우
