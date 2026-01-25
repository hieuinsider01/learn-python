- Trong List chỉ chứa giá trị, không chứa phép gán

- Cú pháp truy cập key-value của 1 dict lồng trong 1 list:

  Syntax: `variable = list_name[index][key]`
  => Trong đó `index` là giá trị (vị trí của dict trong list chứa nó(bắt đầu từ 0))

- Hoặc để an toàn hơn (tránh trường hợp lỗi khi key không tồn tại) thì chúng ta sẽ dùng `get()`:

  Syntax: `variable = list_name[index].get("key", "Giá trị mặc định")`

- dùng set() để biến đổi 1 list thành 1 set. Kết quả trả về sẽ là 1 danh sách các phần tử độc nhất (unique, không trùng lặp)
  Syntax: `variable = set(old_list)`
  => Lúc này variable sẽ là 1 set
