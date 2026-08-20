class Duck:
    def quack(self):
        print("Quack")


class Person:
    def quack(self):
        print("Person is pretending to be a duck")


def make_it_quack(obj):
    obj.quack()


duck = Duck()
person = Person()

make_it_quack(duck)  # Output: Quack
make_it_quack(person)  # Output: Person is pretending to be a duck
