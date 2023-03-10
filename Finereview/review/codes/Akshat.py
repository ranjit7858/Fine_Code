

def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break

	return result

def mergesort(list):
	if len(list) < 2:
		return list

	middle = int(len(list)/2)
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])

	return merge(left, right)
	
seq =[11, 31, 7, 41, 101, 56, 77, 2]
print("Given array is")
print(seq);
print("\n")
print("Sorted array is")
print(mergesort(seq))


