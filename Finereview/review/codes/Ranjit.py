def merge_sort_prog(inp_arr):
    size = len(inp_arr)
    if size > 1:
        middle = size // 2
        left_arr = inp_arr[:middle]
        right_arr = inp_arr[middle:]
 
        merge_sort_prog(left_arr)
        merge_sort_prog(right_arr)
 
        pi = 0
        qi = 0
        ri = 0
 
        left_size = len(left_arr)
        right_size = len(right_arr)
        while pi < left_size and qi < right_size:
            if left_arr[pi] < right_arr[qi]:
              inp_arr[ri] = left_arr[pi]
              pi += 1
            else:
                inp_arr[ri] = right_arr[qi]
                qi += 1
             
            ri += 1
 
        
        while pi < left_size:
            inp_arr[ri] = left_arr[pi]
            pi += 1
            ri += 1
 
        while qi < right_size:
            inp_arr[ri]=right_arr[qi]
            qi += 1
            ri += 1
 
inp_arr = [11, 31, 7, 41, 101, 56, 77, 2]
print("Input Array:\n")
print(inp_arr)
merge_sort_prog(inp_arr)
print("Sorted Array:\n")
print(inp_arr)
