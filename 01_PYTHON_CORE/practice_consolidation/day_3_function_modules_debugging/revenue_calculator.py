def calculate_revenue(price, quantity):
  total_revenue = price * quantity
  return total_revenue

# K.1 Phiên bản cơ bản
def print_report(item_name, price, quantity):
  total_revenue = calculate_revenue(price, quantity)
  
  report_string = f"Báo cáo doanh thu sản phẩm {item_name} đã bán được {quantity} đơn vị với giá {price}. Tổng doanh thu là: {total_revenue} VND."
  return report_string
print(print_report("Phân Bón A", 50000, 100))

#K.1 Phiên bản refactor
def formatted_revenue(report_revenue):
  formatted = f"{report_revenue:,.0f}".replace(",", "v").replace(".", ",").replace("v", ".")
  return formatted

def process_report(item_name, price, quantity):
  report_revenue = calculate_revenue(price, quantity)
  final_revenue = formatted_revenue(report_revenue)
  report_string = f"Báo cáo doanh thu sản phẩm: {item_name} đã bán được {quantity} đơn vị với giá {price}. Tổng doanh thu là: {final_revenue}"
  return report_string
print(process_report("Phân NPK 30-10-10", 500000, 50))