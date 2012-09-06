def quicksort(listOfNumbers):
	if len(listOfNumbers) == 0:
		return []
	pivot = listOfNumbers[0]
	listOfNumbers = listOfNumbers[1:]
	left = [x for x in listOfNumbers if x < pivot]
	right = [x for x in listOfNumbers if x >= pivot]
	return quicksort(left) + [pivot] + quicksort(right)

# Main Function
if __name__ == '__main__':    
    lst = [2,4,5,1]
    print quicksort(lst)    
    