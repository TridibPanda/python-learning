class Mobile:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price


samsung = Mobile("Samsung", "64GB", "256GB", 29999)
apple = Mobile("Apple", "64GB", "256GB", 79999)
oneplus = Mobile("OnePlus", "64GB", "128GB", 19999)

print(
    f"Brand: {samsung.brand}, RAM: {samsung.ram}, Storage: {samsung.storage}, Price: {samsung.price}"
)
print(
    f"Brand: {apple.brand}, RAM: {apple.ram}, Storage: {apple.storage}, Price: {apple.price}"
)
print(
    f"Brand: {oneplus.brand}, RAM: {oneplus.ram}, Storage: {oneplus.storage}, Price: {oneplus.price}"
)
# Output:
# Brand: Samsung, RAM: 64GB, Storage: 256GB, Price: 29999
# Brand: Apple, RAM: 64GB, Storage: 256GB, Price: 79999
# Brand: OnePlus, RAM: 64GB, Storage: 128GB, Price: 19999
