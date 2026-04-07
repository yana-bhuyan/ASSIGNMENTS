class Parent:
    def property(self):
        print("Parent Property")

class Child1(Parent):
    def skill1(self):
        print("Child1 Skill")

class Child2(Parent):
    def skill2(self):
        print("Child2 Skill")

c1 = Child1()
c2 = Child2()

c1.property()
c1.skill1()

c2.property()
c2.skill2()