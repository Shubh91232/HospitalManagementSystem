import tkinter as tk
from tkinter import messagebox
import pymongo

class BillGenerator:
    def __init__(self, root,Bill_id,flag):
        self.root = root
        self.Bill_id=Bill_id
        self.flag=flag
        self.root.title("Bill Generator")
        self.root.geometry("700x500")
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["hospital"] # Edit Hospital Name
        self.mybill = self.mydb["Bill"]
        
        # Create labels and entry fields for items, quantity, and prices
        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()
        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.AmountPad_label = tk.Label(root, text="AmountPad:")
        self.AmountPad_label.pack()
        self.AmountPad_entry = tk.Entry(root)
        self.AmountPad_entry.pack()
        self.amountpd_btn = tk.Button(root, text="AmountPad", command=self.AmountPad)
        self.amountpd_btn.pack()

        # Create 'Add Item' button
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()
        if self.flag:
            GenerateBillbtn="Update Bill"
        else:
            GenerateBillbtn="Add New Bill"
        # Create 'Generate Bill' button
        self.generate_button = tk.Button(root, text=GenerateBillbtn, command=self.generate_bill)
        self.generate_button.pack()

        

        # Create bill preview text widget
        self.bill_text = tk.Text(root)
        self.bill_text.pack()

        # Initialize the list to store items, quantity, and prices
        self.items = []

    def AmountPad(self):
        filter = {"_id": self.Bill_id }  # Replace with the actual document _id value
        try:
            PadAmount= int(self.AmountPad_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity or price. Please enter valid numbers.")
        AlreadyPad=0
        # query = {"_id": id}
        document = self.mybill.find_one(filter)
        AlreadyPad=document["Amount-pad"]

            # Specify the update operation and new values
        update = {
            "$set": {
                #  "items": self.items,
                 "Amount-pad" : PadAmount+AlreadyPad
                # Add more fields to update if needed
            }
        }
        self.mybill.update_one(filter, update)
        messagebox.showinfo("Success", "AmountPad saved to database.")    

    def add_item(self):
        item = self.item_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if item and quantity and price:
            try:
                quantity = int(quantity)
                price = float(price)
                if quantity > 0 and price > 0:
                    self.items.append((item, quantity, price))
                    self.clear_fields()
                    self.update_bill_preview()  # Update bill preview after adding item
                else:
                    messagebox.showerror("Error", "Quantity and price must be greater than 0.")
            except ValueError:
                messagebox.showerror("Error", "Invalid quantity or price. Please enter valid numbers.")
        else:
            messagebox.showerror("Error", "Please enter item, quantity, and price.")

    def generate_bill(self):
        if self.items:
            self.update_bill_preview()
            self.save_bill_to_db()
        else:
            messagebox.showerror("Error", "No items added.")

    def update_bill_preview(self):
        self.bill_text.delete("1.0", tk.END)  # Clear previous bill preview
        total = 0
        bill_preview = "BILL\n\n"
        for item, quantity, price in self.items:
            amount = int(quantity) * float(price)
            bill_preview += f"{item} (Quantity: {quantity}) - ${amount:.2f}\n"
            total += amount
        bill_preview += f"\nTotal: ${total:.2f}"
        self.bill_text.insert(tk.END, bill_preview)

    def clear_fields(self):
        self.item_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def save_bill_to_db(self):

        if self.flag:
            filter = {"_id": self.Bill_id }  # Replace with the actual document _id value
            # PadAmount= int(self.amount_pad_entry.get())
            # AlreadyPad=0
            # query = {"_id": id}
            # document = self.mybill.find_one(filter)
            # AlreadyPad=document["Amount-pad"]

            # Specify the update operation and new values
            update = {
                "$set": {
                     "items": self.items,
                    #  "Amount-pad" : PadAmount+AlreadyPad
                    # Add more fields to update if needed
                }
            }

            # Update the document using update_one
            self.mybill.update_one(filter, update)
            messagebox.showinfo("Success", "Bill Update to database.")
        else:
            
            bill_data = {
                "_id": self.Bill_id,
                "items": self.items,
                "Amount-pad":0
            }
            self.mybill.insert_one(bill_data)
            messagebox.showinfo("Success", "Bill saved to database.")

def Admin_bill(BillId,flag):
    Bill_id=BillId
    Add_Update=flag
    root = tk.Tk()
    app = BillGenerator(root,Bill_id,Add_Update)
    root.mainloop()

# if __name__ == "__main__":
#     Bill_id=1
#     AddorUpdate=False
#     root = tk.Tk()
#     app = BillGenerator(root,Bill_id,AddorUpdate)
#     root.mainloop()
