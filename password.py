def auth_password(password):
  has_letter=0
  has_num=0  
  for i in password:
        if i.isalnum():
            if i.isalpha():
               has_letter=has_letter+1
            if i.isnumeric():
              has_num+=1
        else:
         return False
  if has_letter and has_num:                
      return True
  else:
      return False
  
while True:
    phone=input("enter the phone number(10 digits , numbers only):")
    if len(phone)==10 and phone.isdigit():
       print("valid phone number")
       break
    else:
       print("invalid phone number")
while True:
    password=input("enter the password(which includes letters ,characters and numbers)") 
    if len(password)>=8 and auth_password(password):
        print("valid password")
        break
    else:
        print("invalid password")          
