def fusili_core(a, b, c):
    return (a ^ b) + (b ^ c) - (a & c)


def compute_fusili_number(nums):
    while len(nums) > 1:
        if len(nums) % 3 != 0:
            nums.extend([0] * (3 - len(nums) % 3))

        new_list = []
        for i in range(0, len(nums), 3):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            new_list.append(fusili_core(a, b, c))
        nums = new_list
    return nums[0]


# Read input
data = list(map(int, input().split()))
final_number = compute_fusili_number(data)

if final_number % 2 == 0:
    print("Фусли е доволна!")
else:
    print("Фусли е объркана...")