# ------------------------------Task 1-------------------------------------

diction = {'Shivam':80,'Amit':50,'Naveen':60,'Bilal':70,'Asif':90,'Imran':89,}

diction_input = input("Enter Student's name : ")

if diction_input in diction:
     print(f"{diction_input}'s marks: {diction[diction_input]}")
else:
    print("Student name not found in the records.")


# ------------------------------Task 2 ------------------------------------- 
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

extract = list_1[0:5]
print("Extracted elements:", extract)

extract.reverse()
print("Reversed extracted elements:", extract)


