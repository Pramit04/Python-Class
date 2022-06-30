print("======Computer Bazaar======")


print("1.Dell(Rs.20000) 2.Toshiba(Rs.30000) 3.Mac(Rs.50000)")
option=int(input("Select Any Option:"))

dell_price = 0
toshiba_price = 0
mac_price = 0
quantity = 0
delivery_price = 0
plastic_price = 0
bag_price = 0
gift_box_Price = 0
tax_price = 0

if option ==1:
    quantity =int(input("Enter the quantity:"))
    dell_price = 2000* quantity
elif option ==2:
    quantity = int(input("Enter the quantity:"))
    toshiba_price = 30000* quantity
elif option ==3:
    quantity =int(input("Enter the quantity:"))
    mac_price = 50000* quantity

else:
    print("Invalid option")
    exit()


print("Delivery options")
print("1.Home delivery(1000) 2.Pickup(free)")

delivery_option=int(input("Select any option:"))
if delivery_option ==1:
    delivery_price = 1000

print("Packing Options")
print("1. plastic: 500 2.bag: 1000 3. gift box price:50000")
packing_option=int(input("Select any option"))

if packing_option==1:
    plastic_price=500
elif packing_option==2:
    bag_price=1000
elif packing_option==3:
    gift_price=5000

print("Location: 1. Ktm(13% Tax) 2. Ltp(Free) 3. Bkt(Free)")
location_option=int(input("Select any option"))

if location_option==1:
    tax_price= total_price * 0.13

grand_total = total_price




    





 
