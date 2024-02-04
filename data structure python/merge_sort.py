def merge_sort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]


    left =  merge_sort(left)
    right = merge_sort(right)
    return merge_two_sorted_arrays(left , right ) 

def merge_two_sorted_arrays(a ,b):
    sorted_list = [ ]
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1 
        else:
            sorted_list.append(b[j])
            j += 1    
    while i < len_a:
        sorted_list.append(a[i])
        i += 1 
    while j < len_a:
        sorted_list.append(a[j])
        j += 1     
    return sorted_list

if __name__ == '__main__':
    arr = [10,3,15,7,8,23,98,29]
    print("THIS IS SORTED ARRAY :->" , merge_sort(arr))