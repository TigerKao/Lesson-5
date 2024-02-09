import os # operating system

products = []

# 檢查檔案是不是有在同一個路徑裡面
if os.path.isfile("product.csv"):
    print("Yeah!找到檔案了")
    with open("product.csv", "r", encoding = "utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue # continue 跟 break 只能在 迴圈（for, while) 裡面使用
            name, price = line.strip().split(",") # split 完的結果是清單
            products.append([name, price])
    print(products)

else:
    print("找不到檔案。。。")

# 讓使用者輸入
while True:
    name = input("請輸入商品名稱：")
    if name == "q":
        break
    price = int(input("請輸入商品價格："))
    products.append([name, price])
print(products)

products[0][0]

# 印出所有購買紀錄
for product in products:
    print(product[0])

# 寫入檔案
with open("product.csv", "w", encoding = "utf-8") as f:
    f.write("商品, 價格\n")
    for product in products:
        f.write(product[0] + "," + str(product[1]) + "\n")