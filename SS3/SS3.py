# Đề bài: Viết chương trình để lưu thông tin nhân viên của một tổ chức.
# Chương trình lưu trữ những thông tin của nhân viên như: tên, tuổi, chức vụ và năm gia nhập công ty

# spock = ["Spock", 35, "Science Officer", 2020]
# mck = ["mck", 25, "Science Officer", 2021]
# Jack = ["Jack", "Science Officer", 25,  2021]
## Vấn đề 1: spock[1] => đều là tuổi nhân viên. Tuy nhiên không ai biết cụ thể số 2 là gì nếu chưa nhìn vào dữ liệu
## Vấn đề 2: Jack[1] => Không còn là tuổi nhân viên nữa mà là chức vụ.

# ===> Như vậy yêu cầu một cách tổ chức thông tin mới chuyên dùng để quản lý thông tin theo từng đối tượng, gọi là " LP Hướng đối tượng"


#### 12. Mô tả đối tượng bằng lớp

## Tạo ra kiểu dữ liệu (loài) Dog
class Dog: # bản thiết kế Dog
    tail = "long"
    # Hàm khởi tạo
    def __init__(self, name, age): # 'Cậu Vàng', 10
        self.name = name
        self.age = age
        self.__sound = "Woof!!"
        
    
    def get_description(self):
        return f'{self.name} is {self.age} year old'
    def speak(self):
        return self.__sound
    
# ## Tạo đối tượng chó mới (thực hành)
# my_dog = Dog("Lu", 3)
# # in ra tên chú chó
# print(my_dog.name) 
# print(my_dog.age) 
# print(my_dog.get_description()) ## ....

    
##### Bài tập thực hành Car
# class Car:
#     # HÀM KHỞI TẠO
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
    
#     def get_description(self):
#         return f"Một chiếc xe {self.color} chạy được {self.mileage}k km"

# car1 = Car('xanh', 20)
# car2 = Car('đỏ', 30)

# print(car1.get_description())
# print(car2.get_description())
        
        
###### 3. Tính đóng gói
# class MonAn:
#     def __init__(self, ten, cong_thuc_bi_mat):
#         self.ten = ten
#         self.__cong_thuc_bi_mat = cong_thuc_bi_mat ## thuộc tính private
    
#     def xem_mon_an(self):
#         print(f'Đây là món {self.ten}')
        
#     ## Tính đóng gói chỉ dùng phương thức mới lấy được thông tin
#     def get_secret(self):
#         return self.__cong_thuc_bi_mat
    
#     ## Tính đóng gói chỉ dùng phương thức mới cập nhật được thông tin
#     def thay_doi_cong_thuc(self, cong_thuc_moi): 
#         self.__cong_thuc_bi_mat = cong_thuc_moi
        
# mon_an_1 = MonAn('Rau muống luộc', 'Rửa sạch rau -> đun sôi nước -> cho rau vào 7p -> vớt rau ra')
# # print(mon_an_1.__cong_thuc_bi_mat)

# ### Cập nhật công thức bí mật
# mon_an_1.thay_doi_cong_thuc('Rửa sạch rau -> đun sôi nước -> cho rau vào 10p -> vớt rau ra')
# print(mon_an_1.get_secret())

    
####### Module 4: kế thừa
# class Husky(Dog):
#     def __init__(self, name, age):
#         super().__init__(name, age)

# husky1 = Husky("Ngáo", 10)
# print(husky1.name, husky1.age)
# print(husky1.get_description())
# print(husky1.speak())
# print(husky1.tail)



class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    
class Order:
    def __init__(self, customer_id):
        self.items = []
        self.customer_id = customer_id
    def calculate_total(self):
        total = 0
        for item in self.items: 
            total += item.price
    
class Promotion:
    def __init__(self, price):
        self.price = price
    def discount(self):
        self.price *= 0.95 # discount 5%
        
class BulkOrderPromo(Promotion):
    pass # viết bổ sung sau
    
class LoyaltyPromo(Promotion):
    pass
        
    