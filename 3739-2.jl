using Statistics

# 计算点之间的距离并分组
function distance_group(x, y, a, b)
    dist = sqrt.((a[:, 1] .- x).^2 .+ (a[:, 2] .- y).^2)
    group = argmin(dist)
    return dist[group], group
end

# 计算K-mean值
function cal_Kmean(point, a, b)
    d = []
    g = []
    for i in 1:15
        dist, group = distance_group(point[i, 1], point[i, 2], a, b)
        push!(d, dist)
        push!(g, group)
    end
    D = mean(d)
    return D, d, g
end

# 点更新
function update(group, point, a, b)
    new_a = [mean(point[group .== i, 1]) for i in 1:size(a, 1)]
    new_b = [mean(point[group .== i, 2]) for i in 1:size(b, 1)]
    return new_a, new_b
end

# 定义15个以上的座标
point = [2.0 5.0; 3.0 2.0; 3.0 3.0; 3.0 4.0; 4.0 3.0; 4.0 4.0; 6.0 3.0; 6.0 4.0; 6.0 6.0; 7.0 2.0; 7.0 5.0; 7.0 6.0; 7.0 7.0; 8.0 6.0; 8.0 7.0]

# 定义4个点
a = [2.0 2.0; 4.0 6.0; 6.0 5.0; 8.0 8.0]
b = copy(a)  # 初始化 b，使其与 a 具有相同的维度

while true
    D_result, _, group = cal_Kmean(point, a, b)
    println("The K-mean is: ", D_result)
    new_a, new_b = update(group, point, a, b)
    if a == hcat(new_a,new_b)
        println("The K-mean is: ", D_result)
        break
    else
       global  a = hcat(new_a, new_b)
       global  b = copy(a)
    end
end
