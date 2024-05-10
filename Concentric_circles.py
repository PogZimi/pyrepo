import turtle 
import random 

print("Enter the no. of concentric circles you want : \n")
conc_circ = int(input())
print("Enter the base radius of first circle : \n")
radius = int(input())
print("The base radius will be increased by | radius | for each iteration/circle.\n")
print("Enjoy!")

# generates a list of size len such that 2 consecutive elements are not equal! It is required to avoid duplicate coloring.
def generate_unique_random_list(len):
    unique_list = []
    previous_value = None

    for x in range(len):
        current_value = random.randint(0, 2)  
        while current_value == previous_value:
            current_value = random.randint(0, 2)
        unique_list.append(current_value)
        previous_value = current_value

    return unique_list

def coloring(random):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    colors = [RED, GREEN, BLUE]
    return colors[random]

def remove_duplicating():
 pass 


t=turtle.Turtle()
t.shape("circle")
t.pencolor("black")
t.width(4)
random_list=[]
initial_pos=0
counter=0
R = generate_unique_random_list(conc_circ)

for i in range(conc_circ, 0, -1):         

    c=coloring(R[counter])
    t.color(c)    
    initial_pos=t.position()
    t.fillcolor(c)
    t.begin_fill()
    t.circle(radius*(i))
    t.end_fill()
    t.up()
    # Sets a new y-coordinate for a new circle
    t.sety(initial_pos[1]+((radius*(i))) - (radius*(i-1)))
    t.down()
    counter+=1

turtle.done()
