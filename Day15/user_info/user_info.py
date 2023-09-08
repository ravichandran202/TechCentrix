import qrcode

print('---------USER PORTFOLIO---------')
name = input('Enter Name : ')
contact = input('Enter Contact : ')
email = input('Enter Email : ')
usn = input('Enter USN : ')
course = input('Enter Course : ')
clg_name = input('Enter College Name : ')

profile = (f'Name : {name}\nContact : {contact}\nEmail : {email}\nUSN : {usn}\nCourse : {course}\nCollege Name : {clg_name}')

generate = qrcode.make(profile)
generate.save(f'{name}_profile.png','png')