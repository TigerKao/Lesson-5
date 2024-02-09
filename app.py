products = []

with open("product.csv", "r", encoding = "utf-8") as f:
    for line in f:
        name, price = line.strip().split(",") # split 完的結果是清單
        products.append([name, price])
print(products)

# [['商品', ' 價格'], ['ramen', '280'], ['pasta', '200']]

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

with open("product.csv", "w", encoding = "utf-8") as f:
    f.write("商品, 價格\n")
    for product in products:
        f.write(product[0] + "," + str(product[1]) + "\n")