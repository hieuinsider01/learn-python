from drug import Drug
def load_inventory():
  return []

# Thêm thuốc
def add_drug(inventory):
  name = input("Nhập tên thuốc: ")
  try:
    quantity = int(input("Nhập số lượng: "))
    price = float(input("Nhập giá: "))
  except ValueError:
    print("Số lượng phải là số nguyên và giá phải là số thực.")
    return
  new_drug = Drug(name=name, quantity=quantity, price=price)
  inventory.append(new_drug)
  print(f"Đã thêm thuốc: {name}")
def search_drug(inventory, search_term):
  results = [drug for drug in inventory if search_term["name"] in drug.name]
  return results
def save_inventory(inventory):
  with open("inventory.txt", "w", encoding="utf-8") as f:
    for drug in inventory:
      f.write(f"{drug.name},{drug.quantity},{drug.price}\n")
