# 1) Takes input 8 times from user & stores it inside a list
# 2) It Detects if any number is repeated & how many times the n numbers has been repeated in the list
# 3) If you want the number of inputs to be increased , change the list_size to whatever no. of inputs you want

# ----------------------[Variables & List]------------------------------

list1 = [] 
list_size = 8  # You can change this, currently it takes input 8 times
list_elements = 0
i = 0 
j = i + 1

# -----------------------------------------------------------------------

def inner_core():
 for i in range(list_size):
         list_elements = input(f"Enter the list element[{i+1}] :  \n")
         int(list_elements)
         list1.append(list_elements)

def outer_core():
         k = 0;
         r = 0;
         for i in range(list_size):
           for j in range(list_size - 1):
                if(list1[i] == list1[j]): 
                        k = k + 1
                else:
                        pass; 
         print(f"Detected repeated numbers in List : {k-7} times\n")

inner_core();
outer_core();
