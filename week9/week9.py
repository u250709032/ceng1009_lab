# def is_odd(n) :
#     if n%2==1:
#         return True
#     else:
#         return False
# print(is_odd(5))
#
# def nur(n):
#     return n%2==0
# print(nur(5))
from unittest import result


# def i_leapyear(year):
#     if year%400==0:
#        return True
#     elif year%100==0:
#        return False
#     elif year%4==0:
#        return True
#     else:
#        return False
#
# print(i_leapyear(2000))

# def print_triangular_numbers(n):
#     total=0
#     for i in range(1,n+1):
#         total+=i
#         print(i,total)
#
# print_triangular_numbers(7)

# def is_prime(n):
#   if n<2:
#      return False
#   for i in range(2,n):
#     if n%i==0:
#       return False
#   return True
#
# print(is_prime(13))

# def reverse(s):
#    result=""
#    for ch in s:
#      result=ch+result
#    return result
# print(reverse("hello world"))
#
# def reverse_slice(s):
#    return s[::-1]
# print(reverse_slice("hello world"))

# def remove_all_occurrences(sub,s):
#    return s.replace(sub,"")
#
# print(remove_all_occurrences("l","hello world"))
# print(remove_all_occurrences("ll","hello world"))

# def substitude(message,key):
#    alphabet="abcçdedfgğhıijklmnoöprstştuüvyz"
#    result=""
#    for ch in message:
#       index=alphabet.find(ch.lower())
#       if index == -1:
#           result=result+ch
#       elif ch.isupper():
#           result=result+key[index].upper()
#       else:
#           result = result+key[index].lower()
#    return result
# key="gtgpogjklmnjdıhekdoleejfnffnyh"
# print(substitude("hello world",key))

# def remove_dups(s):
#     result=""
#     for ch  in s:
#         if ch.lower() not in result.lower():
#             result+=ch
#     return result
# print(remove_dups("heLlo world"))
