from dbmanager import DbManager
import datetime
from Student import Student
from Teacher import Teacher



class App:
    def __init__(self):
        self.db = DbManager()


    def initApp(self):
        msg= "******\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Öğretmen Güncelle\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent()
            elif islem == '5':
                self.addTeacher()
            elif islem == '6':
                self.editTeacher()
            elif islem == '7':
                break
            elif islem == 'E' or islem == 'Ç':
                break
            else:
                print("yanlış seçim")
    
    def addStudent(self):
        self.displayClasses()
        classid = int(input('hangi sınıf: '))
        STUDENTNUMBER = input('numara: ')
        NAME = input('isim: ')
        SURNAME = input('soyisim: ')
        year = int(input('doğum yılı: '))
        month= int(input('doğum ayı: '))
        day= int(input('doğum günü:: '))
        
        BIRTHDATE = datetime.date(year,month,day)
        GENDER = input('cinsiyet(E/K): ')

        student = Student(STUDENTNUMBER, NAME, SURNAME, BIRTHDATE, GENDER, None, classid)
        self.db.addStudent(student)


    def editStudent(self):
        classid = self.displayStudents()
        
        studentid = int(input('öğrenci id: '))
        student = self.db.getStudentByID(studentid)
       
        student[0].STUDENTNUMBER = input('Okul No: ') or student[0].STUDENTNUMBER
        student[0].NAME = input('isim: ') or student[0].NAME
        student[0].SURNAME = input('soyisim: ') or student[0].SURNAME
        student[0].GENDER = input('cinsiyet(E/K) ') or student[0].GENDER
        student[0].classid = input('sınıf: ') or student[0].classid
        
        # year = input("year: ") or student[0].BIRTHDATE.year
        # month = input("month: ") or student[0].BIRTHDATE.month
        # day = input("day: ") or student[0].BIRTHDATE.day

        # student[0].BIRTHDATE =datetime.date(year,month,day)
        student[0].BIRTHDATE = input('doğum tarihi') or student[0].BIRTHDATE

        self.db.editStudent(student[0])

    def deleteStudent(self):
        classid = self.displayStudents()
       
        studentid = int(input('öğrenci id: '))
        self.db.deleteStudent(studentid)


    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')
    
    
    
    
    def displayStudents(self):
        self.displayClasses()
        classid = int(input('hangi sınıf: '))
        students = self.db.getStudentByClassid(classid)
        print('Öğrenci Listesi')
        for std in students:
            print(f'{std.ID}-{std.NAME} {std.SURNAME}')
        return classid
    



    def addTeacher(self):
        branch = input('hangi branş: ')
        name = input('isim: ')
        surname = input('soyisim: ')
        year = int(input('doğum yılı: '))
        month= int(input('doğum ayı: '))
        day= int(input('doğum günü: '))
        
        birthdate = datetime.date(year,month,day)
        
        gender = input('cinsiyet(E/K): ')

        teacher = Teacher(None, branch, name, surname, birthdate, gender)
        self.db.addTeacher(teacher)



    def editTeacher(self):
        self.db.displayTeacher()
       


    




    # def editTeacher(self):
    #     self.displayTeacher()
       
    #     teacherId = int(input("teacherId seçiniz: "))
    #     teacher = self.db.getTeacherByID(teacherId)
    #     for i in teacher:
            
    #         i[0].branch = input('hangi branş: ')
    #         i[0].name = input('isim: ')
    #         i[0].surname = input('soyisim: ')
    #         i[0].birthdate = input('doğum tarihi')
    #         i[0].gender = input('cinsiyet(E/K)')
        
     
    #     # year = input("year: ")
    #     # month = input("month: ")
    #     # day = input("day: ")
    #     # birthdate = datetime.date(year,month,day)
        
        
    #         self.db.editTeacher(i[0])



    # def displayTeacher(self):
    #     teachers = self.db.getTeacher()
    #     print('Öğretmen Listesi')
    #     for te in teachers:
    #         print(f'{te.id}-{te.name} {te.surname}')
     


app = App()
app.initApp()


