

name = input('enter name ')
surname = input('enter surname ')
year = int(input('enter year '))
city = input('enter city ')
email = input('enter email ')
telephone = input('input telephone ')

def func(name, surname, year, city, email, telephone):
   print(f"name - {name}; surname - {surname};  year - {year}; city - {city}; email - {email}; telephone - {telephone}")
func(name= 'Anton', surname= 'Shershnev', year= '33', city= 'Moscow', email= 'true@mail.ru', telephone= '200-200-2')