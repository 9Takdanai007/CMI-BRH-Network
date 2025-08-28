from datetime import datetime

#Data for calculation DRG
"""
Fuction check_PDx
asdasd
"""
def check_PDx(PDx):
    if PDx[0] in ["V","W","X","Y"]:
        return "ERROR"
    else:
        return PDx
"""
Fuction check_Age
asdasd
"""  
def check_AgeDay(AgeDay):
    if AgeDay>=0 and AgeDay<=365:
        return AgeDay
    else:
        return "ERROR"
    
def calculate_age(date_adm, dob):
    """
    คำนวณ Age (ปี) และ AgeDay (วัน)
    date_adm, dob: datetime objects
    """
    # ส่วนต่างของวันทั้งหมด
    delta = date_adm - dob
    days = delta.days

    # อายุเป็นปี (เต็มปี)
    years = date_adm.year - dob.year
    if (date_adm.month, date_adm.day) < (dob.month, dob.day):
        years -= 1

    # อายุเป็นวัน (เฉพาะกรณี < 1 ปี)
    age_day = days if years == 0 else None

    return years, age_day


PDx_input = input("กรอก PDx : ") # Principal Diagnosis มีได้แค่อันเดียว // จำเป็นต้องมี // อ้างอิงรหัสจาก ICD-10 (2016) และ ICD-10-TM (2016)
SDx_input = input("กรอก SDx : ") # Secondary Diagnosis มีได้ไม่เกิน 12 // ไม่มีก็ได้
Proc_input = input("กรอก Pro : ") # Procedure มีได้ไม่เกิน 12 // ไม่มีก็ได้ // อ้างอิงรหัสจาก ICD-9-CM (ฉบับปี 2015)

# --- รับค่า Input จากผู้ใช้ ---
dob_input = input("กรอกวันเกิด (รูปแบบ YYYY-MM-DD): ")
date_adm_input = input("กรอกวันเข้ารพ. (รูปแบบ YYYY-MM-DD): ")

# แปลง string → datetime
dob = datetime.strptime(dob_input, "%Y-%m-%d")
date_adm = datetime.strptime(date_adm_input, "%Y-%m-%d")

# คำนวณ
age, age_day = calculate_age(date_adm, dob)

# แสดงผล
print(f"\nAge (ปี): {age}")
if age_day is not None:
    print(f"AgeDay (วัน): {age_day}")
else:
    print("AgeDay: - (ไม่ใช้เพราะอายุมากกว่า 1 ปี)")

check_PDx(PDx_input) # Admission weight

AdmWt_input = input("กรอก AdmWt :") 

Sex_input = input("Sex : ")
Discht_input = input("Discht : ")

DateDsc_input = input("DateDsc : ")
TimeDsc_input = input("TimeDsc : ")
Leave_day_input = input("Leave day : ")
los_input = input("los_input : ") #TEST
