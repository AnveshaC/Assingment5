classA={"Anvesha":99 ,"Arjun":66,"Krishna":62,"Pranjal":88,"Varada":90}
a=str(input("Enter a students name:"))
if a in classA:
    print("{}'s marks :".format(a) , classA[a])
else:
    print("Student not found")





