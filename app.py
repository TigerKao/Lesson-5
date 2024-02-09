products = []

while True:
    name = input("請輸入商品名稱：")
    if name == "q":
        break
    price = int(input("請輸入商品價格："))
    products.append([name, price])
print(products)

products[0][0]

for product in products:
    print(product[0])

with open("product.csv", "w") as f:
    for product in products:
        f.write(product[0] + "," + str(product[1]) + "\n")