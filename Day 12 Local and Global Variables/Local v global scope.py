
User_height = 1.8  # Global scope 

def user_data():
    user_weight = 60
    print(user_weight)

user_data()
print(User_height)
# print(user_weight) >> name not defined error because it has a local scope
