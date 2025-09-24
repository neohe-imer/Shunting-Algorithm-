input = "1 + 4 * 2 - 5"
print("INPUT", input)

precedence = {
    '*' : 3, 
    '/' : 3, 
    '+' : 2,
    '-' : 2
}

 ################################
   # Perform Shunting Algorith 
 ################################

output = []
opstack = []


for token in input.strip().split():
    if token in precedence:
        while len(opstack) > 0:
            op = opstack[-1] # get the operator at the top of the opstack 
            if precedence[token] > precedence[op]:
                break
            opstack.pop()
            output.append(op)
        opstack.append(token)
    else:
        output.append(token) # <--- push numbers directly to the output 

# Push the remaining operators form the opstack inot the output 
while len(opstack) > 0:
    output.append(opstack.pop())

print("POSTFIX (RMP):", ',' .join(output))

########################################
# Evaluate a list of elements (in postfix notation / RPN form)
########################################

result = []
for elem in output:
    if elem not in precedence:
        result.append(float(elem))
    else:
        right = result.pop()
        left = result.pop()
        if elem == '+':
            result.append(left + right)
        if elem == '-':
            result.append(left - right)
        if elem == '*':
            result.append(left * right)
        if elem == '/':
            result.append(left / right)

print("Result:", result.pop())