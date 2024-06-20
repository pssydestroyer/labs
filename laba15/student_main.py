import re

def task1(data):
    return list(map(lambda x: x.strip().lower(), data.split(',')))

def task2(emails):
    return list(filter(lambda x: x.count('@') == 1, emails.split()))

def task3(words, length):
    return list(filter(lambda x: len(x) > length, words.split()))

def task4(texts):
    cleaned = map(lambda x: re.sub(r'\W+', '', x.strip().lower()), texts.split(','))
    return list(filter(lambda x: len(x) > 1, cleaned))

def task5(numbers):
    nums = list(map(float, numbers.split(',')))
    max_val = max(nums)
    return list(map(lambda x: x / max_val, nums))

def task6(data, separator):
    return ''.join(data.split(separator))

def task7(numbers):
    return sum(map(lambda x: int(x) if x.isdigit() else 0, numbers.split(',')))

def task8(numbers, threshold):
    return list(filter(lambda x: float(x) > threshold, numbers.split()))

def task9(numbers):
    return list(map(lambda x: int(x) ** 2, numbers.split(',')))

def task10(words):
    return list(map(lambda x: x[::-1], words.split(',')))