total_revenue = 1000 # Biến Global

def update_global_counter(amount):
    # Mục đích: Tăng total_revenue lên bằng total_revenue + amount
    # HÃY CỐ GẮNG TRUY CẬP VÀ THAY ĐỔI total_revenue Ở ĐÂY
    global total_revenue
    total_revenue = total_revenue + amount # Dòng này sẽ gây lỗi
    print(f"Revenue cập nhật (trong hàm): {total_revenue}")

update_global_counter(500)