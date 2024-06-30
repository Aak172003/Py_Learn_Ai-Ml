# Give a second chance , if mail id correct but password is incorrect

email = input('enter email')
password = input('enter password')

if email == 'nitish.campusx@gmail.com' and password == '1234':
  print('Welcome')

elif email == 'nitish.campusx@gmail.com' and password != '1234':

  # tell the user

  print('Incorrect password')

  password = input('enter password again')

  if password == '1234':
    print('Welcome,finally!')
  else:
    print('beta tumse na ho paayega!')
else:
  print('Not correct')