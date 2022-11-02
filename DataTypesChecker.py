import re
import sys
import ipaddress


# we can call this method retun one type I try to make it accurate 100% type returned no possible for weight, path without detailed info
# like size limit of number what weight have and path not 41514 41514 both valid weight and path can have hidden word 
def validate_IP(prop, match_ip=False,match_prefiex=False):
     # accept starting number 0 or less than 2
     # loop example not
     
     prop = prop.strip()

     # block chain
     
     if match_ip==True:     
         try:
             isValidIPNextHob = ipaddress.ip_address(prop) is not None
             return True
         except:
             return False
             
     if match_prefiex == True:
         # validate prefiex
         
         if "/" in prop:
         
             withoutList = prop.split("/")
             if len(withoutList) != 2:
                 return False
             part1 = withoutList[0]
             part2 = withoutList[1]
             valid_part2 = re.search('([0-9]|0){1,2}$', part2)
             if not valid_part2:
                 print("hi32", part2)
                 return False
             try:
                 testInt = int(str(part2).strip())
                 if testInt < 0 or testInt > 60:
                      return False
             except:
                 return False

             try:
                 valid = ipaddress.ip_address(part1)
                 print(valid)
                 return True
             except:
                 print("hi3")
                 return False
         else:
             try:
                 valid = ipaddress.ip_address(prop)
                 return True
             except:
                 return False
     return False
     
     
def IPPrefiexerTypeChecker(prop, propType='ipprefex', acceptAny=False):
    
     # like typescript says not recomended to use acceptAny as it broke type checking
     if acceptAny == True and not prop:
         return True
      
     if not prop:
         # none when returned it means some wrong when calling method not error !used for troubelshot only
         return None
         
     if type(prop) != type("") and type(prop) != type(0):
         return None
         
     if propType == 'ipprefex':
         stripedProp = str(prop).strip()
         # false mean ignore end check for pure ip it not end with / True mean if only previous base not work apply second type which have /
         isValidIPPrefiex = validate_IP(prop, False, True)
         if isValidIPPrefiex:
             return True
         else:
             return False
             
             
             
     elif propType == 'ipnexthob':
         stripedProp = str(prop).strip()
         isValidIPNextHob = validate_IP(prop, True)

                     
             
         #print(stripedProp.split("."))
         #print(lastValidIP)
         if isValidIPNextHob:
             return True
         else:
             return False
     elif propType == 'weight':
         weightValidatorRegex = '^\d{0,4}\d{0,4}$'
         isValidWeightType = re.match(weightValidatorRegex, prop)        
         
         if isValidWeightType:
             return True
         else:
             return False     

     elif propType == 'aspath':
         validAsPath = False
         stripedProp = str(prop).strip()
         asPathValidator = "^[0-9]{0,6}$"
         # one small diffrence not yet
         if " " in stripedProp:
             for pathPart in stripedProp.split(" "):
                 validAsPath = re.search(asPathValidator, pathPart)
                 
                 if not validAsPath:
                     validAsPath = False
                 else:
                     validAsPath = True
         else:
             

             validAsPath = re.search(asPathValidator, stripedProp) is not None
         return validAsPath


     else:
         # why none while I return true false always, cus none come from mistake maybe wrong type or prop 
         return None


dataTypes = ['ipprefex', 'ipnexthob', 'weight', 'aspath']


for atype in dataTypes:
    isValidIPPrefex = IPPrefiexerTypeChecker('192.168.1.1', atype)
    print("\nis valid {} type: ".format(atype), str(isValidIPPrefex))

    
