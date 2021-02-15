note4u = open("C:\\Users\\User\\Desktop\\note4u.txt","r")
a = note4u.read()
print(a)

newfile = open("C:\\Users\\User\\Desktop\\newfile.txt", "w")
newfile.write(a)

note4u.close()
newfile.close()

newfile = open("C:\\Users\\User\\Desktop\\newfile.txt", "r")
b = newfile.read()
print(b)

newfile.close()
