# Sắp xếp là quá trình thay đổi vị trí của các phần tử trong một tập hợp các phần tử
# theo một thứ tự nhất định. Trong đó
# - Tập hợp phần tử có thể là một: danh sách, dict, ... 
# - Tập hợp phần tử đã được sắp xếp là mục tiêu chính 

#### Thuật toán sắp xếp tăng dần
def selection_sort(arr:list): # bắt buộc dữ liệu truyền vào phải là list
    arr_sorted = [] # tạo một list rỗng
    while arr: # Nếu arr có phần tử thì chạy. Nếu arr rỗng => thoát while
        minium = min(arr) # tìm phần tử nhỏ nhất 
        arr_sorted.append(minium) # Thêm phần tử nhỏ nhất vào danh sách mới
        arr.remove(minium) # xoá phần tử nhỏ nhất ở danh sách gốc.
    
    return arr_sorted

# arr = [0, 3, 100, 67, 80, 2] 
# arr_sorted = selection_sort(arr) # Gọi hàm selection sort
# print(arr_sorted)

#### Thuật toán sx nổi bọt: tăng dần
def bubble_sort(arr: list):  # [1, 3, 100, 67, 80, 2] 
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
            
arr = [1, 3, 100, 67, 80, 2] 
print(bubble_sort(arr))

### Nhiệm vụ -> biến đổi hàm bubble_sort (tăng dần) => giảm dần 

def bubble_sort_reverse(arr: list):  # [1, 3, 100, 67, 80, 2]
    for i in range(len(arr)):
            for j in range(len(arr) - i - 1): 
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

### Chữa bài thực hành
# numbers = [1, 3, 5 ,7 ,9]
# n = int(input("Nhập số cần tìm: "))

# for i in range(len(numbers)):
#     if numbers[i] == n:
#         print(f"{n} có nằm trong danh sách ")
#         print(f"Vị trí số cần tìm là {i}")


### Chữa bài 3
n = int(input("Nhập số phần tử của danh sách: "))

numbers = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    numbers.append(x)

print("Danh sách đã tạo là: ", numbers)
# Viết hàm Selection Sort (giảm dần) => tham khảo từ code gốc (tăng dần)
# PRINT

