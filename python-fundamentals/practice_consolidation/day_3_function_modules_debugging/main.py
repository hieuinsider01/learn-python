from utils import *
# K.2 phiên bản cơ bản
def show_name_uppercase():
  coffee = {
    "name": "Cà phê",
    "grow_day" : 180,
    "temperature" : "27°C",
    "disease" : ["Rệp sáp", "Rầy nâu", "Rỉ sắt", "Sâu đục thân"]
  }
  result = get_plants_name(coffee)
  return result
print(show_name_uppercase())

# K.2 phiên bản refactor
def good_show_name_uppercase():
  coffee = {
    "name": "Cà phê",
    "grow_day" : 180,
    "temperature" : "27°C",
    "disease" : ["Rệp sáp", "Rầy nâu", "Rỉ sắt", "Sâu đục thân"]
  }
  result = good_get_plants_name(coffee)
  if result["status"] == "success":
    return f"Tên cây trồng là {result['value']}"
  else:
    return f"Lỗi: {result['message']}"
print(good_show_name_uppercase())