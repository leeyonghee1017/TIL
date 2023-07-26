from collections import deque
total, trade = map(int, input().split())

reservation_list = deque()
for _ in range(trade):
    trade_val = input().split()
    if trade_val[0] == 'deposit':
        total += int(trade_val[1])
        while reservation_list and reservation_list[0] <= total:
            total -= reservation_list[0]
            reservation_list.popleft()
    elif trade_val[0] == 'pay':
        if total >= int(trade_val[1]):
            total -= int(trade_val[1])
    else:
        if not reservation_list and total >= int(trade_val[1]):
            total -= int(trade_val[1])
        else:
            reservation_list.append(int(trade_val[1]))
print(total)