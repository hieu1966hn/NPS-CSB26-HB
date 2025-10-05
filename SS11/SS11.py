# stack = [1, 2, 3]

# # Xem phần tử ở đỉnh: 3
# print(stack[-1])

# # Thêm phần tử 4 vào đỉnh của Stack: 
# stack.append(4)
# print(stack[-1]) # 4


# # Lấy 1 phần tử tử từ đỉnh của Stack: pop()
# stack.pop()
# print(stack[-1]) # 3


#### Bài tập thực hành ứng dụng Stack
class Browser:
    def __init__(self):
        self.backward_stack = []
        self.forward_stack = []
        
    def visit_page(self, url):
        self.backward_stack.append(url)
        self.forward_stack.clear() # xóa hết các trang forward
        print(f'Visiting {url}')
    
    def back(self):
        # kiểm tra xem danh sách backward có phần tử hay không.
        if len(self.backward_stack) > 1: # [youtube, facebook]
            current_page = self.backward_stack.pop() # xóa phần tử ở đỉnh
            self.forward_stack.append(current_page) # thêm phần tử vào forward
            previous_page = self.backward_stack[-1]
            print(f'Going back to {previous_page}')
        else:
            print('Cannot go back!!!')
            
    def forward(self):
        if self.forward_stack:
            next_page =  self.forward_stack.pop() # xóa phần tử đỉnh của forward_stack
            self.backward_stack.append(next_page)
            print(f'Going forward to {next_page}')
        else: 
            print("Cannot go forward!!")
            
            
### Example
browser = Browser()
browser.visit_page("https://drive.google.com/drive/u/0/")
browser.visit_page("https://www.facebook.com/")
browser.visit_page("https://gx.games/")

browser.back() ## https://www.facebook.com/
browser.back() ## https://drive.google.com/drive/u/0/
browser.back() ## Cannot go back!!!

browser.forward() ## https://www.facebook.com/
browser.forward() ## https://gx.games/
browser.forward() ## Cannot go forward!!


