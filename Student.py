class Student:
    def _init_(self,name,marks):
        self.__name =None
        self.marks =None
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_marks(self,marks):
        self.marks = marks
    def get_marks(self):
        if self.marks >= 0 and self.marks <= 100:
            return self.marks
        else:
            return "Error : Marks must be between 0 and 100"
S=Student('Alice',160)
S.set_name('Alice')
print(S.get_name())
S.set_marks(85)
print(S.get_marks())