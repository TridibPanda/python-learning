# Method Resolution Order (MRO) and Multiple Inheritance
# MRO determines the order in which Python looks for methods in a hierarchy of classes.
# Python uses the C3 Linearization algorithm to determine the MRO.

# Base class A with a show() method
class A:
    def show(self):
        print("A")


# Class B inherits from A and overrides the show() method
# super().show() calls the next method in the MRO chain
class B(A):
    def show(self):
        print("B")
        super().show()  # Calls the next show() method in MRO


# Class C also inherits from A and overrides the show() method
# super().show() calls the next method in the MRO chain
class C(A):
    def show(self):
        print("C")
        super().show()  # Calls the next show() method in MRO


# Class D uses multiple inheritance: inherits from both B and C
# The order matters: B is the first parent, C is the second parent
# MRO for D will be: D → B → C → A → object
class D(B, C):
    pass


# Create an instance of D and call show()
d = D()
d.show()

# Execution flow:
# 1. d.show() calls D.show() - but D doesn't have show(), so it looks up the MRO
# 2. Next in MRO is B, so B.show() is called → prints "B"
# 3. super().show() in B calls the next in MRO, which is C → C.show() is called → prints "C"
# 4. super().show() in C calls the next in MRO, which is A → A.show() is called → prints "A"
# 5. A.show() doesn't call super(), so execution stops

# Output:
# B
# C
# A

# To see the MRO order, you can use:
# print(D.mro())
# or
# print(D.__mro__)
