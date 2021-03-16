h = []
total = 0
for i in range(9):
    data = int(input())
    h.append(data)
    total += data
total = total - 100    
for i in range(9):
    find = total - h[i]
    if find in h and find != h[i]:
        remove_data = find
        h.remove(find)
        h.remove(h[i])
        break

def quick_sort(array):
    if len(array) <=1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x> pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

result = quick_sort(h)
for i in range(7):
    print(result[i])
