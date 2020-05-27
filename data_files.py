with open("myfile.txt","w") as file:
    file.write("this is my file")
with open("myfile.txt","r") as file:
    content = file.read()
    print(content)
with open("myfile.txt","w+") as file:
    file.write("Starting again")
    file.seek(0)
    print(file.read())
