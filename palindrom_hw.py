def palindrome(s): 
  return s[::-1] == s 

while True: 
  s = input("введите слово: ") 
  print(True if 
  palindrome(s) else False)
