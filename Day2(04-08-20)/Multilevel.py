class ClassA:
    def A():
        return " i am from classA"

class ClassB(ClassA):
    def B():
        return "i am from class B"

class ClassC(ClassB):
    def C():
        return "I am from ClassC"
