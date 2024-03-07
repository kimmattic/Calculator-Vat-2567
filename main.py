def calculate_income_tax(income):
    # กำหนดช่วงรายได้แต่ละขั้น
    income_ranges = [150000, 300000, 500000, 750000, 1000000]
    tax_rates = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]

    # คำนวณภาษี
    tax = 0
    remaining_income = income

    for i in range(len(income_ranges)):
        if remaining_income <= 0:
            break
        if i == len(income_ranges) - 1 or remaining_income <= income_ranges[i + 1] - income_ranges[i]:
            tax += remaining_income * tax_rates[i]
            break
        else:
            tax += (income_ranges[i + 1] - income_ranges[i]) * tax_rates[i]
            remaining_income -= (income_ranges[i + 1] - income_ranges[i])

    return tax


# รายได้
income = float(input("กรุณาป้อนรายได้ของคุณ: "))

# เรียกใช้ฟังก์ชันคำนวณภาษี
tax = calculate_income_tax(income)

# แสดงผลลัพธ์
print(f"ภาษีรายได้ของคุณ: {tax:.2f} บาท")
