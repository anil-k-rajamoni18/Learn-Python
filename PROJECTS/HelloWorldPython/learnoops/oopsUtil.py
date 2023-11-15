class Student(object):
    def __init__(self, name: str, college: str, branch: str, marks: list[int]):
        self.__studentName = name
        self.__studentCollege = college
        self.__studentBranch = branch
        self.__studentMarks = marks

    def calculate_total(self):
        return sum(self.__studentMarks)

    def display_average(self):
        return sum(self.__studentMarks) / len(self.__studentCollege)

    def display_name(self):
        return self.__studentName

    def display_college(self):
        return self.__studentCollege

    def display_branch(self):
        return self.__studentBranch

    def display_marks(self):
        return self.__studentMarks

    def __str__(self):
        return f'<Student [name: {self.__studentName}, college: {self.__studentCollege}, branch: {self.__studentBranch}]>'