# # File not found
#
# try:   # Inside the try block, it passes all errors
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print((a_dictionary["Something"]))
# except FileNotFoundError:  # It's better to specific the type of error
#     file = open("a_file.txt", "w")  # Like this I´m creating the file
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:  # Code that runs no matter what happens.
#     raise TypeError('This is an error I made up')  # Raises your own errors
#     # file.close()
#     # print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise TypeError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)