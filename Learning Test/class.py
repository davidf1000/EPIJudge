class Student:
    data = 3

    def get_data(self) -> int:
        return self.data

    def set_data(self, x: int) -> int:
        self.data = x


x = Student()
print(x.data)
x.set_data(5)
print(x.data)
