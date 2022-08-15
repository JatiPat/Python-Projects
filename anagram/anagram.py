def sort(arr): #Bubble sorting the letters!
	n = len(arr)
	for i in range(n):
		for j in range(n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr

def main():
	print("This is main! Please give two strings to see if they are anagrams!")
	
	str1 = input("Enter string #1: ").lower().replace(" ","") #takes input and lower cases them and deletes spaces!
	str2 = input("Enter string #2: ").lower().replace(" ","")


	x = len(str1) #gets string length
	y = len(str2)

	if x != y: #different lengths mean different strings
		print("Different sizes! So they aren't anagrams!")
		
	else:
		print("Same size checked!")
	
		arr3 = sort(list(str1)) #converting string into a list of array and sorting the letters 
		arr4 = sort(list(str2))

		if arr3 == arr4: #If the two arrays are they same, they must be anagrams!
			print("We have a match! It is an anagram!")
		else:
			print("We do NOT have a match! It is NOT an anagram!")

	
if __name__ == "__main__": #code given in project manual
	main()