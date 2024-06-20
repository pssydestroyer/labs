import re 

def task1(text):
    pattern1 = r"^[a-z0-9]*[a-z][a-z0-9]*[0-9][a-z0-9]*$"
    return bool(re.match(pattern1,text))

def task2(text):
    pattern2 = r'[A-Z]'
    return bool(re.search(pattern2, text))

def task3(text):
    ippattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(ippattern,text))

def task4(text):
    time_pattern = r'^(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])$'
    return bool(re.match(time_pattern,text))


def task5(text):
    post_pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(post_pattern,text))

def task6(text):
    pos_pattern = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(pos_pattern,text))

def task7(text):
    card_number = r'^(4|5|6)\d{3}(-?\d{4}){3}$|^(4|5|6)\d{14}$'
    return bool(re.match(card_number, text))

def task8(text):
    number = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(number, text))

def task9(text):
    pattern228 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(pattern228, text))

def task10(text):
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return bool(re.match(ipv6_pattern, text))
