class Class:
    def __init__(self, id, name, Teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.Teacherid = Teacherid

    @staticmethod
    def CreateClass(obj):
        list=[]

        for i in obj:
            list.append(Class(i[0],i[1],i[2]))
        return list


        