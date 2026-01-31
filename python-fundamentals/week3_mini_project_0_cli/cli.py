from manager import load_inventory, add_drug, save_inventory
from drug import Drug
def main():
    inventory = load_inventory()
    while True:
        print("\nQuản lý kho thuốc")
        print("1. Thêm thuốc")
        print("2. Hiển thị kho thuốc")
        print("3. Tìm kiếm thuốc")
        print("4. Lưu và thoát")
        choice = input("Chọn một tùy chọn (1-4): ")
        if choice == '1':
            add_drug(inventory)
        elif choice == '2':
            if not inventory:
                print("Kho thuốc trống.")
            else:
                for drug in inventory:
                    print(drug.get_display_info())
        elif choice == '3':
            search_term = input("Nhập tên thuốc cần tìm: ")
            results = [drug for drug in inventory if search_term in drug.name]
            print(f"Đã tìm thấy {len(results)} kết quả:")
            for drug in results:
                print(drug.get_display_info())
        elif choice == '4':
            # from manager import save_inventory
            save_inventory(inventory)
            print("Đã lưu kho thuốc. Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            