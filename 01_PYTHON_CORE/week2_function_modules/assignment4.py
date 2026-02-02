# Yêu cầu 1:
# Phiên bản Tối ưu hóa:
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

# Cách sử dụng (ở bên ngoài hàm):
stage = 2
ratio = suggest_npk_ratio(stage)
print(f"Vui lòng bỏ phân {ratio} cho giai đoạn {stage}")

# Yêu cầu 2:
from data_processing import filter_by_city
authorized_dealers = [
  {
    "name" : "An Phát",
    "city" : "TPHCM",
    "rating" : "4.8",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "Nguyễn Công",
    "city" : "DN",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Đại Việt",
    "city" : "TPHCM",
    "rating" : "4.8",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "Long Hân",
    "city" : "HN",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Phúc Thịnh",
    "city" : "TPHCM",
    "rating" : "4.8",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "An Vinh",
    "city" : "DL",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
  {
    "name" : "Ngọc An",
    "city" : "TPHCM",
    "rating" : "4.8",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "An Cường",
    "city" : "GL",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
]
dealer_in_hcm = filter_by_city(authorized_dealers, "TPHCM")

print("Danh sách đại lý ở TPHCM: ")
print(dealer_in_hcm)