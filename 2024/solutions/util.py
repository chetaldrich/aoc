
def delimit(lst, delimiter=''):
    delimited = []
    current_group = []
    for value in lst:
        if value != delimiter:
            current_group.append(value)
        else:
            delimited.append(current_group)
            current_group = []
    delimited.append(current_group)
    return delimited
