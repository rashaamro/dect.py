products = []
while True:
    selection = int(input("1.Add new product \n"
                          "2. print product details\n"
                          "3.Buy product\n"
                          "4.Delete product \n"
                          "5.Exit"))

    if selection == 1:
        product_number = int(input("Enter product number:"))
        product_name = input("Enter product name:")
        product_price = float(input("Enter product price:"))
        product_qty = int(input("Enter product quantity:"))
        product = {"id": product_number,
                   "name": product_name,
                   "price": product_price,
                   "qty": product_qty
                   }
        products.append(product)
        print("product added ..thank")

    elif selection == 2:
        product_number = int(input("Enter product number:"))
        for i in products:
            if i.get("id") == product_number:
                print(i)
                break

    elif selection == 3:
        product_number = int(input("Enter product number you want :"))
        for i in products:
            if i['id'] == product_number:
                while True:
                  qty_buy = int(input("Enter quantity you want :"))
                  if qty_buy > i['qty'] or qty_buy<=0 :
                     print("invalid quantity")
                  else:
                        break
                i['qty']=i['qty'] - qty_buy
                break






    elif selection == 4:
        product_number = input("Enter product number you want :")
        for i in products[:]:
            if i.get("id"):
                products.reverse(i)
                break
         else:
            print("product not found ")


    elif selection == 5:
        exit()
    else:
        print("Invalid input")
