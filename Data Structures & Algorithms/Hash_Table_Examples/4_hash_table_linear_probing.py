"""
HashTableWithLinearProbing - Hash Table với xử lý collision bằng Linear Probing
Khi collision, tìm vị trí trống tiếp theo
"""


class HashTableWithLinearProbing:
    """
    Hash Table với xử lý collision bằng Linear Probing
    Khi collision, tìm vị trí trống tiếp theo
    """
    
    def __init__(self, size=10):
        """Khởi tạo hash table"""
        self.size = size
        self.table = [None] * size
        self.count = 0  # Số phần tử hiện tại
    
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
    
    def _find_index(self, key):
        """
        Tìm index để insert hoặc get key
        Trả về index nếu tìm thấy vị trí phù hợp, None nếu không
        """
        index = self.hash(key)
        start_index = index
        
        # Linear probing: tìm vị trí trống hoặc có cùng key
        while True:
            if self.table[index] is None:
                return index  # Vị trí trống
            stored_key, _ = self.table[index]
            if stored_key == key:
                return index  # Tìm thấy key
            index = (index + 1) % self.size  # Vị trí tiếp theo (wrap around)
            if index == start_index:
                return None  # Hash table đầy
    
    def _find_key_index(self, key):
        """Tìm index của key (chỉ dùng cho get/delete)"""
        index = self.hash(key)
        start_index = index
        
        while self.table[index] is not None:
            stored_key, _ = self.table[index]
            if stored_key == key:
                return index
            index = (index + 1) % self.size
            if index == start_index:
                break
        return None
    
    def insert(self, key, value):
        """Thêm cặp key-value (sử dụng linear probing khi collision)"""
        if self.count >= self.size:
            print("⚠️ Hash table đầy!")
            return False
        
        index = self._find_index(key)
        if index is None:
            print("⚠️ Không thể thêm - hash table đầy!")
            return False
        
        if self.table[index] is None:
            self.count += 1
            print(f"✓ Đã thêm '{key}' -> {value} tại index {index}")
        else:
            print(f"✓ Đã cập nhật '{key}' -> {value} tại index {index}")
        
        self.table[index] = (key, value)
        return True
    
    def get(self, key):
        """Lấy value theo key"""
        index = self._find_key_index(key)
        if index is not None:
            _, value = self.table[index]
            return value
        return None
    
    def delete(self, key):
        """Xóa cặp key-value"""
        index = self._find_key_index(key)
        if index is not None:
            self.table[index] = None
            self.count -= 1
            print(f"✓ Đã xóa '{key}' tại index {index}")
            
            # Rehash các phần tử tiếp theo trong cluster
            next_index = (index + 1) % self.size
            while self.table[next_index] is not None:
                k, v = self.table[next_index]
                self.table[next_index] = None
                self.count -= 1
                self.insert(k, v)  # Reinsert
                next_index = (next_index + 1) % self.size
            
            return True
        return False
    
    def contains(self, key):
        """Kiểm tra key có tồn tại không"""
        return self.get(key) is not None
    
    def display(self):
        """Hiển thị toàn bộ hash table"""
        print(f"\n=== Hash Table (Linear Probing) [Count: {self.count}/{self.size}] ===")
        for i in range(self.size):
            if self.table[i] is not None:
                key, value = self.table[i]
                print(f"Index {i}: '{key}' -> {value}")
            else:
                print(f"Index {i}: None")
        print("=" * 50)


if __name__ == "__main__":
    # Tạo hash table
    ht = HashTableWithLinearProbing(size=5)
    
    # Thêm các phần tử
    print("Thêm các phần tử:")
    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("cherry", 300)
    ht.insert(1, "one")
    ht.insert(6, "six")  # 6 % 5 = 1 -> collision, sẽ tìm vị trí tiếp theo
    
    ht.display()
    
    # Truy xuất
    print("\nTruy xuất:")
    print(f"get('apple'): {ht.get('apple')}")
    print(f"get(1): {ht.get(1)}")
    print(f"get(6): {ht.get(6)}")  # ✅ Tìm được!
    
    # Xóa
    print("\nXóa:")
    ht.delete("banana")
    ht.display()
