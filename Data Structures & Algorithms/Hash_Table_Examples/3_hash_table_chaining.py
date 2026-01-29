"""
HashTableWithChaining - Hash Table với xử lý collision bằng Chaining
Mỗi bucket là một list chứa các tuple (key, value)
"""


class HashTableWithChaining:
    """
    Hash Table với xử lý collision bằng Chaining
    Mỗi bucket là một list chứa các tuple (key, value)
    """
    
    def __init__(self, size=10):
        """Khởi tạo hash table với kích thước mặc định là 10"""
        self.size = size
        self.table = [[] for _ in range(size)]  # Mỗi bucket là một list rỗng
    
    def hash(self, key):
        """Hash function cho key"""
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            p = 31
            hash_value = 0
            power = 1
            for char in key:
                hash_value = (hash_value + ord(char) * power) % self.size
                power = (power * p) % self.size
            return hash_value
        else:
            return self.hash(str(key))
    
    def insert(self, key, value):
        """Thêm cặp key-value vào hash table (xử lý collision)"""
        index = self.hash(key)
        bucket = self.table[index]
        
        # Kiểm tra xem key đã tồn tại chưa
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Key đã tồn tại, cập nhật value
                bucket[i] = (key, value)
                print(f"✓ Đã cập nhật '{key}' -> {value} tại index {index}")
                return
        
        # Key chưa tồn tại, thêm mới
        bucket.append((key, value))
        print(f"✓ Đã thêm '{key}' -> {value} tại index {index} (bucket size: {len(bucket)})")
    
    def get(self, key):
        """Lấy value theo key"""
        index = self.hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None  # Không tìm thấy
    
    def delete(self, key):
        """Xóa cặp key-value"""
        index = self.hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                print(f"✓ Đã xóa '{key}' tại index {index}")
                return True
        return False
    
    def contains(self, key):
        """Kiểm tra key có tồn tại không"""
        return self.get(key) is not None
    
    def display(self):
        """Hiển thị toàn bộ hash table"""
        print("\n=== Hash Table (Chaining) ===")
        for i in range(self.size):
            bucket = self.table[i]
            if bucket:
                items = [f"'{k}':{v}" for k, v in bucket]
                print(f"Index {i}: [{', '.join(items)}]")
            else:
                print(f"Index {i}: []")
        print("=" * 40)


if __name__ == "__main__":
    # Tạo hash table
    ht = HashTableWithChaining(size=5)
    
    # Thêm các phần tử - bao gồm collision
    print("Thêm các phần tử (bao gồm collision):")
    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("cherry", 300)
    ht.insert(1, "one")
    ht.insert(6, "six")   # 6 % 5 = 1 -> collision với key=1, nhưng vẫn OK!
    ht.insert(11, "eleven")  # 11 % 5 = 1 -> collision nữa!
    
    ht.display()
    
    # Truy xuất
    print("\nTruy xuất:")
    print(f"get('apple'): {ht.get('apple')}")
    print(f"get(1): {ht.get(1)}")
    print(f"get(6): {ht.get(6)}")  # ✅ Không còn bị ghi đè!
    print(f"get(11): {ht.get(11)}")
    
    # Kiểm tra
    print("\nKiểm tra:")
    print(f"contains('apple'): {ht.contains('apple')}")
    print(f"contains('grape'): {ht.contains('grape')}")
    
    # Xóa
    print("\nXóa:")
    ht.delete("banana")
    ht.display()
