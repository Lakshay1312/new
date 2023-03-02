print("Name: Lakshay")
print("Enrollment No.: BT20HCS125")

length=50
path=input('Enter the grammar : ')
lhs=path[0]
f= path[3:]
rhs=f.split('|')
grammer={lhs: rhs}

def match(a,b,la,lb):
    if la==0 or lb==0:
        return 0;
    elif a[la-1]==b[lb-1]:
        return 1 + match(a,b,la-1,lb-1);
    else:
        return max(match(a,b,la,lb-1), match(a,b,la-1,lb));

for key in grammer.copy():
    val=grammer[key]
    for i in range(0,len(val) - 1):
        for j in range(i,len(val)):
            if i!=j:
                l=match(val[i],val[j],len(val[i]),len(val[j]))
                if l>0:
                    if length>l:
                        length=l
eq2=[]
if length>0:
    com_val=grammer[key][0][:length]
    for i in range(len(grammer[key])):
        if com_val in grammer[key][i]:
            grammer[key][i]=grammer[key][i][length:]
            eq2.append(grammer[key][i])
            grammer[key][i]=''

eq1=grammer[key]
for i in range(len(eq1)):
    if '' in eq1:
        eq1.remove('')
eq1.append(com_val+lhs+"'")

for i in eq2:
    if i=='':
        ind=eq2.index(i)
        eq2[ind]='ε'

print(" ")
print("Output after left factoring is: ")
print(" ")
fun1=lhs+'-> '
for i in eq1:
    fun1+=i+'|'
fun1=fun1[:-1]
print(fun1)

fun2=lhs+''''-> '''
for i in eq2:
    fun2+=i+'|'
fun2=fun2[:-1]
print(fun2)


