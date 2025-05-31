import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_ms.settings')
django.setup()

from finance.models import Account

# 创建M-PESA账户
mpesa_account = Account.objects.create(
    name="M-PESA",
    paybill_number="174379",  # 这是Safaricom的测试paybill号码
    account_number="%(username)s",  # 使用用户名作为账户号码
    is_active=True,
    details="M-PESA支付账户"
)

print("M-PESA账户创建成功！") 