
s=input("Enter the String :")
# def isPalindrome(s):
#   return s == s[::-1]

rev_str=(s[::-1])
if s==rev_str:
  print("the string is palindrome")
else:
  print("the string is not palindrome")