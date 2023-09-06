# val=int(input("Enter the total number of elements: "))
# lst=[]
# outputlst=[]
# for element in range(0,val):
#     x=int(input())
#     lst.append(x)
#     if (x%2)== 0:


#         outputlst.append(x)
# print("Input numbers:",lst)
# print("Even numbers:",outputlst)
#------------------------------------
#numlist
x=input("Enter list :")
input_list=x.split(',')
lst=[int(item) for item in input_list]
#input list
print("The input list :",lst)
#even number
even_num = [item for item in lst if item%2 == 0]
print("even numbers are:",even_num)
#list number and count
count_elements = {(item,lst.count(item)) for item in lst}
print("list numbers and its count:",count_elements)
#every 2nd element
even_places = [lst[item] for item in range(len(lst)) if item% 2 != 0 ]
print("every second element",even_places)
#every 3rd element
third_element = [lst[item] for item in range(len(lst)) if (item-2) % 3 == 0]
print("third element:",third_element)

#sorting
sorted_elements = sorted(lst)
print("sorted elements:",sorted_elements)

#adding a constant 

added_constant = list(map(lambda x : x+ 5, lst))
print(added_constant)

# every 4 number
fourth_number = list(filter(lambda x : x % 4 == 0 , lst))
print(fourth_number)

#=============================================================

#string list

# str_lst = input("enter the str:")
# str_lst= str_lst.split(',')
# print(f'input list :{str_lst}')

# # even elements 
# even_index=[str_lst[item] for item in range(len(str_lst)) if item% 2 == 0]
# print(even_index)

# # count of vowels
# import re
# vowels = list(filter(lambda x: re.search(r'[aeiouAEIOU]', x), str_lst))
# print(len(vowels))

# #if length more then 5 capitalize
# #str_item = list(filter(lambda x:x.upper() if len(x)> 5 else x.lower(),str_lst))
# str_item = list(map(lambda x: x.upper() if len(x) > 5 else x.lower(), str_lst))
# print(str_item)

# print(" ".join(str_item))

# cons = [x for x in str_lst if not re.search(r'[aeiouAEIOU]', x)]
# print(f'{cons}- the consonents')

# print_count = [len(x) for x in cons]
# print(print_count)

# #---------------------------------

# #looping


 





