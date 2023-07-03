word_len = int(input())
word = input()
result_word = ""
for i in word:
	if i.isupper():
		result_word += i.lower()
	else:
		result_word += i.upper()
		
print(result_word)

# ex
# input -> 10 goormLevel
# output -> GOORMlEVEL