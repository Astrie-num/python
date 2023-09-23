# file = input("Enter the name of the file: ")
# content = open(file)
# for words in content :
#     word = words.split()
# print(word)



#printing the file extension

filename = input("Enter the name of the file: ")
file_extension = filename.split(".")
print ("The extension of the file is : " + repr(file_extension[-1]))

