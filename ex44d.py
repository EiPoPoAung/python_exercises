class Parent(object):
    def override(self):
        print("Parent override()")
    def implicit(self):
        print("PARENT implicit()")
    def altered(self):
        print("PARENT altered()")
class Child(Parent):
    def override(self):
        print("ChILD override()")
    def altered(self):
        print("CHILD,BEFORE PARENT alterred()")
        super(Child,self).altered()
        print("CHILD,AFTER PARENT altered()")
dad=Parent()
son=Child()
dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()
