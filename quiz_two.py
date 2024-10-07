# SAPGUIAN, ESTHER RIN

# CREATE A VARIABLE THAT WILL STORE THE NAMES OF YOUR GROUPMATES
mem1 = "Esther Rin P. Sapguian"
mem2 = "Christine Jhed Infante"
mem3 = "Deyn R. Castro"

firstMemAge = "19"
secMemAge = "20"
thirdMemAge = "20"

# convert the age string to integer
memAge1 = int(firstMemAge)
memAge2 = int(secMemAge)
memAge3 = int(thirdMemAge)

# declaration of group member allowances

firstMemAllowance = float(1000.0)
secMemAllowance = float(1000.0)
thirdMemAllowance = float(1000.0)

teamName = "Nuxt"

print("Team name:" , teamName)
print("Member 1:", mem1 , ",her age is" , firstMemAge , ",allowance per week is ", firstMemAllowance )
print("Member 2:", mem2 , ",her age is" , secMemAge , ", allowance per week is ", secMemAllowance )
print("Member 3:", mem3 , ",his age is" , thirdMemAge , ", allowance per week is ", thirdMemAllowance )

# length of names of group members
memName1 = len(mem1)
memName2 = len(mem2)
memName3 = len(mem3)

print("Member 1 consists of", memName1 , "characters")
print("Member 2 consists of", memName2 , "characters")
print("Member 3 consists of", memName3 , "characters")

sumMember = (memAge1 + memAge2 + memAge3)
print (sumMember)
subMember = (memAge1 - memAge2 - memAge3)
print (subMember)

product1 = (memAge1 * firstMemAllowance)
product2 = (memAge2 * secMemAllowance)
product3 = (memAge3 * thirdMemAllowance)

print(product1)
print(product2)
print(product3)

# Comparison of members age

compare1 = (memAge1 - memAge2)
compare2 = (memAge2 - memAge3)
print(compare1)
print(compare2)

# Comparison of name length of group members

nameLen1 = (memName1 - memName2)
nameLem2 = (memName2 - memName3)

print(nameLen1)
print(nameLem2)