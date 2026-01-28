# Yêu cầu 1:
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
    "rating" : "4.4",
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
    "rating" : "4.7",
    "product" : ["Anvil 5SC", "Mancozeb", "Amino Humic"]
  },
  {
    "name" : "An Cường",
    "city" : "GL",
    "rating" : "4.5",
    "product" : ["Ridomil Gold", "Amistar TOP", "Rocsket 888"],
  },
]

# Truy cập và in ra tên đại lý thứ nhất:
dealer_1_name = authorized_dealers[1]["name"]
print(f"{dealer_1_name} là tên của đại lý thứ hai")

# Add products vào danh sách sản phẩm của đại lý thứ nhất
add_new_product = authorized_dealers[0]["product"].append("NPK 15-15-15")

#Kiểm tra danh sách mới của product dealer 1
new_list_product = authorized_dealers[0]["product"]
print(f'Danh sách các sản phẩm sau khi cập nhật của đại lý 1 là: {new_list_product}')

# Yêu cầu 2:

all_loctations = ["Hà Nội", "TP. HCM", "Đà Nẵng", "Hà Nội", "Cần Thơ", "TP. HCM"]

unique_locations = set(all_loctations)
