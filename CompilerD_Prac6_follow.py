import sys
sys.setrecursionlimit(60)

def myfirst(str):
    first_1 = set()
    if str in non_terminals:
        rules = productions_dict[str]

        for rule in rules:
            first_2 = myfirst(rule)
            first_1 = first_1 |first_2

    elif str in word:
        first_1 = {str}

    elif str== '' or str== '@':
        first_1 = {'@'}

    else:
        first_2 = myfirst(str[0])
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                #print("inside while")

                first_1 = first_1 | (first_2 - {'@'})
                #print('string[i:]=', string[i:])
                if str[i:] in word:
                    first_1 = first_1 | {str[i:]}
                    break
                elif str[i:] == '':
                    first_1 = first_1 | {'@'}
                    break
                first_2 = myfirst(str[i:])
                first_1 = first_1 | first_2 - {'@'}
                i += 1
        else:
            first_1 = first_1 | first_2

    return  first_1


def myfollow(nT):

    follow_1 = set()

    prods = productions_dict.items()
    if nT==starting_symbol:
        follow_1 = follow_1 | {'$'}
    for nt,rhs in prods:
        #print("nt to rhs", nt,rhs)
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_1 = follow_1 | myfollow(nt)
                    else:
                        follow_2 = myfirst(following_str)
                        if '@' in follow_2:
                            follow_1 = follow_1 | follow_2-{'@'}
                            follow_1 = follow_1 | myfollow(nt)
                        else:
                            follow_1 = follow_1 | follow_2
    return follow_1

no_of_terminals=int(input("Enter no. of terminals: "))
word = []
print("Enter the terminals :")
for _ in range(no_of_terminals):
    word.append(input())
no_of_non_terminals=int(input("Enter no. of non terminals: "))
non_terminals = []

print("Enter the non terminals :")
for _ in range(no_of_non_terminals):
    non_terminals.append(input())

starting_symbol = input("Enter the starting symbol: ")

no_of_productions = int(input("Enter no of productions: "))

productions = []

print("Enter the productions:")
for _ in range(no_of_productions):
    productions.append(input())

productions_dict = {}

for nT in non_terminals:
    productions_dict[nT] = []

for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

FIRST = {}
FOLLOW = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | myfirst(non_terminal)

FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | myfollow(non_terminal)

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal])))