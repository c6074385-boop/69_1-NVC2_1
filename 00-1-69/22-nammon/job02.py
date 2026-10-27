# สินค้าชิ้นที่ 1
<<<<<<< HEAD:00-1-69/22-nammon/job02.py
name1 = input("กรอกชื่อสินค้าชิ้นที่ 1: ")
=======
name1 = input("กรุณากรอกชื่อสินค้าชิ้นที่ 1: ")
>>>>>>> 8ded7c943b6442de8e908f5ff310e991cacd9fc4:22-nammon/job02.py
price1 = float(input("กรอกราคาต่อชิ้นของ " + name1 + ": "))
qty1 = int(input("กรอกจำนวนที่ขายของ " + name1 + ": "))
total1 = price1 * qty1

# สินค้าชิ้นที่ 2
name2 = input("กรอกชื่อสินค้าชิ้นที่ 2: ")
price2 = float(input("กรอกราคาต่อชิ้นของ " + name2 + ": "))
qty2 = int(input("กรอกจำนวนที่ขายของ " + name2 + ": "))

total2 = price2 * qty2

# แสดงผลลัพธ์
print("----- สรุปยอดขายสินค้า -----")
print("สินค้า:", name1, "| ราคาต่อชิ้น:", price1, "| จำนวนที่ขาย:", qty1, "| ยอดรวม:", total1)
print("สินค้า:", name2, "| ราคาต่อชิ้น:", price2, "| จำนวนที่ขาย:", qty2, "| ยอดรวม:", total2)
print("ยอดขายรวมทั้งหมด:", total1 + total2)