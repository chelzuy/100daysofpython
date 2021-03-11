# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# #Reading on the file
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)


# #Write on the file where the file text will be replaced by "new here", mode is "w"
# with open("my_file.txt", mode= "w") as file:
#     file.write("new here")

#Write on file where the text will instead be appended on the file, mode is "a"
with open("my_file.txt", mode="a") as file:
    file.write("\nNew here")







































