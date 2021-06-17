
def subsets(nums):
    res = [[]]

    for num in nums:
        tmp = []
        # 创造临时变量，存储遍历到当前num值与res之前的组合值
        # 开始遍历前清空之前存储的组合值
        for sub in res:
            item = sub + [num]
            tmp.append(item)
        res += tmp
    return res

nums = [1, 2, 2]
result = subsets(nums)