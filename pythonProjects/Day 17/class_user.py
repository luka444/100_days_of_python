
class User:
    def __init__(self,id,username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        user.following += 1

user_1 = User('001','luka')
user_2 = User('002','Vaxo')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)