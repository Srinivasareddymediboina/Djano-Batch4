class ClassA:
    def A():
        return "i am from classA"
class ClassB:
    def B():
        return "i am from classB"
class ClassC(ClassA,ClassB):
    def C():
        return "i am from classc"
