# ## khởi tạo danh sách: index: 0
# nums = [1,2,3,4]

# ## truy cập phần tử 
# print(nums[2]) ## 3

# ## Độ dài của danh sách: 
# print(len(nums)) # 4

# ## Thay đổi giá trị phần tử: 3 => "Hello"
# nums[2] = "Hello" 
# print(nums) # 1, 2, Hello, 4

# ## Thêm phần tử: append
# nums.append(5)
# nums.insert(2, 2.5) # 1, 2, 2.5, Hello, 4


# ## Xóa phần tử: 
# del nums[3]
# print(nums) # 1, 2, 2.5, 4

# new_list = [9, 10]

# ## Nối 2 danh sách
# print(nums + new_list)

# ## Duyệt danh sách
# for i in nums: 
#     print(i) # 1, 2, 2.5, 4

# for j in range(len(nums)):
#     print(nums[j]) # 1, 2, 2.5, 4
    


### Đề bài thực hành 1: 

# grades = [9, 10, 10, 2, 1, 7, 1, 10, 1, 9]

# #  Tính mean: trung bình
# tb = sum(grades)/ len(grades) # 6.0

# # Tính trung vị: sx lại danh sách
# grades.sort() # tăng dần: [1, 1, 1, 2, 7, 9, 9, 10, 10, 10] => sàn
# l = len(grades) # 10
# mid = l//2 # 5 (//: lấy phần nguyên)
# if l%2 ==0: 
#     tv = (grades[mid] + grades[mid - 1])/2
# else:
#     tv = grades[mid]
    
# ## Tính yếu vị
# from collections import Counter # => Đếm số lần mỗi điểm xuất hiện
# counter = Counter(grades) # Counter({1: 3, 10: 3, 9: 2, 2: 1, 7: 1})

# max_freq = max(counter.values()) # giá trị lớn nhất trong các tần suất -> tần suất cao nhất 3


# yv = []
# for element, freq in counter.items(): # element (điểm), freq (tần suất)
#     # Nếu tần suất điểm đang xét bằng với max_freq, thêm nó vào list yv
#     if freq == max_freq:
#         yv.append(element)
    


# # ## In kết quả 
# print("Trung Bình: ", tb)
# print("Trung vị: ", tv)
# print("Yếu vị: ", yv)


####### Module 2: Hàm
## Khởi tạo hàm máy mía
def May_mia(mia):
    print("ép mía")
    return 'nước mía'

## Gọi hàm: 
print(May_mia("Cây mía"))

### Viết chương trình con (hàm) in ra số từ 0 => n - người dùng nhập vào
def in_ra_tu_0_den_n(n):
    for i in range(n+1):
        print(i)
    
in_ra_tu_0_den_n(10)

### Viết chương trình con chào người dùng
def hello_user(name):
    return f"Xin chào {name}" # f"{name}" => cho phép truyền biến vào chuỗi => "Xin chào" + name

print(hello_user("Nguyễn Trung Hiếu"))

#### Viết chương trình con tính giai thừa của một số n nhập vào: 5! = 1*2*3*4*5 = 120
def giai_thua(n):
    if n < 0: 
        return f"Không tồn tại {n}!"
    elif n == 0:
        return 1
    else:
        gt = 1
        for i in range(1, n + 1):
            gt *= i
        return gt

print(giai_thua(5))