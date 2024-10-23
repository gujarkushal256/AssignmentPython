# Write a code for Palindrome

def isPalindrome():
	stringvar=input("Enter the string:")
	tempvar=stringvar[::-1]
	if stringvar==tempvar:
		return True
	else:
		return False

# Boolean Function for checking the Palindrome string

print("The Input String is Palindrome",isPalindrome())