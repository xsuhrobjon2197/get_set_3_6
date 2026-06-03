#6-m
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if new_password == 5:
            self.__password = new_password
        else:
            print("Wrong password")
            
u1 = User("john", "<PASSWORD>")

print(u1.username)
print(u1.get_password())

u1.set_password(7)
print(u1.get_password())

u1.set_password(8)
print(u1.get_password())
