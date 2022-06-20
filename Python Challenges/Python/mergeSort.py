def merge(node1, node2):
	i =j =0 
	mergeArray = []

	while i < len(node1) and j < len(node2):
		if node1[i] < node2 [j]:
			mergeArray.append(node1[i])
			i += 1
		else:
			mergeArray.append(node2[j])
			j += 1
	mergeArray += node1[i:] + node2[j:]
	return mergeArray

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	if len(arr) == 2:
		return sorted(arr)
	mid = int(len(arr) /2)
	return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def main():
	array = merge([2,4,1],[3,7,6])
	print(merge_sort(array))

	array = merge([20,10],[-11,10])
	print(merge_sort(array))

	array = merge([8,-5],[4])
	print(merge_sort(array))

	array = merge([1,2],[3])
	print(merge_sort(array))

if __name__ == '__main__': 
    main()