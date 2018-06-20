# Truth-Table-Generator
This is a Truth Table Generator made for my Topics in Logic Class. Use this to analyze the validity of logical arguments.

How it works:
A logical argument is considered "valid" if the conclusion is never false while the premises are true. 
If the conclusion is true no matter what, it is considered "Trivially Valid."
Keep in mind, a logical argument can be valid even if the premises are false. Then it would be valid but not sound.
This program takes every possible True/False combination of the variables given to it and uses the about rules to check each premise
and conclusion that follows to determine whether or not the argument is valid.
If the argument is invalid, the program will point out the instances where the argument does not hold up.

Read up more about Truth tables and their use here: https://en.wikipedia.org/wiki/Truth_table

Operations are as follows:

\> : implies (Ex: P>Q    "P implies Q")
& : and (Ex: P&Q    "both P and Q are true")
v : or (Ex: PvQ    "either P or Q is true")
- : not (Ex: -P    "not P")

Example Premises and Conclusions:

-Valid Argument

A = Alice goes to party
B = Betsy goes to party
C = Carol goes to party

If Alice or Betsy goes to the party, Carol will go to the party.                    (A v B) > C
If Alice does not go to the party, Carol will not go to the party.                  -A > -C

Therefore:
If Betsy goes to the party, Alice will go to the party.                              B > A

Generated Table

A B C | (AvB)>C | -A>-C | B>A 
------|---------|-------|-----
T T T |    T    |   T   |  T  
T T F |    F    |   T   |  T  
T F T |    T    |   T   |  T  
T F F |    F    |   T   |  T  
F T T |    T    |   F   |  F  
F T F |    F    |   T   |  F  
F F T |    T    |   F   |  T  
F F F |    T    |   T   |  T  
                              
Valid!                        


-Invalid Argument

P = Penny wins the race
Q = Quinton is happy
R = Rudy is happy
S = Sarah wins the race

If Penny wins the race, Quinton is not happy.                      P > -Q
If Rudy is happy, Sarah didn't win the race.                       R > -S
If Sarah is not happy, Penny did not win the race.                 -S > -P

Therefore:
If Rudy is happy, Quinton is happy.                                R > Q

P Q R S | P>-Q | R>-S | -S>-P | R>Q
--------|------|------|-------|-----
T T T T |   F  |   F  |   T   |  T
T T T F |   F  |   T  |   F   |  T
T T F T |   F  |   T  |   T   |  T
T T F F |   F  |   T  |   F   |  T
T F T T |   T  |   F  |   T   |  F
T F T F |   T  |   T  |   F   |  F
T F F T |   T  |   T  |   T   |  T
T F F F |   T  |   T  |   F   |  T
F T T T |   T  |   F  |   T   |  T
F T T F |   T  |   T  |   T   |  T
F T F T |   T  |   T  |   T   |  T
F T F F |   T  |   T  |   T   |  T
F F T T |   T  |   F  |   T   |  F
F F T F |   T  |   T  |   T   |  F  <---
F F F T |   T  |   T  |   T   |  T
F F F F |   T  |   T  |   T   |  T

Invalid!

As you can see, the argument fails when Penny doesn't win the race, Quinton is unhappy, Rudy is happy, and Sarah doesn't win the race.
