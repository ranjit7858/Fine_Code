

def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	a, b = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[a] < right[b]:
			result.append(left[a])
			a+= 1
		else:
			result.append(right[b])
			b+= 1
		if a == len(left) or b == len(right):
			result.extend(left[a:] or right[b:])
			break

	return result

def mergesort(list):
	if len(list) < 2:
		return list

	middle = int(len(list)/2)
	
	right = mergesort(list[middle:])
	left = mergesort(list[:middle])

	return merge(left, right)
	
seq =[11, 31, 7, 41, 101, 56, 77, 2]
print("Given array is")
print(seq);
print("\n")
print("Sorted array is")
print(mergesort(seq))


