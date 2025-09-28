# Khai báo tập hợp set (danh sách set): sử dụng ngoặc {}
# fruit_basket = {"apple", 'banana', 'cherry', 'apple'}

# # print(fruit_basket[0]) ## báo lỗi không có vị trí

# ## Truy cập phần tử: For
# # for fruit in fruit_basket:
# #     print(fruit)
    
# #### Thêm phần tử": Set.add(<phần tử>)
# fruit_basket.add("orange")

# ### Thêm nhiều phần tử: Set.update({<phần tử 1>, <phần tử 2>, ...})
# fruit_basket.update({"kiwi", 'peach', "lemon"})

# ### Xoá phần tử: Set.remove(<phần tử>)
# fruit_basket.remove("apple") # Nếu apple mà không có trong set => KeyError.
# fruit_basket.discard("lemon") # Nếu lemon mà không có trong set => Không làm gì cả.




##### Phép toán: Hợp
# lunch = {'Cơm rang', "Phở bò", 'Cơm văn phòng'}
# dinner = {'Cá kho', 'Chay', "Cơm rang"}

# menu = lunch.union(dinner) # cách 1
# menu1 = lunch | dinner # cách 2
# print(menu, menu1)

### Phép trừ
# meals = lunch.difference(dinner) # trưa - tối (bỏ đi các món chung nhau)
# print(meals) # 



#### Ánh xạ
student_score_ten = [5.0, 7.0, 8.0, 10.0, 9.0]

## Yêu cầu: Đổi danh sách điểm hệ 10 => ds điểm hệ 4.
# Cách 1: truyền thống.
# student_score_four = []
# for score in student_score_ten: # 5.0 => 2.0
#     doi_diem_sang_he_bon = score*4/10 # 2.0
#     # thêm phần vào danh sách hệ 4
#     student_score_four.append(doi_diem_sang_he_bon)

# print(student_score_four) 

### Cách 2: Sử dụng map(): lambda là keyword định nghĩa hàm rút gọn
# student_score_four = list(map(lambda item: item*4/10 , student_score_ten)) # new list
# print(student_score_four) # Để lấy được danh sách kết quả, dùng hàm list để 
# chuyển đổi kết quả của hàm map thành danh sách.

### Cách 3: Sử dụng hàm tự định nghĩa (hàm hoàn chỉnh)
# def convert_gpa(score): # 7 
#     return score*4/10 # 2.8
# gpa_4 = map(convert_gpa, student_score_ten)
# print(list(gpa_4))


### Sử dụng map với kiểu dữ liệu chữ.
# students = ["Hieu", 'Bảo An', 'Quốc Quân']
# # Viết hoa toàn bộ chữ cái trong danh sách
# students_upper = map(str.upper ,students)
# print(list(students_upper))

#### Xử lý bài toán bộ đếm số từ
import string

def word_freq_counter(text):
    word_freq = {} # từ điển rỗng => để lưu tần suất xuất hiện.
    words = text.lower().split() # toàn bộ chữ -> chữ thường (Hello và hello => tính là cùng một từ)
    # tách chuỗi theo khoảng trắng => kiểu dữ liệu danh sách
    
    # Với mỗi ký tự char trong token, giữ lại ký tự đó nếu nó không phải là dấu câu. Rồi nối lại thành một từ mới
    # VD: "hello," => "hello"
    words = map(lambda word: "".join(char for char in word if char not in string.punctuation)
                , words)
    words = list(words) # map trả về một iterator; list(words) biến nó thành danh sách thực sự.
    