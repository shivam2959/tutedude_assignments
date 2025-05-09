# -------------------------------Task1---------------------------------------------


try:

    file_1 = open('sample.txt', 'r')
    #reading_files = file_1.readlines()
    #print(file_1)

    for line in file_1:
        print(line.strip())

    file_1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An Unexpected Error Occured : {e}")    


# ----------------------------------Task2--------------------------------------------


user_input = input("Enter some text to write to the file: ")

file = open("output.txt", "w")
file.write(user_input + "\n")
file.close()
print("Initial input written to output.txt")

additional_input = input("Enter additional text to append to the file: ")

file = open("output.txt", "a")
file.write(additional_input + "\n")
file.close()
print("Additional input appended to output.txt")

print("\nFinal content of output.txt:")
try:

    file_2 = open('output.txt', 'r')
    #reading_files = file_1.readlines()
    #print(file_1)

    for line in file_2:
        print(line.strip())

    file_2.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An Unexpected Error Occured : {e}") 
