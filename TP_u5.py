import csv
import subprocess
import locale


def format_currency(value):
   return locale.currency(value,grouping=True)


def list_products(products):
   for idx, product in enumerate(products, 1):
      
      name = product['name']
      price = format_currency(product['price'])
      quantity = product['quantity']

      print(f"{idx}) {name} \t {price} \t {quantity:<5}")


def view_product(idx, products):
   subprocess.run('cls', shell=True)
   #print(products,idx)
   product = products[idx]
   
   print(f"Name: {product['name']}")
   print(f"Description: {product['desc']}")
   print(f"Price: {product['price']}")
   print(f"Quantity: {product['quantity']}")


def remove_product(idx,products):
   if idx >= 1 and idx <len(products) + 1:
      products.pop(idx-1)
      return "Success deleted"
   

   else:
       return "ERROR PRODUKTEN FINNS INTE"
  

def add_product():

   new_name = input("produktnamn: ")
   new_desc = input("beskrivning: ")
   new_price = float(input("price: "))
   new_quantity = int(input("quantitet: "))
   found_max = max(products, key=lambda id: id['id'])
   max_id = found_max['id']
   new_id = max_id + 1
   
   new_product = {

   
      "id": new_id,
      "name": new_name,
      "desc": new_desc,
      "quantity": new_quantity,
      "price": new_price
   
   }
   products.append(new_product)
def change_product(products, wich_product_change):

    
   
   if wich_product_change < 1 or wich_product_change > len(products):
         print("ERROR: Produkten finns inte.")
         return

   product = products[wich_product_change - 1]

   print(f"\nDu ändrar: {product['name']}")
   print("Vad vill du ändra på?")
   print("1) Namn\n2) Beskrivning\n3) Pris\n4) Kvantitet")
        
   
   change_choice = input("Val: ").lower()

   if change_choice in ["1", "namn"]:
      product['name'] = input("Nytt namn: ")
      print("Namnet har uppdaterats!")

   elif change_choice in ["2", "beskrivning", "beskrivningen"]:
      product['desc'] = input("Ny beskrivning: ")
      print("Beskrivningen har uppdaterats!")

   elif change_choice in ["3", "pris", "priset"]:
      product['price'] = float(input("Nytt pris: "))
      print("Priset har uppdaterats!")

   elif change_choice in ["4", "kvantitet", "quantiteten"]:
      product['quantity'] = int(input("Ny kvantitet: "))
      print("Kvantiteten har uppdaterats!")

   else:
      print("Ogiltigt val.")
      
       
       
   
def load_data(filename): 
   products = []           #lista
   
   with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
      reader = csv.DictReader(file)
      for row in reader:
         id = int(row['id'])
         name = row['name']
         desc = row['desc']
         price = float(row['price'])
         quantity = int(row['quantity'])
         
         products.append(
               {                   
                  "id": id,       
                  "name": name,
                  "desc": desc,
                  "price": price,
                  "quantity": quantity
               }
         )
         
   return products
def save_product(products):
   # Define the CSV file path
    csv_file_path = "db_products.csv"

    # Write the products data to a CSV file
    with open(csv_file_path, mode='w', newline='', encoding="UTF-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "desc", "price", "quantity"])
        writer.writeheader()  # Write the header row
        writer.writerows(products)  # Write the product data

    print(f"Data successfully saved to {csv_file_path}")


#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv klart funktionen som returnerar en specifik produkt med hjälp av id & products
#TODO: skriv en funkion som skapar en ny produkt - den behöver inte spara till fil!
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id

   # found_max = max(products, key=lambda id: id['id'])
   # max_id = found_max['id']
   # new_id = max_id + 1
   
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

subprocess.run('cls',shell=True)

products = load_data('db_products.csv')


while True:
   list_products(products)
   
   print("-" * 140)
   option = input("Vad vill du göra? [# = visa produkt | L = lägg till | T = ta bort | E = ändra | Q = avsluta] ")
   
   
   if option.isdigit(): #if it is numbers digits
      idx = int(option) #4 gör om inmatade option siffror till heltal och idx är en variabel som är datatyp heltal,int
      
      if idx >= 1 and idx < len(products) + 1:
         view_product(idx-1, products)
         input() #bara vänta till tangentbordsklick

   else:
      if option.upper() == "Q":
         exit()

      elif option.upper() == "T":
         which = int(input("Vilken product?: "))

         print(remove_product(which,products))
         input()
      elif option.upper() == "L":
         add_product()
      elif option.upper() == "S":
         save_product(products)
         print("Product saved")

      elif option.upper() == "E":   
         try:
            wich_product_change = int(input("Vilken produkt vill du ändra? Ange #: "))
            change_product(products, wich_product_change)
         except ValueError:
            print("ERROR: Ange ett giltigt nummer.")
            input("\nTryck Enter för att fortsätta...")
    