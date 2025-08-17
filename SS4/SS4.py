# class Dog:
#     tail="long"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__sound = "Woof" # thuộc tính: đóng gói
    
#     def speak(self):
#         return self.__sound
        
# class Corgi(Dog): # kế thừa class Dog
#     tail = "short" # Kế thừa và ghi đè
#     def __init__(self, name, age):
#         super().__init__(name, age) # Kế thừa và Gọi lại phàm khởi tạo của Cha
#     def speak(self):
#         return super().speak() + " Woof!!" ## kế thừa và ghi đè phương thức

# corgi1 = Corgi("ngắn", 5)
# print(corgi1.tail)
# print(corgi1.speak())
    
### Tính Đa hình 
# class MonAn:
#     def chuan_bi(self):
#         print("Chuẩn bị món ăn chung") # phương thức mặc định => bị ghi đè bởi lớp con
        
# Lớp con: Món chính
# class MonChinh(MonAn):
#     # ghi đè phương thức chuẩn bị
#     def chuan_bi(self):
#         print("Chuẩn bị món chính")

# Lớp con: Món tráng miệng
# class MonTrangMieng(MonAn):
#     # ghi đè phương thức chuẩn bị
#     def chuan_bi(self):
#         print("Chuẩn bị món tráng miệng")
        
# ## Hàm dùng đa hình (Polymorphism)
# def goi_mon(mon_an: MonAn): # Hàm nhận vào 1 đối tượng thuộc lớp MonAn hoặc lớp con của nó
#     ## => Gọi đúng phương tức tương ứng => chính là đa hình
#     mon_an.chuan_bi()
    
# # Thử nghiệm
# mon_chinh = MonChinh()
# mon_trang_mieng = MonTrangMieng()

# goi_mon(mon_chinh) # 
# goi_mon(mon_trang_mieng) # 


#### Bài tập 2 về tính đa hình
# lớp cha
# class DongVat:
#     def keu(self):
#         print("Động vật kêu ...")

# # lớp con: Chó
# class Cho(DongVat):
#     def keu(self):
#         print("Gâu gâu!!")

# # lớp con: Mèo
# class Meo(DongVat):
#     def keu(self):
#         print("Meo meo!!")
        
# # Hàm đa hình
# def nghe_tieng_keu(dong_vat: DongVat):
#     dong_vat.keu()
    
# ## thử nghiệm 
# cho = Cho()
# meo = Meo()

# nghe_tieng_keu(cho) #
# nghe_tieng_keu(meo) # 


#### Chương trình quản lý đơn đặt hàng

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def __str__(self): # hàm hiển thị dạng chuỗi => mặc định sẽ gọi để hiển thị trong terminal
        return f"{self.name}"
    
class Order:
    def __init__(self, customer_id):
        self.items = [] # danh sách sản phẩm KH mua
        self.customer_id = customer_id
    def calculate_total(self): # tính tổng giá trị đơn hàng
        total = 0
        for item in self.items: 
            total += item.price
        return total # trả về kết quả tổng giá trị đơn hàng
    
class Promotion:
    def __init__(self, price):
        self.price = price
    def discount(self):
        self.price *= 0.95 # discount 5%
        
class BulkOrderPromo(Promotion):
    def discount(self):
        self.price *= 0.9
        return self.price
    
class LoyaltyPromo(Promotion): # OOP khách hàng thân thiết
    def discount(self):
        self.price *= 0.85 # giảm 15%
        return self.price
        
# 2 sản phẩm
coc = Item('cốc',2, 30000)
ghe = Item("ghế", 10, 1500000)

# Lên đơn hàng
Hieu = Order("Hieunt")
## Thêm sản phẩm vào đơn hàng
Hieu.items.append(coc)
Hieu.items.append(ghe)

# In ra đơn hàng hiện tại
print("Đơn hàng hiện tại là: ")
for i in Hieu.items:
    print(i)


print(f'Tổng giá trị đơn hàng là {Hieu.calculate_total()}')

## Giá đã giảm vì Hieu là khách hàng thân thiện là: 
Khach_than_thiet = LoyaltyPromo(Hieu.calculate_total())
print(f"Giá giảm khi là khách hàng thân thiện: {Khach_than_thiet.discount()}")