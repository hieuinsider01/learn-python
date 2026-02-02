# K.2 util phiên bản cơ bản
def get_plants_name(full_data):
  name_uppercase = full_data['name'].upper()
  return name_uppercase

# K.2 utils phiên bản refactor
def good_get_plants_name(full_data):
  try:
    name_uppercase = full_data['name'].upper()
    return {
      "status": "success",
      "value" : name_uppercase
    }
  except KeyError:
    return {
      "status" : "error",
      "message" :"Key 'name' không tồn tại trong dữ liệu"
    }