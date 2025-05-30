import os
import django
from datetime import datetime, timedelta
from decimal import Decimal

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_ms.settings')
django.setup()

# 导入模型
from users.models import CustomUser
from hospital.models import Medicine, Patient, Treatment, TreatmentMedicine
from staffing.models import Department, Speciality, WorkingDay, Doctor
from external.models import About, ServiceFeedback
from finance.models import Account, ExtraFee

def create_initial_data():
    # 创建医院基本信息
    about = About.objects.create(
        name="智慧医院",
        short_name="ZH",
        slogan="科技守护健康",
        details="欢迎来到智慧医院。我们致力于提供最优质的医疗服务。",
        location_name="北京市海淀区",
        latitude=39.9042,
        longitude=116.4074,
        founded_in=datetime.now().date(),
        founder_name="智慧医疗集团",
        mission="为所有人提供优质的医疗服务",
        vision="成为区域内领先的医疗保健提供商",
        email="contact@zhhospital.com",
        phone_number="010-12345678",
        facebook="https://www.facebook.com/zhhospital",
        twitter="https://twitter.com/zhhospital",
        linkedin="https://www.linkedin.com/company/zhhospital",
        instagram="https://www.instagram.com/zhhospital",
        tiktok="https://www.tiktok.com/@zhhospital",
        youtube="https://www.youtube.com/zhhospital"
    )

    # 创建工作日
    working_days = [
        {"name": "Monday"},
        {"name": "Tuesday"},
        {"name": "Wednesday"},
        {"name": "Thursday"},
        {"name": "Friday"}
    ]
    for day in working_days:
        WorkingDay.objects.create(**day)

    # 创建部门
    departments = [
        {"name": "内科", "details": "处理内部疾病和慢性病"},
        {"name": "外科", "details": "进行各类外科手术"},
        {"name": "儿科", "details": "专门治疗儿童疾病"},
        {"name": "妇产科", "details": "处理女性健康和生育问题"},
        {"name": "眼科", "details": "治疗眼部疾病"},
        {"name": "口腔科", "details": "处理口腔和牙齿问题"},
        {"name": "皮肤科", "details": "治疗皮肤相关疾病"},
        {"name": "骨科", "details": "处理骨骼和关节问题"},
        {"name": "神经科", "details": "治疗神经系统疾病"},
        {"name": "心理科", "details": "提供心理健康服务"}
    ]

    for dept in departments:
        Department.objects.create(**dept)

    # 创建专科
    specialities = [
        {
            "name": "心脏病学",
            "department": Department.objects.get(name="内科"),
            "details": "诊断和治疗心脏相关疾病",
            "appointment_charges": Decimal("200.00"),
            "treatment_charges": Decimal("2000.00"),
            "appointments_limit": 20
        },
        {
            "name": "消化内科",
            "department": Department.objects.get(name="内科"),
            "details": "治疗消化系统疾病",
            "appointment_charges": Decimal("150.00"),
            "treatment_charges": Decimal("1500.00"),
            "appointments_limit": 25
        },
        {
            "name": "普外科",
            "department": Department.objects.get(name="外科"),
            "details": "进行常规外科手术",
            "appointment_charges": Decimal("300.00"),
            "treatment_charges": Decimal("3000.00"),
            "appointments_limit": 15
        }
    ]

    for spec in specialities:
        Speciality.objects.create(**spec)

    # 创建药品
    medicines = [
        {
            "name": "阿莫西林",
            "short_name": "AMX",
            "category": Medicine.MedicineCategory.ANTIBIOTICS.value,
            "description": "广谱抗生素，用于治疗细菌感染",
            "expiry_date": datetime.now().date() + timedelta(days=365),
            "price": Decimal("15.00"),
            "stock": 1000
        },
        {
            "name": "布洛芬",
            "short_name": "IBU",
            "category": Medicine.MedicineCategory.PAIN_RELIEF.value,
            "description": "非甾体抗炎药，用于缓解疼痛和发热",
            "expiry_date": datetime.now().date() + timedelta(days=365),
            "price": Decimal("8.00"),
            "stock": 2000
        },
        {
            "name": "维生素C片",
            "short_name": "VITC",
            "category": Medicine.MedicineCategory.VITAMINS.value,
            "description": "补充维生素C，增强免疫力",
            "expiry_date": datetime.now().date() + timedelta(days=365),
            "price": Decimal("12.00"),
            "stock": 1500
        }
    ]

    for med in medicines:
        Medicine.objects.create(**med)

    # 创建支付账户
    accounts = [
        {
            "name": "微信支付",
            "paybill_number": "wxpay",
            "account_number": "%(username)s",
            "details": "使用微信扫码支付"
        },
        {
            "name": "支付宝",
            "paybill_number": "alipay",
            "account_number": "%(username)s",
            "details": "使用支付宝扫码支付"
        }
    ]

    for acc in accounts:
        Account.objects.create(**acc)

    # 创建额外费用类型
    extra_fees = [
        {
            "name": "X光检查",
            "details": "胸部X光检查",
            "amount": Decimal("100.00")
        },
        {
            "name": "CT扫描",
            "details": "全身CT扫描",
            "amount": Decimal("500.00")
        },
        {
            "name": "核磁共振",
            "details": "全身核磁共振检查",
            "amount": Decimal("1000.00")
        }
    ]

    for fee in extra_fees:
        ExtraFee.objects.create(**fee)

    # 创建医生用户和医生记录
    doctors_data = [
        {
            "username": "zhang_doctor",
            "password": "doctor123",
            "first_name": "张",
            "last_name": "医生",
            "gender": "M",
            "date_of_birth": datetime(1980, 1, 1).date(),
            "phone_number": "13800138001",
            "location": "北京市",
            "role": "Doctor",
            "speciality": "心脏病学",
            "shift": "Day",
            "salary": Decimal("15000.00")
        },
        {
            "username": "li_doctor",
            "password": "doctor123",
            "first_name": "李",
            "last_name": "医生",
            "gender": "F",
            "date_of_birth": datetime(1985, 6, 15).date(),
            "phone_number": "13800138002",
            "location": "北京市",
            "role": "Doctor",
            "speciality": "消化内科",
            "shift": "Day",
            "salary": Decimal("14000.00")
        },
        {
            "username": "wang_doctor",
            "password": "doctor123",
            "first_name": "王",
            "last_name": "医生",
            "gender": "M",
            "date_of_birth": datetime(1978, 12, 20).date(),
            "phone_number": "13800138003",
            "location": "北京市",
            "role": "Doctor",
            "speciality": "普外科",
            "shift": "Day",
            "salary": Decimal("16000.00")
        }
    ]

    for doc_data in doctors_data:
        # 创建医生用户
        user = CustomUser.objects.create_user(
            username=doc_data["username"],
            password=doc_data["password"],
            first_name=doc_data["first_name"],
            last_name=doc_data["last_name"],
            gender=doc_data["gender"],
            date_of_birth=doc_data["date_of_birth"],
            phone_number=doc_data["phone_number"],
            location=doc_data["location"],
            role=doc_data["role"]
        )
        
        # 创建医生记录
        doctor = Doctor.objects.create(
            user=user,
            speciality=Speciality.objects.get(name=doc_data["speciality"]),
            shift=doc_data["shift"],
            salary=doc_data["salary"]
        )
        
        # 设置工作日
        doctor.working_days.set(WorkingDay.objects.all())

    print("初始数据创建完成！")

if __name__ == "__main__":
    create_initial_data() 