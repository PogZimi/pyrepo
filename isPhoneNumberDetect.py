'Tells whether a phone number given in the data is a valid American Phone Number or not.'


'''
For example :
'Call me at 415-555-1011 tomorrow. 415-555-9999 is my residence\'s phoneNo . My Businnes\'s Phone Number is 415-462-2999.'

The first 3 digits signify the area code of a particular area/region in the North American Countries
415 is area code of San Fransisco , California. 
415-555-1011, 415-555-9999 & 415-462-2999 are American Phone Numbers .

'''

print("AmericanPhoneNumberFormat : **ABC-DEF-GHIJ** where AB\n")

print("Enter the first-3-digits of your Area Code (In the UnitedStates) : \n")
AREA_CODE = input()
print("Enter the name of your Area : \n")
AREA_NAME = input()
print("Enter a message containing a Phone Number/Numbers : \n")
message1 = input()


#Sample
#message1 = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my residence\'s phoneNo . My Businnes\'s Phone Number is 415-462-2999.'
phone_numbers_fetched = []

def PhoneNumberPattern(message):
    
    sample = ''
    i=0
    hyphen_index=None 
    hyphen_count=message.count('-')

    #print(f"Hyphen Count : {hyphen_count}\n\n")
    while i < hyphen_count//2 :
      hyphen_index = message.index('-')
      #print(f"i : {i}\n")
      #print(f"Hyphen_Index : {hyphen_index}\n")
      
      if('-' in message and message[message.index('-')+1]  and message[message.index('-')-1]):
           sample = message[hyphen_index-3 : hyphen_index+9]
           #print(f"sample : {sample}\n")
           if(len(sample) == 12):
                phone_numbers_fetched.append(sample)
           
           message = message[:hyphen_index-3] + message[hyphen_index+10:]
           #print(f"message : {message}\n")
      
      i+=1

def isPhoneNumber(phoneNo):
  bin = None 

  if(len(phoneNo) == 12):
   if('-' in phoneNo):
        if(phoneNo.count('-') == 2):
             if phoneNo[3]=='-' and phoneNo[7]=='-':
                 if phoneNo[0]==AREA_CODE[0] and  phoneNo[1]==AREA_CODE[1] and phoneNo[2]==AREA_CODE[2]:
                    bin = 1
                 else:
                    bin = 0
   else:
    bin = None 
   if(bin==1):bin=True 
   else:bin=False 

   return bin

def isPhoneNumberStatus(phone_nos):
    format_status = None 
    for item in phone_nos:
        format_status=isPhoneNumber(item)
        print(f"{item} is a American phone number of {AREA_NAME}  : {format_status}\n")


print(f"Data : {message1} \n\n")
print("Results : \n")
PhoneNumberPattern(message1)
isPhoneNumberStatus(phone_numbers_fetched)
