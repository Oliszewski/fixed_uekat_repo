class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self):
        return f"Student: {self.name}"


student1 = Student("Zdzisław Kowalski", [60, 70, 65])
print(f"{student1.name} passed: {student1.is_passed()}")

student2 = Student("Marianna Nowak", [30, 40, 35])
print(f"{student2.name} passed: {student2.is_passed()}")
