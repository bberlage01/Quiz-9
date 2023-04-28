#Problem1
fin=open("mytextfile.txt","w")
line1="hello..\n"
line2="how are you...\n"
line3="I am good...\n"
line4="That is good...\n"
line5="Yes...\n"
fin.write(line1)
fin.write(line2)
fin.write(line3)
fin.write(line4)
fin.write(line5)

#Problem2
fin=open("mytextfile.txt")
for line in fin:
    print(line)
fin.close()
