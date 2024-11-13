class VendingMachine:
    def __init__(self):
        self.inventory = {
            "bottles": 20,
            "cans": 20,
            "candy": 20,
            "chips": 20
        }
        
    def purchase_item(self, item, amount):
        if item in self.inventory:
            self.inventory[item] -= amount

    def restock_item(self, item, amount):
        if item in self.inventory:
            self.inventory[item] += amount
    
    def get_inventory(self):
        return self.inventory
        
    def report(self):
        for item, amount in self.inventory.items():
            print(f'Inventory: {amount} {item}')
        

def display_menu(vending):
    while True:
        print('1. Purchase')
        print('2. Report')
        print('3. Exit')
        input_value = input('Enter a number: ')

        if input_value == '1':
            amount = int(input('Enter amount: '))
            print('1. Bottles')
            print('2. Cans')
            print('3. Candy')
            print('4. Chips')
            print('5. Exit')
            input_value = input('Enter a number: ')

            item_map = {
                '1': 'bottles',
                '2': 'cans',
                '3': 'candy',
                '4': 'chips'
            }

            if input_value in item_map:
                item = item_map[input_value]
                vending.purchase_item(item, amount)
                vending.restock_item(item, amount)
            elif input_value == '5':
                break
            else:
                print('Invalid input')

        elif input_value == '2':
            vending.report()
        elif input_value == '3':
            break
        else:
            print('Invalid input')


if __name__ == "__main__":
    display_menu(VendingMachine())
