import prettytable
my_table=prettytable.PrettyTable(["Id","Name","Class"]);


m=int(input("enter the no: of rows: \n"))   
#n=int(input("enter the no: of columns: \n"))


#adding the row values i.e, students details
print("enter Name, Class")
for i in range(1,m+1):
 
    name=input("enter the name: ")
    cls=input("enter the class: ")
    my_table.add_row([i,name,cls])
    
print(my_table)

