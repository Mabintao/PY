"""
@Author: matt
@Date : 2019/11/25
@Desc : 面向对象
"""
from abc import ABCMeta, abstractmethod


class Student(object):
    # __init__ 对象初始化方法，创建对象使用
    def __init__(self, name, age, foo):
        self.name = name
        self.age = age
        self.__foo = foo  # __开头表示私有属性，一般不设置，程序员自己约束控制

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")

    def drive(self):
        if self.age > 18:
            print(f"{self.name}驾驶汽车")
        else:
            print(f"{self.name}骑自行车")


class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def gen_person(cls, name, age):
        return cls(name, age)

    @staticmethod  # 静态方法
    def is_audit(age):
        return age >= 18

    @property  # getter
    def name(self):
        return self._name

    @property  # getter
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f"{self._name}正在玩飞行棋")
        else:
            print(f"{self._name}正在玩斗地主")


class Student2(Person):  # 继承
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # 超类调用
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f"{self._grade}的{self._name}同学正在学习{course}")


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    def make_voice(self):
        print(f"{self._nickname},汪汪汪。。。")


class Cat(Pet):
    def make_voice(self):
        print(f"{self._nickname},喵喵喵。。。")


def main():
    # 对象创建
    stu1 = Student("Matt", 23, "私有属性")
    stu1.study("python")
    stu1.drive()
    # print(stu1.__foo)  # AttributeError: 'Student' object has no attribute '__foo'

    man = Person("matt", 23)
    man.play()
    man.age = 16
    man.play()
    # man.name = "Matt"  # AttributeError: can't set attribute 没有setter
    man._gender = '男'
    # man._hobby = 'java'  # AttributeError: 'Person' object has no attribute '_hobby' __slots__ 中指定ß
    Person.is_audit(23)  # 静态方法调用
    man2 = Person.gen_person("Ljx", 23)
    man2.play()

    # 继承
    student = Student2("Ljx", 23, "大班")
    print(student.grade)
    student.play()
    student.study("韩语")

    # 多态
    pets = [Dog("柴柴"),Cat("波斯")]
    for pet in pets:
        pet.make_voice()

if __name__ == "__main__":
    main()
