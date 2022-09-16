from random import choice
def hoar_sort(arr):
    if len(arr) <= 1 :
        return arr
    b = (arr[0]+ choice (arr) +arr[-1])//3
    left = [ x for x in arr if x < b]
    mid = [ x for x in arr if x == b]
    right = [ x for x in arr if x > b]
    left = hoar_sort (left)
    right = hoar_sort (right)
    return left + mid + right



