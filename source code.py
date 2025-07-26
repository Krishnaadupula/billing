
product={
    'milk':30,
    'rice':50
}
cart={}
for item, price in product.items():
  print(f"{item}: ₹{price}")
while True:
  item=input("enter the item")
  if item=='done':
    break;
  
  elif item in product:
    qyt=int(input("num of u want"))
    if item in cart:
      cart[item]+=qyt
    else:
      cart[item]=qyt
  else:
    print("try again")
print("\n  final bill")
total_price=0
for item,q in cart.items():
    price=product[item]
    total_price+=price*q
    print(f"{item:10} x {q:<3}={total_price}")
