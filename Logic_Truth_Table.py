print()
print()

#loop allows for resetting
again = True
while again == True:

#asks for premises and conclusion
    statements = []

    prem_num = input("How many premises?")
    print()
    num_ok = False
    while num_ok == False:
        try:
            prem_num = int(prem_num)
            if type(prem_num) is int:
                num_ok = True
        except ValueError:
            prem_num = input("Please enter an integer: ")
            print()

    for i in range(int(prem_num)):
        user = input("Premise #" + str(i+1) + ": ")
        if user != '':
            statements.append([i for i in user])
        else:
            premise = False
    print()
    statements.append(input("Conclusion: "))


    operators = ['(',')','-','&','v','>']

# Figure out the variables
    var = []
    for state in statements:
        for i in state:
            if (i not in operators 
                    and i not in var 
                    and i != ' '):
                var.append(i)

#All possible T/F combinations

    lines = 2**(len(var))

    possible = []
    for row in range(lines):
        var_case = {}
        for column in range(len(var)):
            if row % 2**(len(var) - column) < 2**((len(var)-(column + 1))):
                var_case[var[column]] = "T"
            else:
                var_case[var[column]] = "F"
        possible.append(var_case) 



#rules
    def imply_result(a,b):
        if a == "T" and b == "T":
                return "T"
        if a == "T" and b == "F":
                return "F"
        if a == "F" and b == "T":
                return "T"
        if a == "F" and b == "F":
                return "T"
            

    def and_result(a,b):
        if a == "T" and b == "T":
                return "T"
        if a == "T" and b == "F":
                return "F"
        if a == "F" and b == "T":
                return "F"
        if a == "F" and b == "F":
                return "F"


    def or_result(a,b):
        if a == "T" and b == "T":
                return "T"
        if a == "T" and b == "F":
                return "T"
        if a == "F" and b == "T":
                return "T"
        if a == "F" and b == "F":
                return "F"

    def not_result(a):
        if a == "T":
                return "F"
        if a == "F":
                return "T"

#substitutes True/False values for each case

    def substitute(a, num):
        a = [possible[num][i] if i in var else i if i in operators else ' ' for i in a]
        return [i for i in a if i != ' ']

#parses out a statement into a tree structure

    def parser(a):
        b = []

#Find Top Layer of Tree

        total = len([c for c in a if c in ["(", ")"]])
        tree_top = len(a)
        if any(o in a for o in [">","&","v"]):
            for i in range(len(a)):
                if a[i] in [">","&","v"]:
                    front = len([c for c in a[0:i] if c == "("])
                    back = len([c for c in a[i:] if c == ")"])
                    if front + back <= total:
                        total = front + back
                        tree_top = i
        elif len(a) > 0:
            b.append(a[-1])
            b.append(a[0:-1])
            return b
        else:
            return ''


#recursively adds to tree

        tree = []
        n = []
        if (len([c for c in a[0:tree_top] if c == "("]) > 
            len([c for c in a[0:tree_top] if c == ")"])):
            x = a[a.index("(")+1:tree_top]
            y = a[tree_top+1:-1]
            n = a[0:a.index("(")]
        else:
            x = a[0:tree_top]
            y = a[tree_top+1:]
        b.append([a[tree_top], n])
        b.append(parser(x))
        b.append(parser(y))

        return b



#applies rules on the tree to return one value
    def get_result(a):
        if len(a) > 0:
            if a[0][0] == ">":
                b = imply_result(get_result(a[1]),get_result(a[2]))
                if len(a[0][1]) % 2 == 1:
                    b = not_result(b)
            elif a[0][0] == "&":
                b = and_result(get_result(a[1]),get_result(a[2]))
                if len(a[0][1]) % 2 == 1:
                    b = not_result(b)
            elif a[0][0] == "v":
                b = or_result(get_result(a[1]),get_result(a[2]))
                if len(a[0][1]) % 2 == 1:
                    b = not_result(b)
            else:
                b = a[0]
                if len(a[1]) % 2 == 1:
                    b = not_result(b)
        else:
            b = ''
        return b

    def solver(a, num):
        return get_result(parser(substitute(a, num)))

#centers result in column
    def center(a, length):
        beg = True
        if length == 0:
            return [""]
        while len(a) != length:
            if beg == True:
                a.insert(0," ")
            else:
                a.append(" ")
            beg = not beg
        return a 

#prints table
    def table(a):
        triv = True
        print()
        print()

#first line

        for i in var:
            print(i, end = " ")

        for i in statements:
            if i != '':
                print("|", end = " ")

                print("".join(i), end = " ")

        print()

#second line
        for i in range(len(var)):
            print("--", end = "")

        for state in statements:
            if state != '':
                print("|", end = "")
                for i in range(len(state)+2):
                    print("-", end = "")
          
        print()

#meat of table
        for case in possible:

            for c in case:
                    print(case[c], end = " ")

            results = []
            
            for state in statements:
                results.append(solver(state, possible.index(case)))
                if state != "":
                    print("|", end = " ")
                print("".join(center([solver(state, possible.index(case))], len(state))), end = " ")
            
            if results[-1] == "F":
                triv = False

            if (results[-1] == "F" and 
            results[:-1] == ["T" for i in results[:-1]]):
                a = False
                print("<---", end = "")

            elif results[-1] == '':
                a = ''
                
            print()

        return a, triv


    try:
        a = True
        a = table(a)

        if a[1]:
            print()
            print("Trivially Valid!")
            print()
        elif a[0]:
            print()
            print("Valid!")
            print()
        elif a[0] == False:
            print()
            print("Invalid!")
            print()
        else:
            print()

    except TypeError:
        print()
        print()
        print("Input Error :(")
        print()

        
#for testing
#print([solver(statement[0],1])

#allows retries
    reset = False
    while reset == False:
        retry = input("Again? (y/n): ")
        if retry == 'y':
            print()
            print()
            reset = True
        elif retry == 'n':
            again = False
            reset = True
        else:
            None
                
