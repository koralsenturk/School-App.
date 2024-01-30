import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class



class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()


    def getStudentByID(self, ID):
        sql = "Select * From student Where ID = %s"
        value = (ID,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error', err)
        

    def getStudentByClassid(self, classid):
        sql = "Select * From student Where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error', err)
    
    def addStudent(self, student: Student):
        sql = "Insert INTO student(STUDENTNUMBER, NAME, SURNAME, BIRTHDATE, GENDER, classid) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.STUDENTNUMBER, student.NAME, student.SURNAME, student.BIRTHDATE, student.GENDER, student.classid)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
           
        except mysql.connector.Error as err:
            print('Error', err)
        
    def editStudent(self, student: Student):
        sql = "Update student Set STUDENTNUMBER=%s, NAME=%s, SURNAME=%s, BIRTHDATE=%s, GENDER=%s, classid=%s Where ID=%s"
        value = (student.STUDENTNUMBER, student.NAME, student.SURNAME, student.BIRTHDATE, student.GENDER, student.classid, student.ID)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} kayıt güncellendi.')
           
        except mysql.connector.Error as err:
            print('Error', err)



    def deleteStudent(self, studentid):
        sql = "Delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi.')
           
        except mysql.connector.Error as err:
            print('Error', err)

    

    def getClasses(self):
        sql = "Select * From class"
      
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error', err)

    def addTeacher(self, teacher: Teacher):
        sql = "Insert INTO teacher(branch, name, surname, birthdate, gender) VALUES(%s,%s,%s,%s,%s)"
        value = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
           
        except mysql.connector.Error as err:
            print('Error', err)


    def displayTeacher(self):
     
        sql = "SELECT * FROM teacher"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Teacher(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print("Error: ", err)

        # teachers = cursor.fetchall()
        # for ogr in teachers:
        #     print(ogr)


    def getTeacherByID(self, id):
        sql = "SELECT * FROM teacher WHERE id = %s"
        value =(id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Teacher(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print("Error: ", err)


    def editTeacherDB(self, teacher : Teacher):
    
 
        sql = "Update teacher Set branch=%s, name=%s, surname=%s, birthdate=%s, gender=%s, Where ID=%s"
        value = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender, teacher.id)
        self.cursor.execute(sql,value)












    # def editTeacher(self, teacher: Teacher):
    #     sql = "Update teacher Set (branch=%s, name=%s, surname=%s, birthdate=%s, gender=%s Where id=%s)"
    #     value = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender, teacher.id)
    #     self.cursor.execute(sql,value)
    #     try:
    #         self.connection.commit()
    #         print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
           
    #     except mysql.connector.Error as err:
    #         print('Error', err)

    # def getTeacher(self):
    #     sql = "Select * From teacher"
    #     self.cursor.execute(sql,)
    #     try:
    #         obj = self.cursor.fetchall()
    #         print(obj)
    #         return Teacher.CreateTeacher(obj) 
           
    #     except mysql.connector.Error as err:
    #         print('Error', err)       
   
    # def getTeacherByID(self, id):
    #     sql = "Select * From teacher Where id = %s"
    #     value = (id,)
    #     self.cursor.execute(sql,value)
    #     try:
    #         obj = self.cursor.fetchone()
    #         return Teacher.CreateTeacher(obj)
    #     except mysql.connector.Error as err:
    #         print('Error', err)




    def __del__(self):
        self.connection.close()
        print('db silindi')

    


db = DbManager()



liste = db.displayTeacher()
print(liste[0])



# student = db.getStudentByID(2)
# # print(student.NAME)
# # print(student.SURNAME)

# student[0].NAME = 'Mehmet'
# student[0].SURNAME = 'Benzersiz'
# student[0].STUDENTNUMBER = '115'
# # db.addStudent(student[0])     #getstudentbyid fonk tanımlanan id nin tüm bilgilerini kopyalayıp, yeni tanımlanacak arkadaşın eksik kalan bilgilerine ekliyor.
# db.editStudent(student[0])
# # students = db.getStudentByClassid(1)