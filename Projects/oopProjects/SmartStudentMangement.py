class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def get_avg(self):
        total = 0
        for num in self.marks:
            total +=num  
        if (len(self.marks) != 0) :   
            avg = total/len(self.marks) 
            return avg
        else:
            print("0 Average Marks")    

    def get_grades(self):
        avg  = self.get_avg()
        if avg >=90:
            return "A"
        elif avg >=80:
            return "B"
        elif avg >=70:
            return "C" 
        elif avg >=60 :
            return "D"  
        else:
            return "F"  
        
class StudentManagement:
    def __init__(self) :
        self.students = [] 

    def add_students(self, student) :
        self.students.append(student)  
        print(f"{self.student} was added")

    def view_student(self, name):
        if not self.students:
            print("No student with {name} name was found")
        for person in self.students:
            print(f"Name: {")     




