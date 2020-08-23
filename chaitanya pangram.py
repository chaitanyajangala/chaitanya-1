import string
def pangram(str):
     alp="abcdefghijklmnopqrstuwxyz"
     for char in alp:
            if char not in str.lower():
                  return False
     else:
            return True
            
string="The five boxing wizards jump quickly"
if(pangram(string)==True):
     print("yes")
else:
     print("no")
