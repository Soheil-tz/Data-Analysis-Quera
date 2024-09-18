# coding: utf-8
def my_any(x):
    result = False
    for i in x:
        if i:
            result = True
            break
    return result
