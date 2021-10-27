class User:
    '''
    id=100#estos son mis atributos
    full_name = "full name"
    personal_email = "personal_email@gmail.com"
    '''

    def __init__(self, id, full_name, personal_email):#(def __init__ es mi contructor)Un CONSTRUCTOR es Obligarte a inicializar los atributos de un objeto
        self.id = id
        self.full_name = full_name
        self.personal_email = personal_email

object_user = User("0122110655", " Cesar G", "0122110655@alumnos.univa.mx")
#print(object_user)
print("0" + str(object_user.id))
print(object_user.full_name)
print(object_user.personal_email)


#Un CONSTRUCTOR es Obligarte a inicializar los atributos de un objeto