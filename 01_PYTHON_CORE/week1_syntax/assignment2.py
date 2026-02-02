# Yêu cầu 1:
plant_stage = 2
if plant_stage == 1:
  print("Gợi ý: Phân bón giàu đạm")
elif plant_stage == 2:
  print("Gợi ý: Phân bón cân bằng NPK")
elif plant_stage == 3:
  print("Gợi ý: Phân bón giàu Kali")
else:
  print("Lỗi: Giai đoạn cây trồng không hợp lệ")
  
# Yêu cầu 2:
for i in range(1, 6):
  print(f"Đang kiểm tra đại lý thứ {i}")