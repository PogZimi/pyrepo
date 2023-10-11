import sys 
import random 

max_len = 26
min_len = 18
pass_len = 1

# Password ELEMENTS 
special_chars = ['@','!','#','*', '&','$']
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','x','y','z','w']
numbers = [0,1,2,3,4,5,6,7,8,9]
# CONVERTING numbers's items into str() type 
num = [str(item) for item in numbers]

# for storing generated password 
password = ''
# For Choosing Whether special_chars, alphabets or numbers should be used during each iteration 
xr = 0
# For choosing random value from the elements 
yr = 0

pass_list = [special_chars, alphabets, num]

print("Press 1 for max_length and 2 for min_length : ")
choice = int(input())

if(choice == 1):
     pass_len=max_len
elif(choice == 2):
     pass_len=min_len
else: 
     sys.exit() # exits the program 

for i in range(pass_len):
      xr =random.randint(0,2)
      yr =random.randint(0, len(pass_list[xr]) - 1 )
      password += pass_list[xr][yr]
     

print(f" {password} is your password !!! \n")
