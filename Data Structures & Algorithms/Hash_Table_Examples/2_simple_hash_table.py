"""
SimpleHashTable - Hash Table đơn giản (không xử lý collision)
Nếu có 2 key cùng hash value, value sau sẽ ghi đè value trước
"""


class SimpleHashTable:
    """
    Hash Table đơn giản - chưa xử lý collision
    Nếu có 2 key cùng hash value, value sau sẽ ghi đè value trước
    """
    
    def __init__(self, size=10):
        """Khởi tạo hash table với kích thước mặc định là 10"""
        self.size = size
        self.table = [None] * size  # Khởi tạo mảng với None
    
    def hash(self, key):
        """Hash function cho key (hỗ trợ cả int và string)"""
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            # Sử dụng polynomial rolling hash
            p = 31
            hash_value = 0
            power = 1
            for char in key:
                hash_value = (hash_value + ord(char) * power) % self.size
                power = (power * p) % self.size
            return hash_value
        else:
            # Với các kiểu khác, chuyển sang string rồi hash
            return self.hash(str(key))
    
    def insert(self, key, value):
        """Thêm cặp key-value vào hash table"""
        index = self.hash(key)
        self.table[index] = (key, value)  # Lưu tuple (key, value)
        print(f"✓ Đã thêm '{key}' -> {value} tại index {index}")
    
    def get(self, key):
        """Lấy value theo key"""
        index = self.hash(key)
        if self.table[index] is None:
            return None
        stored_key, value = self.table[index]
        if stored_key == key:
            return value
        return None  # Key không khớp (có thể do collision)
    
    def delete(self, key):
        """Xóa cặp key-value"""
        index = self.hash(key)
        if self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                self.table[index] = None
                print(f"✓ Đã xóa '{key}' tại index {index}")
                return True
        return False
    
    def contains(self, key):
        """Kiểm tra key có tồn tại không"""
        return self.get(key) is not None
    
    def display(self):
        """Hiển thị toàn bộ hash table"""
        print("\n=== Hash Table ===")
        for i in range(self.size):
            if self.table[i] is not None:
                key, value = self.table[i]
                print(f"Index {i}: '{key}' -> {value}")
            else:
                print(f"Index {i}: None")
        print("=" * 30)


if __name__ == "__main__":
    # Tạo hash table
    ht = SimpleHashTable(size=5)
    
    # Thêm các phần tử
    print("Thêm các phần tử:")
    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("cherry", 300)
    ht.insert(1, "one")
    ht.insert(6, "six")  # 6 % 5 = 1, sẽ collision với key=1!
    
    ht.display()
    
    # Truy xuất
    print("\nTruy xuất:")
    print(f"get('apple'): {ht.get('apple')}")
    print(f"get('banana'): {ht.get('banana')}")
    print(f"get(1): {ht.get(1)}")
    print(f"get(6): {ht.get(6)}")  # Sẽ bị ghi đè hoặc None
    
    # Kiểm tra collision
    print("\nKiểm tra:")
    print(f"contains('apple'): {ht.contains('apple')}")
    print(f"contains('grape'): {ht.contains('grape')}")
    
    # Xóa
    print("\nXóa:")
    ht.delete("banana")
    ht.display()
