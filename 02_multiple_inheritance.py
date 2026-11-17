class Teacher:
    def teach(self):
        print("Teaching students")


class Researcher:
    def research(self):
        print("Doing research")


class Professor(Teacher, Researcher):
    pass


p = Professor()
p.teach()
p.research()
