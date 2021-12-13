Title=input("Enter the name of platform : ")
Email=input("What email did you used there : ")
UserName=input("What Username did you used there :")
Password=input("What was the password: ")

if __name__== "__main__":
    file=open(Title + ".txt", "a")
    file.write("Platform:" + Title +"\n")
    file.write("E-Mail Address:" +Email+ "\n")
    file.write("Username:" +UserName+"\n")
    file.write("Password:" +Password+"\n")
    file.write("\n")
