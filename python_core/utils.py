def suggest_npk_ratio(plant_stage): # Nhận tham số trực tiếp
  """Trả về chuỗi tỷ lệ NPK dựa trên giai đoạn cây trồng."""
  if plant_stage == 1:
    return "NPK 30-10-10" # Trả về DỮ LIỆU
  elif plant_stage == 2:
    return "NPK 16-16-8"
  elif plant_stage == 3:
    return "NPK 12-12-17"
  else:
    # Trả về thông báo lỗi, hoặc một giá trị mặc định để xử lý lỗi sau này
    return "Giai đoạn cây trồng không hợp lệ"