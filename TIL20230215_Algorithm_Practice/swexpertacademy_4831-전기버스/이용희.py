import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    k, n, m = map(int, input().split())
    charge_list = list(map(int, input().split()))
    bus_now = 0
    charge_count = 0
    charge_check = 0
    while True:
        station_list = []
        for station in range(bus_now + 1, bus_now + k + 1):
            station_list.append(station)
        if n in station_list:
            print(f'#{test_case} {charge_count}')
            break
        else:
            for station in station_list:
                for charge in charge_list:
                    if station == charge:
                        bus_now = charge
                        charge_check = 1
            if charge_check != 0:
                charge_count += 1
                charge_check = 0
            else:
                print(f'#{test_case} {0}')
                break
