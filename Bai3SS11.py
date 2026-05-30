# Phân tích 
# Đề bài yêu cầu chúng ta làm 1 menu gồm có 5 chức năng, để làm được menu này thì chúng ta cần vòng lặp while và kết thúc khi người dùng ấn 5 là break
# Chức năng 1 là yêu cầu hiển thị danh sách sản phẩm theo định dạng
# Để làm được chức năng này thì chúng ta duyệt qua vòng for sau đó in ra lần lượt các phần tử 
# Còn nếu mà danh sách không có sản phẩm thì in ra danh sách hiện đang trống 
# Chức năng thứ 2 là thêm sản phẩm mới 
# Đầu tiên là yêu cầu người dùng nhập vào 4 biến là mã sản phẩm, tên sản phẩm, giá sản phẩm và số lượng 
# Sau đó chúng ta thêm làn lượt các biến vào dict sau đó mới thêm vào mảng sau, sau khi thêm xong thì hiện ra thông báo 
# Chức năng thứ 3 là cập nhật thông tin sản phẩm
# Thì chúng ta yêu cầu người dùng nhập mã cần cập nhật 
# Sau đó chúng ta chuẩn hóa xóa khoảng trắng và chuyển thành chữ hoa, check xem nó có tồn tại hay không, nếu không thì in ra thông báo 
# Còn nếu có thì chúng ta tiến hành cập nhật tên, giá, và số lượng tồn kho 
# Và chức năng cuối cùng là xóa sản phẩm 
# Trước khi xóa thì yêu cầu người dùng nhập mã sản phẩm cần xóa 
# Sau đó check xong là có mã sản phẩm không, nếu không thì in ra thông báo còn nếu có thì tiến hnahf xóa khỏi danh sách 
# Khi code còn cần làm thêm các Edge Cases để code không bug khi chạy và đúng logic 

# Viết code

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]
while True:
    choose = input("""===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm 
4. Xóa sản phẩm theo mã 
5. Thoát chương trình
Chọn chức năng: """)
    match choose:
        case "1":
            print()
            print("Danh sách sản phẩm hiện tại:")
            for index,product in enumerate(product_list):
                print(f"{index+1}. Mã SP: {product.get("product_id")} | Tên: {product.get("product_name")} | Giá: {product.get("price")} | Số lượng: {product.get("quantity")}")
            print()
        case "2":
            input_id_product = input("Nhập mã sản phẩm cần thêm: ")
            valid = True
            for index,product in enumerate(product_list):
                if product.get("product_id").lower() == input_id_product.strip().lower():
                    print("Mã sản phẩn đã tồn tại, không thể thêm sản phẩm")
                    valid = False
                    break 
            if valid == True:
                input_name_product = input("Nhập tên sản phẩm: ")
                input_price = int(input("Nhập giá sản phẩm: "))
                while input_price < 0:
                    print("Giá không hợp lệ")
                    input_price = int(input("Nhập giá sản phẩm: "))
                input_quantity = int(input("Nhập số lượng sản phẩm: "))
                while input_quantity < 0:
                    print("Số lượng không hợp lệ")
                    input_quantity = int(input("Nhập số lượng sản phẩm: "))
                new_dict = {}
                new_dict["product_id"] = input_id_product.upper()
                new_dict["product_name"] = input_name_product
                new_dict["price"] = input_price
                new_dict["quantity"] = input_quantity
                product_list.append(new_dict)
        case "3":
            input_product_update = input("Nhập mã sản phẩm cần cập nhật")
            valid = True
            for index,product in enumerate(product_list):
                if product.get("product_id").lower() == input_product_update.strip().lower():
                    input_name_update = input("Nhập tên mới cho sản phẩm: ")
                    input_price_update = int(input("Nhập giá mới cho sản phẩm: "))
                    input_quantity_update = int(input("Nhập số lượng mới cho sản phẩm: "))
                    product["product_name"]
        case "4":
            print()
        case "5":
            print("Chương trình kết thúc")
            break
        case _:
            print("Lựa chọn không hợp lệ")
            print()