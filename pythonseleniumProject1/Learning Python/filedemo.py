f = open("demo.txt", "a")
f.write("Hello1")
print("Write Task Done!!")
f = open("demo.txt", "r")
print(f.read())
f.close()
