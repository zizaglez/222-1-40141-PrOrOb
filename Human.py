class Human:

    born_year = 1987

    def say_hello(self):
        print("Hello")

    def say_hello_user(self, user_name):
        print("Hello "+ user_name)



human_one = Human()
print(human_one)
print(human_one.born_year)
human_one.say_hello()#aqui estamos invocando
human_one.say_hello_user("Cesar")#aqui estamos invocando
