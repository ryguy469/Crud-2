import csv

products = []

# leveraged code from professor rosseti
csv_file_path = "data/products.csv"
headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        #print(row["id"], row["name"])
        products.append(row)

# OVERWRITING INVENTORY CSV FILE
with open(csv_file_path, "w") as csv_file: # NOTE: "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)

menu = """
-----------------------------------
PRODUCTS APPLICATION
-----------------------------------

Welcome Hungry Hippo Employee.

There are {0} products.

   operation | description
    --------- | ------------------
    'List'    | Display a list of product identifiers and names.
    'Show'    | Show information about a product.
    'Create'  | Add a new product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.

Please choose an operation:
""".format(len(products))



chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def product_full_information():
    print(str(" + '{id: '" + product["id"] + "," + "'name: '" + product["name"] + "," + "'aisle: '" + product["aisle"] + "," + "'department: '" + product["department"] + "," + "'price: '" + product["price"] + "}"))


def list_products(): #leveraged code from professor rosseti
    print("There are " + str(len(products)) + "products")
    for product in products:
        print(" + '{id: '" + product["id"] + "," + "'name: '" + product["name"] + "," + "'aisle: '" + product["aisle"] + "," + "'department: '" + product["department"] + "," + "'price: '" + product["price"] + "}")

def show_products(): #leveraged code from professor rosseti
    product_id = input("Ok, enter the desired product id:")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("Right then, here's the information", "'{id: '" + product["id"] + "," + "'name: '" + product["name"] + "," + "'aisle: '" + product["aisle"] + "," + "'department: '" + product["department"] + "," + "'price: '" + product["price"] + "}")
    else:
        print("ummm, are you sure that was the right product id?", product)



def create_product(): #leveraged code from professor rosseti
    print('Oh yea add products baby')
    product_name = input("product name?")
    product_aisle = input("product aisle?")
    product_department = input("product department?")
    product_price = input("product price?")
    newproduct = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price,
    }
    print("New product logged in the Hippo System")
    products.append(newproduct)



def update_product():
    product_id = input("Sure thing, hippo we can update some products. What is the product id?")
    product = [p for p in products if p["id"] == product_id][0] #leveraged code from professor rosseti
    if product:
        print("OK. What's the updated information?") #leveraged code from professor rosseti
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header])) #leveraged code from professor rosseti
        print("Here's that new product info", "'{id: '" + product["id"] + "," + "'name: '" + product["name"] + "," + "'aisle: '" + product["aisle"] + "," + "'department: '" + product["department"] + "," + "'price: '" + product["price"] + "}")
    else:
        print("ummm, are you sure that was the right product id?", product_id)



def destroy_product():
    product_id = input("Lets destroy some products baby. Enter ID to delete:")
    product = [p for p in products if p["id"] == product_id][0] #leveraged code from professor rosseti
    if product:
        print("Destroying in 3...2...1...", product)
        del products[products.index(product)]
    else:
        print("ummm, are you sure that was the right product id?", product_id)

#leveraged code from professor rosseti
if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_products()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == 'Destroy': destroy_product()
else:print("You can't do that you hippopotamus")
