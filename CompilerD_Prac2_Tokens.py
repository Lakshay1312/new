print("Nimit Singhal")
print("BT20HCS193")

Keyword = ["int", "if", "then", "else", "endif","print"]
DataTypes = ["int", "float", "char", "bool"]
Operator = ["=", "==", "+", "++", "+=", "-", "--", "-=", "!=", ">>", "=>", ">", "<<", "=<", "<", "*", "/", "%"]
Special_Symbols = ["(", ")", "{", "}", "[", "]", ":", ";", ",", "."]

program = open('C:/Users/laksh/Desktop/Random.txt', 'r')

variable = set()
operator = set()
keyword = set()
specialsymbols = set()
constant = set()
for line in program:
    for word in line.split():
        if word in Keyword or word in DataTypes:  # Keyword
            keyword.add(word)
        if word in Operator:        # Operator
            operator.add(word)
        if word in Special_Symbols:  # Special Symbols
            specialsymbols.add(word)
        if word.lstrip('-').isdigit():           # Constants
            constant.add(word)
program.seek(0)
for line in program:
    if "int" in line:
        if "main()" not in line:
            for word in line.split(" "):
                if word in DataTypes:
                    pass
                elif word == ",":
                    pass
                else:
                    if word not in operator:  # Variable
                            if word != '' and word != ';\n' and word != '\n' and word not in Special_Symbols and word not in Keyword:  # Variables
                                variable.add(word)

program.seek(0)
program.close()

print("Variables", variable)
print("Operators", operator)
print("Constants", constant)
print("Keywords", keyword)
print("Special Symbols", specialsymbols)
