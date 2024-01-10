'''
We want to manufacture cars of type A and B. How many cars of each type to manufacture per day? 
Suppose we have three resources R1, R2, R3 that are needed to manufacture these cars. 
Car A needs 3 units of R1, 5 units of R2, and 1.5 units of R3 Car B needs 4 units of R1, 6 units of R2, and 3 units of R3. 
Maximum availability of resources per day is: R1 = 30, R2 = 60, R3 = 21 Each 
Car A sale contributes $30,000 to the profits, Car B contributes $45,000 to the profits 
How many cars should we manufacture each day of type A and type B?
'''

import pulp

#intantiate our problem class
model=pulp.LpProblem('Profit_maximising_problem',pulp.LpMaximize)
A=pulp.LpVariable('A',lowBound=0,cat='Integer')
B=pulp.LpVariable('B',lowBound=0,cat='Integer')

#Objective function
model+=30000*A+45000*B,"Profit"

#constrains
