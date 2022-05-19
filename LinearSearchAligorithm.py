nums_list = [10, 23, 45, 70, 11, 15]
target = 70

# if the number is not present return -1

def search(list, n):
    for i in range(len(list)):
        if n == list[i]:
            return f"I found {n}!"
            break
    else:
        return -1

print(search(nums_list, target))
