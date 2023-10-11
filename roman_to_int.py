print("****Constraints : Values Valid from 0 upto 4999****\n")
print("                 ( Roman To Integer )              \n")

# USER - INPUT 
Q = input()

num_list = []
listq = []

# Dictionary & key values 
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Decrypts the the key values of roman characters 
def form_num_list(num_list):
   for i in range(Q.__len__()):
     num_list.append(roman[Q[i]])

# Main algorithm which does the work 
def conversion_algorithm():
  I=0
  tq=0
  while(I<(num_list.__len__())-1):
     if(num_list[I+1] > num_list[I]):
      tq = num_list[I+1] - num_list[I]
      if(tq%4 == 0 or tq%9 == 0 and tq!=num_list[I+1]/2):
                        num_list[I] = tq;
                        num_list[I+1] = 0;
     I+=1
     
# After going through the algorithm function, the dummy values assigned by the previous function are ignored & the values are added to new list
def converted_list(listqf):
   for i in range(num_list.__len__()):
       if(num_list[i] != 0):
            listqf.append(num_list[i])  

# Prints the sum of the values in the new list 
def add_values(lister):
       size = lister.__len__()
       sum = 0
       for i in range(size):
           sum+=lister[i]
       print(sum)

if __name__ == "__main__":
   form_num_list(num_list=num_list)
   conversion_algorithm()
   converted_list(listq)
   add_values(listq)


