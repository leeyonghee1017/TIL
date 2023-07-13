command = "GRGRGRB"
x = 0
y = 0
head = 0
answer = []
for c in command:
    if c == 'R':
        head = (head + 1) % 4
    elif c == 'L':
        head = (head - 1) % 4
    elif c == 'G':
        if head == 0:
            y += 1
        elif head == 1:
            x += 1
        elif head == 2:
            y -= 1
        else:
            x -= 1
    else:
        if head == 0:
            y -= 1
        elif head == 1:
            x -= 1
        elif head == 2:
            y += 1
        else:
            x += 1
    print(x, y)
answer.append(x)
answer.append(y)

print(answer)

