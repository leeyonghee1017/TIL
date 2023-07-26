command, stack = map(int, input().split())
list_stack = []
result=[]
for _ in range(command):  
    command_val = input().split()
    
    if len(list_stack) == stack and command_val[0] == 'push':
        result.append('Overflow')
        continue
    elif len(list_stack) == 0 and command_val[0] == 'pop':
        result.append('Underflow')
        continue

    if command_val[0] == 'push':
        list_stack.append(command_val[1])       
    elif command_val[0] == 'pop':
        result.append(list_stack[len(list_stack) - 1])
        list_stack.pop()

for i in range(len(result)):
    print(result[i])