# a list of dictionaries representing the drinks menu
drinks_menu = [
    {
        'itemname': 'Mountain Dew',
        'itemno': 1,
        'price': 2,
        'qty': 4,
    },
    {
        'itemname': 'Thumbs Up',
        'itemno': 2,
        'price': 2,
        'qty': 5,
    },
    {
        'itemname': 'Coca Cola',
        'itemno': 3,
        'price': 2,
        'qty': 6,
    },
    {
        'itemname': 'Sparkling Water',
        'itemno': 4,
        'price': 6,
        'qty': 8,
    },
    {
        'itemname': 'Pepsi',
        'itemno': 5,
        'price': 2,
        'qty': 5,
    },
    {
        'itemname': 'Water',
        'itemno': 6,
        'price': 1,
        'qty': 7,
    },
    {
        'itemname': 'Strawberry Milk',
        'itemno': 7,
        'price': 3,
        'qty': 3,
    },
    {
        'itemname': 'Chocolate Milk',
        'itemno': 8,
        'price': 3,
        'qty': 2,
    },
    {
        'itemname': 'Apple Juice',
        'itemno': 9,
        'price': 2,
        'qty': 7,
    },
    {
        'itemname': 'Mango Juice',
        'itemno': 10,
        'price': 2,
        'qty': 4,
    },
]

# a dictionary representing the snacks menu
snacks_items = {
    "11 Cup Cake": "3 AED",
    "12 Oatville Biscuit": "3 AED",
    "13 Protein Bar": "5 AED",
    "14 Oreo": "2 AED",
    "15 Tomato Chips": "1 AED",
    "16 Chilli Chips": "1 AED",
    "17 Lotus Biscuit": "3 AED",
    "18 Kit Kat": "2 AED",
    "19 Snickers": "2 AED",
    "20 Skittles": "5 AED",
}

# function to print drinks
def print_drinks():
    print("*********FarzeenMart-Vending-Machine*********")
    print("=====================DRINKS==================")
    for item in drinks_menu[:10]:  # Display only the first 10 items
        print(f" {item['itemno']:02} {item['itemname']:20} {item['price']} AED")

# function to print snacks
def print_snacks():
    print("=====================SNACKS==================")
    for item, price in snacks_items.items():
        print(f" {item:30}, {price}")

# function to calculate and print the receipt
def print_receipt(items_purchased, remaining_balance):
    print("\n*********RECEIPT*********")
    total_price = sum(item['price'] for item in items_purchased)
    print("Items Purchased:")
    for item in items_purchased:
        print(f"  {item['itemname']} - {item['price']} AED")
    print(f"Total Price: {total_price} AED")
    print(f"Remaining Balance: {remaining_balance:.2f} AED")

# function to process user's order
def order():
    # Print menu
    print_drinks()
    print_snacks()

    items_purchased = []
    remaining_balance = float(input("Enter the amount of AED you have: "))

    while True:
        # Get user order
        selected_item_no = int(input("Enter the item number you want to purchase: "))

        # Check if the selected item is from drinks_menu or snacks_items
        selected_item = next((item for item in drinks_menu if item['itemno'] == selected_item_no), None)
        if not selected_item:
            selected_item_name = next((item for item in snacks_items if item.startswith(str(selected_item_no))), None)
            if selected_item_name:
                selected_item = {'itemname': selected_item_name, 'price': int(snacks_items[selected_item_name][:-4])}

        if selected_item:
            # Check if user can afford the selected item
            if remaining_balance >= selected_item['price']:
                remaining_balance -= selected_item['price']
                items_purchased.append(selected_item)
                print(f"{selected_item['itemname']} added to the cart.")
            else:
                print("Insufficient funds. Cannot purchase the selected item.")
        else:
            print("Invalid item number. Please choose a valid item.")

        more_items = input("Do you want to buy more items? (yes/no): ").lower()
        if more_items != 'yes':
            break

    print_receipt(items_purchased, remaining_balance)
    print("Thank you for shopping at Farzeen-Mart! Have a great day!")

# calling the order function
order()
