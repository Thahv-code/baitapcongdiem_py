user_name = input("Tên khách hàng: ")
product_name = input("Tên sản phẩm: ")
price = float(input("Đơn giá: "))
count = int(input("Số lượng: "))
total = price * count
if total >= 100000:
    total= total*0.9
print("===== HÓA ĐƠN =====")
print(f"Khách hàng: {user_name}")
print(f"Sản phẩm: {product_name}")
print(f"Đơn giá: {price} VNĐ")
print(f"Số lượng: {count}")
print(f"Thành tiền: {total} VNĐ")
print("==================")
