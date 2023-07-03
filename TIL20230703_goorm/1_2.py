special_len, word_len = input().split()
special_word = input()
word = input()

result = word

while special_word in result:
    result = result.replace(special_word, '')

if result == '':
    print('EMPTY')
else:
    print(result)

# ex)
# input : 
#   5 10
#   GOORM
#   BwDcVGOORM
# output :
#   BwDcV