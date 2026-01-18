from typing import List


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


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library {self.city} ({self.street})"


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
        title: str,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        self.title = title

    def __str__(self):
        return (
            f"Book: '{self.title}' by {self.author_surname} (Loc: {self.library.city})"
        )


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: List[Book], order_date: str
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_titles = ", ".join([b.title for b in self.books])
        return (
            f"--- ORDER ---\n"
            f"Date: {self.order_date}\n"
            f"Issued by: {self.employee}\n"
            f"For: {self.student.name}\n"
            f"Books: {book_titles}"
        )


lib_katowice = Library("Katowice", "Młyńska 1", "40-001", "8-16", "123-456")
lib_gliwice = Library("Gliwice", "Akademicka 2", "44-100", "9-17", "987-654")


b1 = Book(lib_katowice, "2020", "Robert", "Martin", 400, "Clean Code")
b2 = Book(lib_katowice, "2019", "Francois", "Chollet", 350, "Deep Learning with Python")
b3 = Book(lib_katowice, "2021", "Aurélien", "Géron", 800, "Hands-On ML")
b4 = Book(lib_gliwice, "1949", "George", "Orwell", 200, "1984")
b5 = Book(lib_gliwice, "1954", "J.R.R.", "Tolkien", 500, "The Fellowship of the Ring")


emp1 = Employee(
    "Adam",
    "Nowak",
    "2020-01-01",
    "1990-05-12",
    "Katowice",
    "Opolska",
    "40-001",
    "111-222",
)
emp2 = Employee(
    "Ewa",
    "Kowalska",
    "2019-05-15",
    "1985-11-02",
    "Gliwice",
    "Dworcowa",
    "44-100",
    "333-444",
)
emp3 = Employee(
    "Piotr",
    "Wiśniewski",
    "2021-09-01",
    "1995-03-20",
    "Zabrze",
    "Wolności",
    "41-800",
    "555-666",
)


s1 = Student("Marek Zegarek", [55, 60])
s2 = Student("Kasia Fasola", [90, 95])
s3 = Student("Tomek Domek", [40, 45])

order1 = Order(emp1, s1, [b1, b2], "2023-10-12")
order2 = Order(emp2, s2, [b4], "2023-10-13")


print(order1)
print("\n")
print(order2)
