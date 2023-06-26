import matplotlib.pyplot as plt
import numpy as np
import math
import string
import sys

def menu():
  print("Welcome to the Mini Graphing Calculator\n")
  print("Select the type of graph you want to plot\n")
  print("1 - Straight Line (y = ax+b)\n")
  print("2 - Cosine (y = acos(bx)+c)\n")
  print("3 - Sine (y = asin(bx)+c)\n")
  print("4 - Tangent (y = atan(bx)+c)\n")

def check_graph_option(option): #check for user input, the user must enter 1, 2, 3 or 4 or empty string otherwise the program will not proceed. 
  graphs_options = ['1','2','3','4','']
  if option not in graphs_options:
    print("Oops, Enter a valid input.You have 4 options: 1, 2, 3 or 4. ")
    return sys.exit(-1)
    
def check_input(value): #check for the characters. The user must only enter numbers. 
  alphabet = list(string.ascii_letters) + list(string.punctuation)
  if value in alphabet:
    print("Oops, Enter a valid input. Please, enter a number. ")
    return sys.exit(-1) 
    
def x_axis(): #x_axis of the graphs 
  x = np.arange(-5, math.pi*2, 0.5 )  
  return x 
            
def straight_line_graph(a, b): #graphing straight_line 
  y_line = a*x_axis() + b
  return plt.plot(x_axis(), y_line, color='black', label='Straight Line')
  
def sine_graph(a,b,c): #graphing sine 
  y_sine = a*np.sin(b*x_axis())+c
  return plt.plot(x_axis(), y_sine, color='red', label='Sine')

def cos_graph(a, b, c): #graphing cos 
  y_cos = a*np.cos(b*x_axis())+c
  return plt.plot(x_axis(), y_cos, color='yellow', label='Cosine')

def tan_graph(a,b, c):#graphing tan 
  y_tan = a*np.tan(b*x_axis())+c
  return plt.plot(x_axis(), y_tan,   color='blue', label='Tangent')
  
def main():
  menu() #call the menu 
  done = True 
  all_graphs = [] # empty list to keep track of the graphs options selected by the user 
  graph_type = '1' #random initial value for graph type so that it's true at first
  graph_type__variables = []# empty list to store the graph type and variables a or b or c
  while done == True:
      while len(graph_type) != 0 and len(all_graphs) < 4: # user can select up to 4 graphs or if choice is an empty string it proceeds to plot the graphs selected by user
        graph_type = input("Choice:")
        check_input(graph_type)
        check_graph_option(graph_type)

        #user selects option 1
        #straight line graph values, slope and y intecept
        if graph_type == '1':
          straight_line = [] ##create a empty list to store values of a(amplitude), b(perido), and c
          all_graphs.append(graph_type)
          a = input("Enter value of a - slope:")
          check_input(a) #check whether it is not a string 
          b = input("Enter value of b - y_intercept:")
          check_input(b)
          #change the values to int for calculations  
          straight_line.append(int(graph_type))
          straight_line.append(int(a))
          straight_line.append(int(b))
          #add the list of cos values to the big list that keep all the values of different graphs selected by user.
          graph_type__variables.append(straight_line)

        #user selects option 2
        #cosine values
        if graph_type == '2':
          all_graphs.append(graph_type)
          cos = [] ##create a empty list to store values of a(amplitude), b(perido), and c
          a = input("Enter value of a (amplitude):")
          check_input(a)
          b  = input ("Enter value of b (period):")
          check_input(b)
          c = input("Enter value of c:")
          check_input(c)
          #convert the values to int for easy calculations 
          cos.append(int(graph_type))
          cos.append(int(a))
          cos.append(int(b))
          cos.append(int(c))
          #add the list of cos values to the big list that keep all the values of different graphs selected by user.
          graph_type__variables.append(cos)

        #user selects option 3
        #sine values 
        if graph_type == '3':
          all_graphs.append(graph_type)
          sine = [] #create a empty list to store values of a(amplitude), b(perido), and c
          #get the values from user 
          a = input("Enter value of a (amplitude):")
          check_input(a)
          b  = input ("Enter value of b (period):")
          check_input(b)
          c = input("Enter value of c:")
          check_input(c)
          #converts the values to int for easy calculations 
          sine.append(int(graph_type))
          sine.append(int(a))
          sine.append(int(b))
          sine.append(int(c))
           #add the list of sine values to the big list that keep all the values of different graphs selected by user.
          graph_type__variables.append(sine)
        #User selects option 4
        #tangent values 
        if graph_type == '4':
          all_graphs.append(graph_type)
          tan = [] #create a empty list to store values of a(amplitude), b(perido), and c
          #get the values from user 
          a = input("Enter value of a (amplitude):")
          check_input(a)
          b  = input ("Enter value of b (period):")
          check_input(b)
          c = input("Enter value of c:") 
          check_input(b)
          #add the values to the list 
          #change the values to integers for easy calculations 
          tan.append(int(graph_type))
          tan.append(int(a))
          tan.append(int(b))
          tan.append(int(c))
          #add the list of tan values to the big list that keep all the values of different graphs selected by user. 
          graph_type__variables.append(tan)
        done = True
      else: 
        #call the function to graph 
        done = False
        #get range of scale values from user
        print()
        print("Range of the scale of the y-axis:")
        min_y = int(input("Minimum value: "))
        max_y = int(input("Maximum value:"))
        
        print()
        print("Range of the scale of the x-axis:")
        min_x = int(input("Minimum value: "))
        max_x = int(input("Maximum value: "))

        #set the range of the x-axis
        plt.xlim(min_x, max_x)
        # Set the range of y-axis
        plt.ylim(min_y, max_y)

        #labels of the axis 
        plt.xlabel('Radians')
        plt.ylabel('Amplitude')

        #title for the program
        plt.title("Intro to Trigonometric Functions",fontsize=15, color= 'grey', fontweight="bold")

        #making a grid on the graph
        plt.grid()

        #print(graph_type__variables)
        #print the graphs the user selected at the shell
        print("You have selected the following graphs:")
        
        for i in all_graphs:
          if i == "1":
            print("Straight Line")
          if i == "2":
            print ("Cosine")
          if i == "3":
            print ("Sine")
          if i == "4":
            print("Tan")

        #plotting the graphs selected by the user. 
        for graph in graph_type__variables:
          if graph[0] == 1:
            #draw straight line 
            straight_line_a = graph[1]
            straight_line_b = graph[2]
            #print(straight_line_a,  straight_line_b)
            straight_line_graph( straight_line_a,  straight_line_b)
            
          if graph[0] == 2:
            #draw cosine 
            cos_a = graph[1]
            cos_b = graph[2]
            cos_c = graph[3]
            #print(cos_a, cos_b,cos_c)
            cos_graph(cos_a, cos_b, cos_c)

          if graph[0] == 3:
            #draw sine 
            sine_a = graph[1]
            sine_b = graph[2]
            sine_c = graph[3]
            #print(sine_a, sine_b, sine_c)
            sine_graph(sine_a, sine_b, sine_c)
  
          if graph[0] == 4:
            #draw tangent
            tan_a = graph[1]
            tan_b = graph[2]
            tan_c = graph[3]
            #print(tan_a, tan_b, tan_c)
            tan_graph(tan_a, tan_b, tan_c) 

        plt.legend()
        plt.show()
        
if __name__ == "__main__":
    main()
