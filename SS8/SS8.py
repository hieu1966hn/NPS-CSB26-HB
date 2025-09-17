### Thực hành bài 1:
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

# def intersection(nums1: list, nums2: list): # [1, 2, 1, 3, 4] || [3, 1, 5]
#     arr_giao = [] # list chứa các phần tử chung giữa nums1 và nums2
#     for i in range(len(nums1)): # duyệt theo vị trí phần tử
#         for j in range(len(nums2)):
#             if nums1[i] == nums2[j]: # tìm được phần tử chung của phép giao 2 tập hợp
#                 if nums1[i] in arr_giao: # Nếu như phần tử này đã tồn tại trong danh sách arr_giao
#                     continue # bỏ qua
#                 else:
#                     arr_giao.append(nums1[i]) # thêm vào trong danh sách arr_giao
#     return arr_giao
    
        
# a = [1, 2, 1, 3, 4]
# b = [3, 1, 5]
# print(intersection(a, b)) ## [1, 3]



### Bài thực hành số 2: 
# balls = ['b', 'r', 'b', "w", 'w', 'r']
# def sort_balls(balls:list):
#     count_r = balls.count('r')# Đếm số 'r' có trong danh sách: 2
#     count_w = balls.count('w') # 2
#     count_b = balls.count('b') # 2
#     return ['r']*2 + ['w']*2 + ['b']*2 # trả về danh sách mới

# print(sort_balls(balls))



## Chữa bài thực hành:
scores = [7, 9, 5, 10, 8, 6, 9, 4]
# sx list giảm dần

def bubble_sort(arr: list):  # [1, 3, 100, 67, 80, 2] 
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1): 
            if arr[j] < arr[j+1]: # chỉnh dấu để sx giảm dần
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

scores_bubble = bubble_sort(scores) # DS đã được sx giảm dần
print(scores_bubble) # [10, 9, 9, 8, 7, 6, 5, 4]
print(F'Điểm cao nhất là {scores_bubble[0]}')
print(F'Điểm thấp nhất là {scores_bubble[len(scores_bubble) - 1]}')

## Cách truyền thống;
x = int(input("Mời người dùng nhập điểm: "))
# Kiểm tra xem có học sinh nào đạt điểm x hay không
dem = 0 
for i in range(len(scores_bubble)):
    if x == scores_bubble[i]:
        print(f"Vị trí học sinh có số điểm bằng {x} là: {i}")
        dem += 1 # nếu tìm thấy thì đếm tăng
        break # tìm thấy vị trí đầu tiên thì dừng luôn vòng lặp.
if dem == 0:
    print(f"Không có học sinh nào có số điểm bằng {x}")