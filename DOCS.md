 # Documentation
### Due: Sunday December 18 at 4:00 PM

This file will contain your project Documentation. Fill out the relevant sections to document your code.

## Summary
#### Briefly describe your program and what it does.
It plots four different graphs, straight line (linear function), cosine, sine and tangent. The user selects the graphs they want to plot. They can select up to four graphs or enter an empty string whenever they reach the number of graphs they want to plot.

## Main File
#### What is the "main" file for your program, i.e. what should I run first?
mini_graphing_calculator.py

## Example Usage
#### Provide examples of how the user should run your program.
Example 1: Selected 2 Graphs.
    Choice:1
    Enter value of a - slope:2
    Enter value of b - y_intercept:3
    Choice:2
    Enter value of a (amplitude):2
    Enter value of b (period):1
    Enter value of c:0
    Choice: (Empty string)
    
    Range of the scale of the y-axis:
    Minimum value: -2
    Maximum value:10
    
    Range of the scale of the x-axis:
    Minimum value: -5
    Maximum value: 20
    
    Output:
        You have selected the following graphs:
        Straight Line
        Cosine
        see example_output_1.png for the output produced. 

Example 2: Selected 4 Graphs
    Choice:1 
    Enter value of a - slope:2
    Enter value of b - y_intercept:3
    Choice:2
    Enter value of a (amplitude):1
    Enter value of b (period):1
    Enter value of c:0
    Choice:3
    Enter value of a (amplitude):5
    Enter value of b (period):1
    Enter value of c:3
    Choice:4
    Enter value of a (amplitude):1
    Enter value of b (period):1
    Enter value of c:0
    
    Range of the scale of the y-axis:
    Minimum value: -3
    Maximum value:15
    
    Range of the scale of the x-axis:
    Minimum value: -4
    Maximum value: 25
    Output: 
      You have selected the following graphs:
      Straight Line
      Cosine
      Sine
      Tan
      see example_output_2.png for output produced. 

## Input
#### Describe any input(s) required from the user.
User selects graphs they want to plot. They have 4 options: straight line, cosine, sine or tangent. The graphs are selected in any order. After selecting the graph, the user enters values, a, b, or c, of each graph they want to plot for. 
For straight line, the user enters the slope(gradient) and the y-intercept, y = ax+b, a = slope and b = y intercept.
For the trigonometric functions, the user will enter values: a, b and c. The equations are defined as below: 
1. y = acos(bx)+c
2. y = asin(bx)+c
3. y = atan(bx)+c
   a = relates to amplitude
   b = period of the curve
   c = translating the graph and it also affects the period.
Lastly, the user also has to enter minimum and maximum values of both y-axs and x-axis.
All the values of a, b, or c  and  values of the axis must be numerical values. It takes either positive or negative. It does not take characters. 
   
## Output
#### Describe any output(s) produced by your program.
Example of output from example 1 in example usage: see example_output_1.png

Example of output from example 2 in example usage: see example_output_2.png

It plots all the graphs that user selects. Each graph has each specific color. Check for the color - graph key at the right corner.

## Known Issues
#### Describe any known bugs, including workarounds to keep your program running.

