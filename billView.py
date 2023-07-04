import tkinter as tk
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["hospital"]  # Edit Hospital Name
mybill = mydb["Bill"]

def bill(billid):
    def getdataBill(id):
        query = {"_id": id}
        document = mybill.find_one(query)
        print(document)
        if document:
            items = document["items"]
            pad = document["Amount-pad"]  # Retrieve the "pad" field, defaulting to 0 if not present
            return items, pad
        else:
            return [], 0

    # Create the Tkinter window
    root = tk.Tk()
    id=billid
    # id="3"
    items, pad = getdataBill(id)

    # Create labels for table headers
    name_label = tk.Label(root, text="Item-name", font="bold")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    quantity_label = tk.Label(root, text="Quantity", font="bold")
    quantity_label.grid(row=0, column=1, padx=5, pady=5)

    price_label = tk.Label(root, text="Price", font="bold")
    price_label.grid(row=0, column=2, padx=5, pady=5)

    # Iterate over the items and create labels for each row
    for i, item in enumerate(items, start=1):
        name, quantity, price = item

        name_label = tk.Label(root, text=name, padx=5, pady=5)
        name_label.grid(row=i, column=0, sticky="w")

        quantity_label = tk.Label(root, text=quantity, padx=5, pady=5)
        quantity_label.grid(row=i, column=1)

        price_label = tk.Label(root, text=price, padx=5, pady=5)
        price_label.grid(row=i, column=2, sticky="e")

    # Calculate the total price
    total = sum(int(quantity) * int(price) for _, quantity, price in items)

    AmountPad_label = tk.Label(root, text=f"Amount Pad: $ {pad}", font="bold")
    AmountPad_label.grid(row=len(items) + 1, columnspan=3, padx=5, pady=5)

    total = total - pad

    # Create a label for the total
    total_label = tk.Label(root, text=f"Due: $ {total:.2f}", font="bold")
    total_label.grid(row=len(items) + 2, columnspan=3, padx=5, pady=5)

    # Start the Tkinter event loop
    root.mainloop()
