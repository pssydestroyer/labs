def task1(nums):
    return sum(x**2 for x in nums)

def task2(nums):
    average = sum(nums) / len(nums)
    return sum(x for x in nums if x >= average)

def task3(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    nums.sort(key=lambda x: (-frequency[x], x))
    return nums

def task4(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def task5(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in num_set:
            length = 0
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

def task6(nums, k):
    n = len(nums)
    k = k % n
    return nums[-k:] + nums[:-k]

def task7(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    output = [1] * n
    
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    for i in range(n):
        output[i] = left_products[i] * right_products[i]
    
    return output

def task8(nums):
    max_ending_here = max_so_far = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def task9(matrix):
    if not matrix:
        return []
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


def task10(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]