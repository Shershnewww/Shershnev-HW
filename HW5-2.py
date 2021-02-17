Test_file_2 = open("Test_file_2.txt", "r")
content = Test_file_2.read()
print(f"Содержимое файла: \n {content}")

Test_file_2 = open("Test_file_2.txt", "r")
content = Test_file_2.readlines()
print(f"Количество строк в файле - {len(content)}")

Test_file_2 = open("Test_file_2.txt", "r")
content = Test_file_2.readlines()
for i in range(len(content)):
    print(f"Количество символов {i + 1} {len(content[i])}")

Test_file_2 = open("Test_file_2.txt", "r")
content = Test_file_2.read()
content = content.split()
print(f"Общее количество слов - {len(content)}")
Test_file_2.close()
