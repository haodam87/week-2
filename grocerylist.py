stores = []

class Store:
    def __init__(self, store, address):
        self.store = store
        self.address = address


class Shopping_list:
    def __init__(self, items):
        self.items = items

def creategrocerylist():

    choice =""
    while choice != 'q':
        print("Enter 1 to add a store: ")
        print("Enter 2 to add an item to a store: ")
        print("Enter q to quit")
        choice = input("Enter choice: ")
        if choice == "1":
            store_name = input("Enter store name: ")
            store_address = input("Enter store address: ")
            store = Store(store_name, store_address)
            stores.append(store)

        elif choice == "2":
            index = 1
            for store in stores:
                print(f'{index}  {store.store} {store.address}')
                index = index + 1
            add_index = int(input("Which store would you like to add an item to? ")) - 1
            print(stores[add_index].store)
            add_item = input('What iteam would you like to add? ')

            new_item = Shopping_list(add_item)

            stores[add_index].items.append(new_item)

        else:
            break

creategrocerylist()




           
        





