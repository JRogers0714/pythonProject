employee_file = open("Dudes.txt", "a")

employee_file.write("Erik withakay")   # adds a line to the end
employee_file.write("\nSteve")   # \n is an escape character


employee_file.close()

employee_file = open("MoarDudes.txt", "w")

employee_file.write("\nSteve")   # overwrites the whole file can also create new file

employee_file.close()

fak_website = open("index.html", "w")

employee_file.write("<p>ksjbdflbfljhbsdfljsbhdf</p>")   # overwrites the whole file can also create new file

employee_file.close()


