class Father:
    def skill1(self):
        print("Gardening")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Programming")

c = Child()
c.skill1()
c.skill2()
c.skill3()