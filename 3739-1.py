import math

# 計算點之間距離並分組
def distance_group(x, y, a, b):
    dist = math.sqrt((a[1] - x)**2 + (b[1] - y)**2)
    group = 1
    for i in range(2, 5):
        group1 = i
        dist1 = math.sqrt((a[i] - x)**2 + (b[i] - y)**2)
        if dist1 < dist:
            dist = dist1
            group = group1

    return dist, group

# 計算K-mean值
def cal_Kmean(x, y, a, b):
    # 分組與計算最短距離
    d = [0]
    g = [0]
    sum = 0 
    for i in range(1, len(x)): 
        dist, group = distance_group(x[i], y[i], a, b)
        sum = sum + dist
        d.append(dist)
        g.append(group)

    # 計算K-mean
    D = sum / (len(x) - 1)
    return D, d, g

# 點更新
def update(group, x, y, a, b):
    a1, a2, a3, a4 = 0, 0, 0, 0
    b1, b2, b3, b4 = 0, 0, 0, 0
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0
    for i in range(1, len(x)):
        if group[i] == 1:
            a1 += x[i]
            b1 += y[i]
            sum1 += 1
        if group[i] == 2:
            a2 += x[i]
            b2 += y[i]
            sum2 += 1
        if group[i] == 3:
            a3 += x[i]
            b3 += y[i]
            sum3 += 1
        if group[i] == 4:
            a4 += x[i]
            b4 += y[i]
            sum4 += 1
    a = [0, a1 / sum1, a2 / sum2, a3 / sum3, a4 / sum4]
    b = [0, b1 / sum1, b2 / sum2, b3 / sum3, b4 / sum4]
    
    return a, b
    


# 定義15個以上的座標
x = [0, 2, 3, 3, 3, 4, 4, 6, 6, 6, 7, 7, 7, 7, 8, 8]
y = [0, 5, 2, 3, 4, 3, 4, 3, 4, 6, 2, 5, 6, 7, 6, 7]

# 定義4個點
a = [0, 2, 4, 6, 8]
b = [0, 2, 6, 5, 8]

while True:
    D_result, dist, group = cal_Kmean(x, y, a, b)
    a_new, b_new = update(group, x, y, a, b)
    print("The D is: ", D_result)

    if a == a_new:
        print("The D is: ", D_result)
        break
    a = a_new
    b = b_new
