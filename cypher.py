alpha = 'abcdefghijklmnopqrstuvwxyz'
message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
new_message = ''
encoded_message = ''

user_message = input('Enter a message to be encoded: ')

# for i in message:
#   if i in alpha:
#     i_value = alpha.find(i)
#     new_message += alpha[(i_value - 10) % 26]
#   else:
#     new_message += i
    
for i in user_message:
  if i in alpha:
    i_value = alpha.find(i)
    encoded_message += alpha[(i_value - 10) % 26]
  else:
    encoded_message += i

print("Message to be encoded was: " + (user_message))
print("Message with cypher applied: " + (encoded_message))