# D.2 Phiên bản cơ bản
base_dosage = [100, 150, 200]
for index, dosage in enumerate(base_dosage, start=1):
  print(f"Liều lượng {index} là {dosage}ml")
  
# D.2 Phiên bản refactor
def dosage_usage():
  base_dosage = [100, 150, 200]
  fortmatted_list = [f"Liều lượng {i} là {d}ml" for i, d in enumerate(base_dosage, start=1)]
  result = fortmatted_list
  return ".\n".join(result)
dosage_usage()