
def triangle(a,b,c):
    if a < 1 or a > 1000:
        return "a不在取值范围内"
    if b < 1 or b > 1000:
        return "b不在取值范围内"
    if c < 1 or c > 1000:
        return "c不在取值范围内"
    
    if a + b <= c or a + c <= b or b + c <= a:
        return "不能构成三角形"
    
    if a == b == c:
        return "等边三角形"
    elif a == b or a == c or b == c:
        return "等腰三角形"
    else:
        return "普通三角形"


def calendar(y,m,d):
    if y < 1900 or y > 2100:
        return "年份不在取值范围内"
    
    # 判断是否为闰年
    is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 闰年二月有29天
    if is_leap:
        days_in_month[1] = 29
    
    if m < 1 or m > 12:
        return "月份不在取值范围内"
    
    if d < 1 or d > days_in_month[m - 1]:
        return "日期不在取值范围内"
    
    d += 1
    if d > days_in_month[m - 1]:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1

    return f"{y}-{m:02d}-{d:02d}"


def computer(hosts, monitors, peripherals):
    if hosts < 1 or hosts > 70:
        return "主机的销售数量不在取值范围内（1-70）"
    if monitors < 1 or monitors > 80:
        return "显示器的销售数量不在取值范围内（1-80）"
    if peripherals < 1 or peripherals > 90:
        return "外设的销售数量不在取值范围内（1-90）"

    total_sales = hosts * 25 + monitors * 30 + peripherals * 45
    
    if total_sales <= 1000:
        commission = total_sales * 0.10
    elif total_sales <= 1800:
        commission = total_sales * 0.15
    else:
        commission = total_sales * 0.20
    
    return total_sales, commission

# T13.销售问题-计算佣金
# 题目规定值
CR_High = 7
CR_Medium = 6
CR_Low = 5
AS = 2000000
LD = 10
CCR_High = 0.85
CCR_Medium = 0.60

def calculate_commission(sales, leave_days, cash_received_ratio):
    print(sales, leave_days, cash_received_ratio)
    if (sales>=0) and (leave_days>=0 and leave_days<=365)and (cash_received_ratio>=0 and cash_received_ratio<=1):
        if sales > AS and leave_days <= LD:
            if cash_received_ratio >= CCR_Medium:
                commission_coefficient = CR_High
                commission = sales / commission_coefficient
            else:
                commission = 0
        else:
            if cash_received_ratio <= CCR_High:
                commission_coefficient = CR_Medium
            else:
                commission_coefficient = CR_Low
            commission = (sales / commission_coefficient)
    else:
        return -1

    return commission


def telecom(time, count):
    if 0 <= time <= 60:
        if count <= 1:
            return 1
        else:
            return 0
    elif 60 < time <= 120:
        if count <= 2:
            return 1.5
        else:
            return 0
    elif 120 < time <= 180:
        if count <= 3:
            return 2
        else:
            return 0
    elif 180 < time <= 300:
        if count <= 3:
            return 2.5
        else:
            return 0
    else:
        if count <= 6:
            return 3
        else:
            return 0

