input_count = 8
input_pwd = 'a1b2c3e4'

result = ''
for i in range(0,len(input_pwd),2):
    change_num = ord(input_pwd[i]) + (int(input_pwd[i+1]) * int(input_pwd[i+1]))
    while True:        
        if change_num >= 123:
            change_num -= 26
        else:
            break
    result += chr(change_num)

print(result)