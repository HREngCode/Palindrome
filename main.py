user_input = input("Please enter a word to check if it is a Palindrome. ")
front_letter = user_input[0]
back_letter = user_input[len(user_input)-1]
front_index = user_input.find(front_letter)
back_index = user_input.rfind(back_letter)
while front_index != back_index:
	if back_letter == front_letter:
	    front_index + [2]
		break
	else:
		print(f'{user_input} is not a palindrome')
		break