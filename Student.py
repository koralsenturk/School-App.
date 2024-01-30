class Student:
    def __init__(self, STUDENTNUMBER, NAME, SURNAME, BIRTHDATE, GENDER, ID, classid):
        if ID is None:
            self.ID = 0
        else:
            self.ID = ID
        self.STUDENTNUMBER = STUDENTNUMBER
        self.NAME = NAME
        self.SURNAME = SURNAME
        self.BIRTHDATE = BIRTHDATE
        self.GENDER = GENDER
        self.classid = classid


    @staticmethod
    def CreateStudent(obj):
        list = []
        if isinstance(obj, tuple):
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list

     