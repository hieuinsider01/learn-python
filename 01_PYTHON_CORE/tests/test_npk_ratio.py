from utils import suggest_npk_ratio

# Quy tắc: Tên hàm Test luôn phải bắt đầu bằng 'test_'
def test_stage_1_return_high_nitrogen():
  """Kiểm tra Giai đoạn 1 có trả về công thức N cao không"""
  expected_result = "NPK 30-10-10" # Kết quả mong đợi
  actual_result = suggest_npk_ratio(1) # Chạy hàm với input = 1
  assert actual_result == expected_result # So sánh kết quả thực tế với kết quả mong đợi
  
  """Kiểm tra khi nhập giai đoạn không hợp lệ"""
  expected_result = "Giai đoạn cây trồng không hợp lệ"
  actual_result = suggest_npk_ratio(99)
  assert actual_result == expected_result