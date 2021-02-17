Test_file_1 = open("Test_file_1.txt", "w")
line = input("Введите текст \n")
while line:
    Test_file_1.writelines(line)
    line = input("Введите текст \n")
    if not line:
        break

Test_file_1.close()
Test_file_1 = open("Test_file_1.txt", "r")
content = Test_file_1.readlines()
print(content)
Test_file_1.close()
