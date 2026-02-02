class Disease:
  def __init__(self, name, cause, is_contagious, suggested_treatment):
    self.name = name
    self.cause = cause
    self.is_contagious = is_contagious
    self.suggested_treatment = suggested_treatment

  def get_summary(self):
    if self.is_contagious == True:
      contagious_status = "Có"
    else:
      contagious_status = "Không"
    treatment_string = ", ".join(self.suggested_treatment)
    return f" {self.name} do {self.cause} gây ra. {contagious_status} khả năng lây lan. Các loại thuốc khuyên dùng là: {treatment_string}"
ba_trau = Disease(
  name = "Bệnh bã trầu",
  cause = "virus",
  is_contagious = True,
  suggested_treatment=["Kasuran", "Xantocin", "Coc 85"]
)

result = ba_trau.get_summary()
print(result)