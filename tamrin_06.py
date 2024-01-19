n1 = "tamrin_06f.txt"
file = open(n1,"r")
x = file.read()
file.close()
file = open(n1,"a")
file.write(x)
file.close()