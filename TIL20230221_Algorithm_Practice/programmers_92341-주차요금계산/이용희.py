import math


def solution(fees, records):
    parking_dic = {}  # 주차된 차량을 저장할 딕셔너리
    fee_dic = {}  # 출차 될때 주차한 시간을 저장할 딕셔너리
    for record in records:

        h_s, car_num, in_out = record.split()  # 시간, 차량번호, in out을 각 변수에 저장
        if in_out == "IN":  # in_out이 "IN" 일 경우
            parking_dic[str(car_num)] = h_s  # 딕셔너리에 차량 번호를 키값으로 주차된 시간을 저장
            if car_num not in fee_dic:  # 만약 오늘 처음 들어온 차량이면
                fee_dic[str(car_num)] = 0  # 주차된 시간을 0으로 초기화
        else:  # in_out 이 "OUT" 일 경우
            charge_h_s = parking_dic[str(car_num)].split(':')  # 딕셔너리에 저장되어있는 차량이 입고된 시간을 ':' 로 구분
            start_time = int(charge_h_s[0]) * 60 + int(charge_h_s[1])  # 입고된 시간 계산
            end_time_split = h_s.split(':')  # 출차되는 시간을 ':'로 구분
            end_time = int(end_time_split[0]) * 60 + int(end_time_split[1])  # 출차된 시간 계산
            fee_dic[str(car_num)] += (end_time - start_time)  # 총 시간을 딕셔너리에 더한다
            del parking_dic[str(car_num)]  # 차량이 나갔으므로 딕셔너리에서 삭제

    if parking_dic:  # records가 다 돌았음에도 주차된 차가 남아있다면
        for car_num in parking_dic.keys():
            charge_h_s = parking_dic[car_num].split(':')  # 딕셔너리에 저장되어있는 차량이 입고된 시간을 ':' 로 구분
            start_time = int(charge_h_s[0]) * 60 + int(charge_h_s[1])  # 입고된 시간 계산
            end_time = 23 * 60 + 59  # 출고된 시간은 23:59로 고정
            fee_dic[str(car_num)] += (end_time - start_time)  # 총 시간을 딕셔너리에 더한다
        del parking_dic[str(car_num)]  # 차량이 나갔으므로 딕셔너리에서 삭제

    cal_fee = []  # 요금을 저장할 리스트
    for car_num in sorted(fee_dic):  # 시간이 저장된 리스트의 키값을 작은 것 부터 순환
        if fee_dic[car_num] <= fees[0]:  # 저장된 시간에 기본 시간보다 작다면
            cal_fee.append(fees[1])  # 기본요금을 저장
        else:  # 저장된 시간이 기본시간보다 크다면
            cal_fee.append(fees[1] + (math.ceil((fee_dic[car_num] - fees[0]) / fees[2])) * fees[3])  # 요금을 계산하여 저장
    print(cal_fee)


solution([180, 5000, 10, 600],
         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
          "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
