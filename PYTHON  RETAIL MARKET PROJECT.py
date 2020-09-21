# import sys
#import pandas as pd
def mainMenu():
     while True:
            print ('=========================')
            print('MR ADAMU RETAIL MARKET')
            print ('=========================')
            print('Options')
            print('1.Admin\n 2.User \n 3.Exit') 
            
            Options = int(input('Enter options: '))
            if Options==1:
                print('    ADMIN MENU\n 1. DISPLAY ITEMS \n 2. SET ITEMS PRICE\n 3. UPDATE QUANTITIES  \n 4. ADD NEW ITEM \n 5. View Sales Record \n 6. RETURN') 
                admin = int(input('Enter admin-options: '))
                
                if admin==1:
                    ViewList()
                elif admin ==2:
                    ChangePrice()
                elif admin ==3:
                    updateQty()
                elif admin ==4:
                    addItem()
                elif admin ==5:
                    print ('Receipts', products)
                    print('Available stocks', food_list)
                elif admin ==6:
                    pass
                    

            elif Options == 2:
                print('    USER MENU')
                print('1.DISPLAY ITEMS\n 2.BUY ITEMS \n 3.RETURN') 
                user = int(input('Enter options: '))
                if user == 1:
                     ViewList()
                elif user ==2:
                    Orders()
                elif user ==3:
                    pass
                    
                    
            
                
food_list = {'item': ['Sugar','Bread(sliced)', 'Bread(unsliced)', 'Egg','Three crown(tin)','Peak milk (tin)',
                   'Peak milk (sachet)', 'Bournvita (sachet)', 'Milo(tin)', 'Peak milk (Large Sachet)', 'Milo (Large Sachet)',
                  'Bournvita (Large Sachet)','Custard (small sachet)', 'Corn flakes (small sachet)', 'Golden morn (small sachet)', 
                   'Detergent (small Wawu)', 'Detergent (small Aerial)', 'Detergent (Big Wawu)','Detergent (Big Aerial)',
                   'Corn flakes (big sachet)', 'Golden morn (Large sachet)', 'Sprite (small)','Pepsi (small)','Fanta (small)', 
                   'Lacasera (small)','Sprite (big)','Pepsi (big)', 'Fanta (big)', 'Lacasera (big)','Coke (big)'],
         'Available Quantity': [131, 311, 229, 545, 201,230, 791,611,367,889,934,758,383,647,121,198,354,323,222,341,458,134,674,757,127,956,374,267,786,546],
        'Price per Quantity': [50,200, 150, 50,150, 120,50,50,500,700,700,100,200,150,100,120,115,200,250,750,650,80,80,80,80,150,150,150,150,150]
         
         }
def ViewList():
    #stocks = pd.DataFrame(food_list)
    print('==='*50)
    print(food_list)
    #print(stocks)
def addItem():
    while True:
        print('    New items OPTIONS')
        print('1.Enter Items\n Any other digit to Exit')
        newitems= int(input('Enter newitems-options: '))
        if newitems ==1:
            item = input('Enter an item:')
            qty = int(input('Enter quantity:'))
            price = int(input('Enter Price per quantity:'))
            food_list['item'].append(item)
            food_list['Available Quantity'].append(qty)
            food_list['Price per Quantity'].append(price)
            print ('Items has been updated', food_list)
        else:
            break
def ChangePrice():
    while True:
        print('    New items OPTIONS')
        print('Update Quantity')
        print('1.Yes\n Any other digit to Exit')
        SN = int(input('Enter OPTIONS: '))
        if SN ==1:
            idx = int(input('Enter Serial Number of items: '))
            item = food_list['item'][idx]
            print('You about to change the price of', item)
            print('**'*20)
            print('    New items OPTIONS')
            print('1.Yes\n Any other digit to Exit')
            answer = int(input('Enter Options:'))
            if answer ==1:
                Newprice = int(input('Enter new price:'))
                food_list['Price per Quantity'][idx] = Newprice
                print('price changed')
                print (food_list)
                
        else:
            break
        

def updateQty():
    while True:
        print('    New items OPTIONS')
        print('Update Quantity')
        print('1.Yes\n 2.Exit')
        SN = int(input('Enter OPTIONS: '))
        if SN ==1:
            idx = int(input('Enter Serial Number of items: '))
            item = food_list['item'][idx]
            print('You about to change the quantity of', item)
            print('**'*20)
            print('1.Yes\n Any other digit to Exit')
            answer = int(input('Enter Options:'))
            if answer ==1:
                Newqty = int(input('Enter new Quantity:'))
                food_list['Available Quantity'][idx] = Newqty
                print('Quantity updated successfully')
                print('**'*20)
                print (food_list)
        else:
            break
        


List = []
qty1 = []
prices = []

products = {}

def Orders():
    while True:
        print('    New items OPTIONS')
        print('Make orders')
        print('1.Yes\n Any digit to exit')
        SN = int(input('Enter options: '))
        if SN == 1:
            idx = int(input('Enter Serial Number of items: '))
            item = food_list['item'][idx]
            print('You about to buy', item)
            qty = int(input('Enter quantity:'))
            qtyRem = food_list['Available Quantity'][idx] - qty
            food_list['Available Quantity'][idx] = qtyRem
            price = food_list['Price per Quantity'][idx] * qty
            if  qty < 5:
                    price = price + 0.2
                    print ('20% VAT for customers buying less than 5 item.')
            elif qty > 10:
                price = price + 0.3
                print('30% VAT for customers buying more than 10 items')
                    
            print (products)
                
            print('payment confirmed for', qty, item, 'is', price)
            print('We have', qtyRem, item, 'left')
            List.append(item)
            qty1.append(qty)
            prices.append(price)
            products['item'] = List
            products['qty'] = qty1
            products['prices'] = prices
            
            
            print ('Your orders', products)
            
            total = 0
            for i in products['prices']:
                total = total + i
                if len (products['item']) > 10 and products['prices'] >= 100:
                    total = total - 800
                    print ('N800 bonus goods for customers purchasing more than 10 items')
            print (total)
            products['total'] = total
            print ('Receipts', products)
        else:
            break
        

    
    
            
        
        
        
mainMenu()
