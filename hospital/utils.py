import re
import requests
import datetime
from os import path
from hospital_ms import settings

headers = {"Accept": "*/*"}

url = "https://developer.safaricom.co.ke/api/v1/APIs/API/Simulate/MpesaExpressSimulate/"


def send_payment_push(phone_number: str, amount: int, account_reference: str):
    # 检查是否是模拟模式
    # 如果 settings.MPESA_TOKEN 或 settings.MPESA_AUTHORIZATION 为空字符串，则进入模拟模式
    if not settings.MPESA_TOKEN or not settings.MPESA_AUTHORIZATION:
        print(f"模拟模式：向 {phone_number} 发送 {amount} 的支付请求 (金额: {amount})")
        # 在模拟模式下，我们直接返回，不执行后续的 API 调用代码
        return

    # 以下是实际调用 MPESA API 的代码，只在非模拟模式下执行
    if re.match(r"(^07|^011)", phone_number):
        phone_number = int(phone_number)
    elif re.match(r"^\+254", phone_number):
        phone_number = int(phone_number[4:])
    else:
        # 即使在模拟模式下，手机号码格式验证仍然保留
        raise ValueError(f"Invalid phone number.")

    phone_number = f"254{phone_number}"
    payload = {
        "token": settings.MPESA_TOKEN,
        "authorization": settings.MPESA_AUTHORIZATION,
        "BusinessShortCode": "174379",
        "password": settings.MPESA_PASSWORD,
        "timestamp": settings.MPESA_TIMESTAMP,
        "TransactionType": "CustomerPayBillOnline",
        "amount": amount,
        "PartyA": "254708374149",
        "PartyB": "174379",
        "PhoneNumber": phone_number,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": account_reference,
        "TransactionDesc": "Payment of X",
    }
    resp = requests.post(url=url, json=payload, headers=headers)
    resp.raise_for_status()


def generate_document_filepath(instance, filename: str) -> str:
    filename, extension = path.splitext(filename)
    return f"{instance.__class__.__name__.lower()}/{filename}_{instance.id or ''}{extension}"


if __name__ == "__main__":
    send_payment_push("0748981989", 100, "developer")
