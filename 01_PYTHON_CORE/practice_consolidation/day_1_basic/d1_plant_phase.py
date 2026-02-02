# D.1 phiên bản cơ bản
humidity = 42.5
if (humidity < 25):
  print(" Độ ẩm quá thấp! Cây cần tưới nước!")
elif (humidity >= 25 and humidity <= 50):
  print("Độ ẩm tối ưu cho cây")
else:
  print("Độ ẩm quá cao! Cây cần thoát nước!")
  
# D.1 phiên bản refactor
def humidity_check(humidity):
  if (humidity < 25):
    return "Độ ẩm quá thấp! Cây cần tưới nước!"
  elif (humidity >= 25 and humidity <= 50):
    return "Độ ẩm tối ưu cho cây"
  else:
    return "Độ ẩm quá cao! Cây cần thoát nước!"
result = humidity_check(55)
print(result)