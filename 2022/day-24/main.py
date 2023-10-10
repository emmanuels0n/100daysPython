# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:   # The same as before but no need to close it
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="w") as file:  # To write over the file. To just append something mode="a"
    file.write("new text.")

with open("new_file.txt", mode="w") as file:  # I can create a new file like this
    file.write("new text.")
