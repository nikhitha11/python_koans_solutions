dict_menu = {'veg':
            {'item':['Aloo Matar','Palak Panner',"Dal",'Gobi'],
             'price':['123','111','222','333']},
             'non-veg':
            {'item':['Chic Tikka','Fish',"Prawn",'beef'],
             'price':['145','145','264','355']},
             'dessert':
            {'item':['truffle','blackforest',"vailla",'rainbowcake'],
             'price':['456','434','134','442']},

             }


print("choose the menu")
# for first,sec in dict_menu.items():
#     print("choose the menu")
#     print(first)
#     print(input(""))
#     print(j.keys())
#-------
# x=[first for first,sec in dict_menu.items()]
# print(x)
# menu_opt=input("Enter the option:")
# print(menu_opt)
#------
# if menu_opt == 'veg':
#     veg_opt= [sec['curry'] for first,sec in dict_menu.items() if first == "veg"]
#     #veg_opt= dict_menu['veg']['curry']
#     print(veg_opt)
# elif menu_opt == 'non-veg':
#     veg_opt= [sec for first,sec in dict_menu.items() if first == "non-veg"]
#     print(veg_opt)
# else:
#     veg_opt= [sec for first,sec in dict_menu.items() if first == "Dessert"]
#     print(veg_opt)
# for first ,sec in dict_menu.items():
#     #print(first) 
#     #print(sec)
#     for item1 in sec :
#         print(item1[])
    


    # for item in j:
    #     #print(j)
    #     print(item.keys())
    #     print (j[item])
# for dict in dict_menu:
#     print(dict)
#     if dict == 'veg':
#         print(dict['veg'])
#------------------
total = 0
lst=[]
ord_items=[]
lst2=[]
lst3=[]
while True:
    try:
        for dict in dict_menu:
            print(dict)
        menu_opt=input("Enter the option:")
        print(menu_opt)
        for opt,sub_dict in dict_menu.items():
            for item ,price in zip(sub_dict['item'],sub_dict['price']):
                if opt == 'veg' and menu_opt== 'veg':
                
                    print(f'{item}  - {price}rs')
                if opt == 'non-veg' and menu_opt== 'non-veg':
                    print(f'{item}  - {price}rs')
                if opt == 'dessert' and menu_opt== 'dessert':
                    print(f' {item}  - {price}rs')
        order_input=input('Enter the item: ')
        print(order_input)
        order_quantity =int(input("Enter the quantity: "))
        print(order_quantity)

        if order_input in dict_menu[menu_opt]['item']:
            index_num = dict_menu[menu_opt]['item'].index(order_input)
        
        
            item_price = int(dict_menu[menu_opt]['price'][index_num-1])
            # print(item_price)
        ord_items.append(order_input)
        lst.append(dict_menu[menu_opt]['price'][index_num-1])
        
        total=total+(order_quantity*item_price)
        lst2.append(order_quantity*item_price)
        lst3.append(order_quantity)
        print("------------------------------------------")
        for item1,item2,item3,item4 in zip(ord_items,lst,lst2,lst3):
            
            print((f'{item1} - {item2} * {item4} = {item3}'))

        print("The total money spent : ", total)
        print("Thank You for ordering")
        print("--------------------------------")
    except KeyboardInterrupt:
        break
    except ValueError:
        print("Invalid number")      

            