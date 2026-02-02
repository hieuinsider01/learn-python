# T.3 phiên bản cơ bản
weekly_diagnoses = ["Đốm lá", "Thán thư", "Rệp sáp", "Đốm lá", "Bệnh vàng lá", "Thán thư"]
unique_disease = set(weekly_diagnoses)

disease_count = len(unique_disease)

disease_str = ", ".join(sorted(unique_disease))
print(f"Có {disease_count} bệnh đang xuất hiện trong vườn, bao gồm: {disease_str}")

# T.3 phiên bản refactor
def duplicate_checker():
  weekly_diagnoses = ["Đốm lá", "Thán thư", "Rệp sáp", "Đốm lá", "Bệnh vàng lá", "Thán thư"]
  unique_disease = set(weekly_diagnoses)
  disease_count = len(unique_disease)
  disease_str = ", ".join(sorted(unique_disease))
  return f"Có {disease_count} loại bệnh đang xuất hiện trong vườn, bao gồm: {disease_str} "
result = duplicate_checker()
print(result)