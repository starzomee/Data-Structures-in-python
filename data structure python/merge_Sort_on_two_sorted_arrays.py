def merge_sort():
    pass

def merge_two_sorted_arrays():
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
    a = [5,8,12,56]
    b = [7,9,45,51]
    print("The array is :->" , a)
    print("The length of a is :->",len(a))
    print("The array is :->",b)
    print("The length of b is :->",len(b))
    print("THIS IS SORTED ARRAY :->" , merge_two_sorted_arrays())