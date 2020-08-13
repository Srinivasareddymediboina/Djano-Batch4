class ClassA:
    a=20
    b=30
    def display():
        return "i am from ClassA"

class ClassB(ClassA):
    c=20
    d=87
    def show():
        return " i am from ClassB"

    def add():
        return ClassB.c+ClassB.d
