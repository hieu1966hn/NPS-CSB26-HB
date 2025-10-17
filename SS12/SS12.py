# ###### Buổi học số 12

# ## Khai báo hàng đợi: Giống với khởi tạo danh sách
# queue = [1, 2, 3]
# ####### đầu - giữa - cuối

# ## Xem phần tử đầu tiên (front)
# print(queue[0]) # 1

# ## Thêm vào hàng đợi: enqueue
# queue.append(4) # [1,2,3,4]

# ## Lấy khỏi hàng đợi: dequeue (xóa ở đầu)
# front = queue.pop(0) # truyền vị trí muốn xóa vào trong pop()
# print(front) # 1

# ### Hàm kiểm tra hàng đợi rỗng hay không: True/False
# def is_empty(queue):
#     if len(queue) == 0: # số phần tử trong queue = 0
#         return True
#     else: 
#         return False




###### Thực hành ứng dụng MP3
import queue ## class queue mặc định trong Python 

class MP3Player:
    def __init__(self):
        self.music_queue = queue.Queue() # gán kiểu dữ liệu queue vào biến self.music_queue
        self.current_song = None
        
    def add_song(self, song):
        self.music_queue.put(song) ## thêm bài hát vào cuối của hàng đợi: put() phương thức mặc định của queue
        print(f'Đã thêm bài hát {song} vào hàng đợi.')
        
    def play_next_song(self):
        if self.music_queue.empty():
            print("Không có bài hát nào trong danh sách đợi")
        else:
            self.current_song = self.music_queue.get() # get() phương thức lấy ra ở đầu của hàng đợi
            print(f"Đang phát bài hát: '{self.current_song}'")
    
    def skip_song(self):
        if self.current_song is None:
            print("Không có bài hát nào đang phát.")
        else:
            print(f'Đã bỏ qua bài hát: {self.current_song}')
            self.current_song = None
            self.play_next_song()
            
## Ví dụ sử dụng
mp3_player = MP3Player()

mp3_player.add_song("Đợi")
mp3_player.add_song("break free")
mp3_player.add_song("New Jeans")

mp3_player.play_next_song() # output: Đang phát bài hát "Đợi"

mp3_player.skip_song() # output: Bỏ qua bài Đợi => phát bài break free

mp3_player.add_song("Hello") 
        
mp3_player.skip_song() ## Bỏ qua break free, đang phát New Jeans

mp3_player.play_next_song() # output: Đang phát bài Hello

mp3_player.play_next_song() # output: Không có bài hát nào trong danh sách đợi
