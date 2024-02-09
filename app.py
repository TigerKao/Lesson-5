import os # operating system

# 讀取檔案
def read_files(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue # continue 跟 break 只能在 迴圈（for, while) 裡面使用
            name, price = line.strip().split(",") # split 完的結果是清單
            products.append([name, price])
    return products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input("請輸入商品名稱：")
        if name == "q":
            break
        price = int(input("請輸入商品價格："))
        products.append([name, price])
    print(products)
    return products


# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], "的價格是", p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, "w", encoding = "utf-8") as f:
        f.write("商品, 價格\n")
        for product in products:
            f.write(product[0] + "," + str(product[1]) + "\n")


def main():
    filename = "product.csv"
    if os.path.isfile(filename): # 檢查檔案是不是有在同一個路徑裡面
        print("Yeah!找到檔案了")
        products = read_files(filename)
    else:
        print("找不到檔案。。。")

    print_products(products)
    products = user_input(products)
    write_file(filename, products)

main()


# refactor 重構