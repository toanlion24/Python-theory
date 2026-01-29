"""
Ứng dụng thực tế của Hash Table
Các ví dụ: đếm tần suất, kiểm tra trùng lặp, Two Sum
"""


def count_frequency(text):
    """
    Đếm số lần xuất hiện của mỗi từ trong văn bản
    Sử dụng hash table (dict)
    """
    words = text.lower().split()
    frequency = {}  # Hash table
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency


def has_duplicate(arr):
    """
    Kiểm tra mảng có phần tử trùng lặp không (sử dụng hash set)
    Time Complexity: O(n)
    """
    seen = set()  # Hash set (chỉ lưu keys, không lưu values)
    
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


def two_sum(nums, target):
    """
    Tìm 2 số trong mảng có tổng bằng target
    Trả về indices của 2 số đó
    Sử dụng hash table để đạt O(n) thay vì O(n²)
    
    Args:
        nums: List các số nguyên
        target: Số mục tiêu
    
    Returns:
        List 2 indices hoặc None nếu không tìm thấy
    """
    num_map = {}  # {num: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return None


if __name__ == "__main__":
    # Ví dụ 1: Đếm tần suất xuất hiện
    print("=" * 60)
    print("1. Đếm tần suất xuất hiện của các từ")
    print("=" * 60)
    text = "the quick brown fox jumps over the lazy dog the fox is quick"
    freq = count_frequency(text)
    
    print("Tần suất xuất hiện của các từ:")
    for word, count in sorted(freq.items()):
        print(f"  '{word}': {count}")
    
    # Ví dụ 2: Kiểm tra phần tử trùng lặp
    print("\n" + "=" * 60)
    print("2. Kiểm tra phần tử trùng lặp")
    print("=" * 60)
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 2, 4]
    
    print(f"{arr1} có trùng lặp? {has_duplicate(arr1)}")
    print(f"{arr2} có trùng lặp? {has_duplicate(arr2)}")
    
    # Ví dụ 3: Two Sum
    print("\n" + "=" * 60)
    print("3. Tìm cặp phần tử có tổng bằng target (Two Sum)")
    print("=" * 60)
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    if result:
        idx1, idx2 = result
        print(f"Output: {result}")
        print(f"Giải thích: nums[{idx1}] + nums[{idx2}] = {nums[idx1]} + {nums[idx2]} = {target}")
    else:
        print("Không tìm thấy!")
    
    # Ví dụ 4: Two Sum với test case khác
    print("\n" + "-" * 60)
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    if result2:
        idx1, idx2 = result2
        print(f"Output: {result2}")
        print(f"Giải thích: nums[{idx1}] + nums[{idx2}] = {nums2[idx1]} + {nums2[idx2]} = {target2}")
