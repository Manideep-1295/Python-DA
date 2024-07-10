from abc import *

class NegativeNumber(Exception):
    def __init__(self,error):
        pass


class Shopping(ABC):
    @abstractmethod
    def items(self):
        pass
    @abstractmethod
    def addItems(self):
        pass
    @abstractmethod
    def removeItems(self):
        pass

class ShoppingCart(Shopping):
    products = {}
    def items(self):
        pass
    def addItems(self,item):
        if item.lower() in self.products:
            self.products[item.lower()] += 1
        else:
            self.products[item.lower()] = 1
        return self.products
    def removeItems(self,item):
        if item.lower() in self.products:
            if self.products[item.lower()] == (0 or 1):
                del self.products[item.lower()]
                return self.products
            else:
                self.products[item.lower()] -= 1
        return self.products
    def viewAllItems(self):
        if self.products == 0:
                self.products.clear()
        else:
            return self.products


user = ShoppingCart()
availProds = list(map(str,input("Enter the list of products available in the App: (Use spaces to enter new product) - ").split()))
while True:
    term = int(input("Enter Your choice:\n \
                1. List of available Items\n \
                2. Add Item to Cart\n \
                3. Delete Item from Cart\n \
                4. View Items in Cart\n \
                5. Exit\n \
                Enter your choice: "))

    match term:
        case 1:
            print("List of available products in the application :")
            for i in range(1,len(availProds)+1):
                print(i,'.',availProds[i-1])

        case 2:
            prodAdd = int(input("Enter the product_Id to Add to the cart: "))
            if prodAdd < 0:
                raise NegativeNumber("Invalid product ID")
            else:
                print("Cart: ",user.addItems(availProds[prodAdd-1]))
        case 3:
            prodDel = input("Enter the product Name to Delete from the cart: ")
            print("Updated Cart: ",user.removeItems(prodDel))
        case 4:
            print(f"View all the items in the cart: {user.viewAllItems()}")
        case 5:
            exit()
        case _:
            print("Invalid input, choose correctly")


'''
print("List of available products in the application :")
for i in range(1,len(availProds)+1):
    print(i,'.',availProds[i-1])


prodAdd = int(input("Enter the product_Id to Add to the cart: "))
if prodAdd < 0:
    raise NegativeNumber("Invalid product ID")
else:
    print("Cart: ",user.addItems(availProds[prodAdd-1]))

print(f"View all the items in the cart: {user.viewAllItems()}")

print("List of available products in the application :")
for i in range(1,len(availProds)+1):
    print(f"{i}. {availProds[i-1]}")

prodDel = input("Enter the product Name to Delete from the cart: ")
print(user.removeItems(prodDel))

print(f"View all the items in the cart: {user.viewAllItems()}")
'''