def test_2_wei_bag_problem1(bag_size : int, weight : list[int], value : list[int]) -> int:
    rows, cols = len(weight), bag_size + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = 0
    first_item_weight, first_item_value = weight[0], value[0]
    for j in range(1, cols):
        if first_item_weight <= j:
            dp[0][j] = first_item_value
    for i in range(1, len(weight)):
        cur_weight, cur_val = weight[i], value[i]
        for j in range(1, cols):
            if cur_weight > j:
                dp[i][j] = dp[i -1][j]
            else:
                dp[i][j] = max(dp[i -1][j], dp[i - 1][j - cur_weight] + cur_val)
    print(dp)

if __name__ == "__main__": 
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    test_2_wei_bag_problem1(bag_size, weight, value)