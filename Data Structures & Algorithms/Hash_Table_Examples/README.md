# Hash Table Examples - Các Ví Dụ về Hash Table

Folder này chứa các ví dụ triển khai và ứng dụng của Hash Table trong Python.

## Cấu trúc File

### 1. `1_hash_functions.py`
Các hàm băm (hash functions) cơ bản:
- `simple_hash_integer()`: Hash function cho số nguyên
- `simple_hash_string()`: Hash function đơn giản cho chuỗi
- `improved_hash_string()`: Hash function cải tiến cho chuỗi (polynomial rolling hash)

**Chạy:**
```bash
python 1_hash_functions.py
```

### 2. `2_simple_hash_table.py`
Hash Table đơn giản - **không xử lý collision**
- Class: `SimpleHashTable`
- Khi có collision, value sau sẽ ghi đè value trước

**Chạy:**
```bash
python 2_simple_hash_table.py
```

### 3. `3_hash_table_chaining.py`
Hash Table với xử lý collision bằng **Chaining**
- Class: `HashTableWithChaining`
- Mỗi bucket là một list chứa các tuple (key, value)

**Chạy:**
```bash
python 3_hash_table_chaining.py
```

### 4. `4_hash_table_linear_probing.py`
Hash Table với xử lý collision bằng **Linear Probing**
- Class: `HashTableWithLinearProbing`
- Khi collision, tìm vị trí trống tiếp theo

**Chạy:**
```bash
python 4_hash_table_linear_probing.py
```

### 5. `5_applications.py`
Ứng dụng thực tế của Hash Table:
- `count_frequency()`: Đếm tần suất xuất hiện của từ
- `has_duplicate()`: Kiểm tra phần tử trùng lặp
- `two_sum()`: Tìm 2 số có tổng bằng target

**Chạy:**
```bash
python 5_applications.py
```

### 6. `6_python_dict_demo.py`
Demo sử dụng Dictionary trong Python (được triển khai bằng Hash Table):
- Các thao tác cơ bản với dict
- So sánh hiệu suất với List
- Các tính năng đặc biệt

**Chạy:**
```bash
python 6_python_dict_demo.py
```

## So sánh các kỹ thuật xử lý Collision

| Đặc điểm | Chaining | Linear Probing |
|----------|----------|----------------|
| **Lưu trữ** | Mỗi bucket là list | Mỗi vị trí là một entry |
| **Khi collision** | Thêm vào list | Tìm vị trí trống tiếp theo |
| **Load factor** | Có thể > 1 | Phải ≤ 1 |
| **Xóa** | Đơn giản | Cần rehash |
| **Tốc độ** | Tốt khi ít collision | Nhanh hơn khi ít collision |

## Time Complexity

| Thao tác | Best Case | Average Case | Worst Case |
|----------|-----------|--------------|------------|
| **Search** | O(1) | O(1) | O(n) |
| **Insert** | O(1) | O(1) | O(n) |
| **Delete** | O(1) | O(1) | O(n) |

*Worst case xảy ra khi tất cả keys có cùng hash value (rất hiếm với hash function tốt)*

## Yêu cầu

- Python 3.6+
- Không cần thư viện bên ngoài

## Ghi chú

- Tất cả các ví dụ đều có thể chạy độc lập
- Mỗi file đều có `if __name__ == "__main__":` để demo
- Code có comment tiếng Việt để dễ hiểu

## Đọc thêm

Xem notebook chi tiết: `03_Hash_Table.ipynb`
