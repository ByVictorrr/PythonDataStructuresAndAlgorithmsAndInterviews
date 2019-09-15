def BS(arr, ele):

	high = len(arr)-1
	low = 0
	mid =(high+low) // 2
	# step 1 - base case
	if low > high:
		return 
	else:
		if arr[mid] == ele:
			return True
		elif arr[mid] > ele:
			#search left
			return BS(arr[:mid],ele)
		else: # search right
			return BS(arr[mid:],ele)
		return False
	


if __name__ == "__main__":
	arr = [2,8,9]
	#print(BS(arr,8))
	print(BS(arr,4))
