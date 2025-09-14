# # Thuật toán kiểm tra n có phải là số nguyên tố hay không?



# # def is_prime(n: int): # ép kiểu dữ liệu truyền vào
# #     if n<2: 
# #         return False
# #     for i in range(2, n): # n = 999,999,937
# #         if n%i ==0:
# #             return False
# #     return True
        
# # # Kiểm tra thời gian chạy với số nguyên tố lớn nhất có 9 chữ số n = 999,999,937
# # import time
# # begin = time.time() # bắt đầu tính giờ chạy
# # num = 999999937
# # print(num, "is prime" if is_prime(num) else "is not prime") # thời gian chạy: 36.93020486831665 s
# # end = time.time() # kết thúc tính giờ chạy
# # print("Algorithm took", end-begin, "seconds")
    
# def has_duplicate(nums): # [1, 3, 2, 3]
#     for i in range(len(nums)): 
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# nums = [0,1,2,3,1]
# print(has_duplicate(nums)) # True

# nums = [0,1,2,3]
# print(has_duplicate(nums)) # False

# ## Độ phức tạp thời gian: O(n^2) vì có vòng lặp lồng nhau
# ## Độ phức tạp bộ nhớ: O(1)


############### Thuật toán tìm kiếm - linear Search
def linear_search(arr, num):  # [1,2,3,4,5,6,7], 7 => vị trí số 6
    for i in range(len(arr)):
        if arr[i] == num:
            return i # trả về vị trí thứ i
    return -1

# nums = [1,2,3,4,5,6,7]
# print(linear_search(nums, 7)) # 6
# print(linear_search(nums, 4)) # 3
# print(linear_search(nums, 0)) # ...

# => Đánh giá độ phức tạp: Thời gian: O(n), Bộ nhớ: O(1)
## Linear Search rất dễ hiểu NHƯNG chậm khi danh sách lớn.

#### Thuật toán tìm kiếm nhị phân: Binary Search
nums = [3, 69, 75, 7, 8, 100]
## Sắp xếp lại danh sách này tăng dần
nums.sort()
print(nums)
def binary_search(arr, num):
    left = 0 # vị trí thứ 0
    right = len(arr) - 1 # vị trí cuối cùng
    while left <= right:
        mid = (left + right) // 2 # lấy phần nguyên => tìm vị trí giữa
        
        if arr[mid] == num: # tìm thấy 
            return mid
        elif arr[mid] < num: 
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 # Không tìm thấy vị trí phù hợp    

# 9
## 1 - 10 => 5 - 10 => 7 - 10 => 8 - 10 => 9

print(binary_search(nums, 8))
print(binary_search(nums, 100))
print(binary_search(nums, 1000))

