<<<<<<< HEAD
grade = float(input("กรุณากรอกคะแนน"))

if grade >=80:
 print ("ค")   
elif grade >=70:
    print ("คุณได้เกรดB")
elif grade >=60 :
    print ("คุณได้เกรดC")
elif grade >=50:
    print ("คุณได้เกรดD")
elif grade < 50:
    print ("คุณได้เกรดF")

# รับค่าคะแนนจากผู้ใช้ และแปลงเป็นทศนิยม (float) เพื่อรองรับคะแนนที่เป็นเศษส่วน
score = float(input("กรุณากรอกคะแนนของนักเรียน: "))

# ตรวจสอบเงื่อนไขเพื่อให้เกรด
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

# แสดงผลลัพธ์
print(f"คะแนนของคุณคือ {score} คะแนน ได้รับเกรด: {grade}")
>>>>>>> fd87a636abe5e6ab20f7a3a8dddc5b6e7dfdd115
