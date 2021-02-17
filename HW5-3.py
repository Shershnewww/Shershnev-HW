with open("Test_file_3_salary.txt", "r") as my_file:
    salary = []
    min_sal = []
    my_list = my_file.read().split("\n")
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           min_sal.append(i[0])
        salary.append(i[1])
print(f"Оклад меньше 20.000 {min_sal}")
print(f"Cредний оклад {sum(map(int, salary)) / len(salary)}")

