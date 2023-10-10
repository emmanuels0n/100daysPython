class User:  # Used created class, NameOfClassAlwaysCapitalized (Pascal case)

    def __init__(self, user_id, username):  # initialise attributes, inside this init function is where we
        # initialise or create the starting values for our attributes
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0  # Default value
        self.following = 0

    def follow(self, user):  # A method, always starts with the "self" parameter
        user.followers += 1
        self.following += 1

    # pass  # Just to leave the class empty without pycharm messing


user_1 = User("001", "Angela")
user_2 = User("002", "Emmanuel")

# user_1 = User()  # Object from a previously created class, (snake_case)
# user_1.id = "001" # Add attributes to a class
# user_1.username = "Angela"

print(user_1.username)
print(user_1.id)

# Is also possible to create methods, the attributes are th things that the object has and the methods are the things
# that the object does

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
