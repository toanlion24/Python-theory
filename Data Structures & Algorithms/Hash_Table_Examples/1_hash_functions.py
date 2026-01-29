"""
Hash Functions - Các hàm băm
Các ví dụ về hash function cho số nguyên và chuỗi
"""


def simple_hash_integer(key, size):
    """
    Hash function đơn giản cho số nguyên
    Sử dụng phép chia lấy dư (modulo)
    """
    return key % size


def simple_hash_string(key, size):
    """
    Hash function cho chuỗi
    Tính tổng ASCII của các ký tự rồi chia lấy dư
    """
    hash_value = 0
    for char in key:
        hash_value += ord(char)  # ord() trả về mã ASCII của ký tự
    return hash_value % size


def improved_hash_string(key, size):
    """
    Hash Function cải tiến cho chuỗi (polynomial rolling hash)
    Sử dụng polynomial rolling hash
    Công thức: hash = (char_0 * p^0 + char_1 * p^1 + ...) % m
    
    p: số nguyên tố (thường là 31 hoặc 37)
    m: kích thước hash table
    """
    p = 31  # Số nguyên tố
    hash_value = 0
    power = 1
    
    for char in key:
        hash_value = (hash_value + ord(char) * power) % size
        power = (power * p) % size
    
    return hash_value


if __name__ == "__main__":
    # Ví dụ 1: Hash function cho số nguyên
    print("=" * 50)
    print("1. Hash Function cho số nguyên")
    print("=" * 50)
    size = 10
    keys = [5, 15, 25, 35, 45]
    print("Hash values cho các keys:")
    for key in keys:
        hash_value = simple_hash_integer(key, size)
        print(f"Key {key:3d} -> Hash: {hash_value}")
    
    # Ví dụ 2: Hash function cho chuỗi (đơn giản)
    print("\n" + "=" * 50)
    print("2. Hash Function cho chuỗi (đơn giản)")
    print("=" * 50)
    size = 10
    strings = ["apple", "banana", "cherry", "date"]
    print("Hash values cho các chuỗi:")
    for s in strings:
        hash_value = simple_hash_string(s, size)
        print(f"'{s}' -> Hash: {hash_value}")
    
    # Ví dụ 3: Kiểm tra collision
    print("\n" + "=" * 50)
    print("3. Kiểm tra Collision với hash function đơn giản")
    print("=" * 50)
    s1, s2 = "ab", "ba"
    print(f"'{s1}' -> Hash: {simple_hash_string(s1, size)}")
    print(f"'{s2}' -> Hash: {simple_hash_string(s2, size)}")
    if simple_hash_string(s1, size) == simple_hash_string(s2, size):
        print("⚠️ COLLISION xảy ra!")
    
    # Ví dụ 4: So sánh hash functions
    print("\n" + "=" * 50)
    print("4. So sánh Hash Functions (Simple vs Improved)")
    print("=" * 50)
    size = 10
    strings = ["apple", "banana", "cherry", "ab", "ba"]
    
    print(f"{'String':<10} {'Simple Hash':<12} {'Improved Hash':<15}")
    print("-" * 40)
    for s in strings:
        simple = simple_hash_string(s, size)
        improved = improved_hash_string(s, size)
        print(f"'{s}':{'':<6} {simple:<12} {improved:<15}")
