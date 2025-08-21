test_dict = { "we" : 2 ,"are":3,"the":2,"best":3,"always":2,}
print("The original dictionary is : " + str(test_dict))

A= 2
res=0
for key in test_dict:
    if test_dict[key] == A:
        res = res +1

print(f"frequency of{A}is: {res}")