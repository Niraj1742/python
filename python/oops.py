class student:

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name
    
Student1=student()
Student1.set_name("shehnaaz")
print(Student1.name)

Student2=student()
Student2.set_name("parag")
print(Student2.get_name())