fw = open("sample.txt", "w") #Create sample.txt, and write it
fw.write("You can write things here\n")
fw.write("Even more things")
fw.close()

fr = open("sample.txt", 'r') #Read sample.txt
text = fr.read()
print(text) #Prints it out in dev console
fr.close()

#Note: Items deleted in this file were deleted to reduce clutter; rerun file to create it again