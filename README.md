<h1 align="center">Hospital Management System <img src="backend/hospital/static/hospital/img/logo.png" width="48px"/> </h1>

<p align="center">
<a href=""><img alt="Backend Admin - Django" src="https://img.shields.io/static/v1?logo=django&color=Blue&message=Admin&label=Django"/></a>
<a href=""><img alt="Backend API - FastAPI" src="https://img.shields.io/static/v1?logo=fastapi&color=Blue&message=RestAPI&label=FastAPI"/></a>
<a href=""><img alt="Frontend - React" src="https://img.shields.io/static/v1?logo=react&color=Blue&message=Frontend&label=React"/></a>
<a href="https://github.com/Simatwa/health-management-system/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/static/v1?logo=MIT&color=Blue&message=MIT&label=License"/></a>
</p>
A comprehensive system for appointment scheduling, patient record management, and a patient portal, all designed to improve healthcare efficiency.

<h1 align="center">Demonstrations</h1>

| Identity | Screenshot |
|----------|-------------|
| Admin   | ![admin page](assets/demo/admin.png) |
| Index   | ![Landing page](assets/demo/index.png) |
| Dashboard | ![Patient dashboard](assets/demo/dashboard.png) |

## Technologies Used

- **Django** – Backend framework for handling database and authentication.
- **FastAPI** – High-performance API framework for seamless integration.
- **React** – Frontend framework for a modern and responsive user interface.

## Features

- **Appointment Scheduling** – Easily book and manage patient appointments.
- **Patient Record Management** – Securely store and retrieve patient information.
- **Patient Portal** – Allows patients to view their records and manage appointments.
- **Admin Dashboard** – Manage hospital operations effectively.
- **M-PESA Integration** – Process payments using the M-PESA mobile money service.
- **Hospital Information Showcase** – Display information about the hospital.
- **API Documentation** – Interactive API documentation with OpenAPI.
- **_Many more..._**

## Installation

Follow these steps to set up the project:

> [!NOTE]
> You need to have [Python>=3.13](https://python.org) and [Git](https://git-scm.com).

```sh
git clone https://github.com/csy0804/his_backend.git
cd hospital-management-system/backend

#根据需要选择是否启用虚拟环境
pip install virtualenv # Incase it's not installed
# Create and activate virtual environment
virtualenv venv
source venv/bin/activate # *nix
.\venv\Scripts\activate # Windows

#安装相关依赖包：
pip install -r requirements.txt

#配置Django数据库：
# Set up Django database
python manage.py makemigrations users hospital finance external staffing
python manage.py migrate
python manage.py collectstatic

#加载一些数据库中的数据：
python manage.py loaddata initial_data.json

#在8998端口启动FastAPI应用：
uvicorn api:app --reload --port 8998


## api文档的ui界面：
- **API Documentation**: `http://localhost:8998/api/docs`
- **Redoc Documentation**: `http://localhost:8998/api/redoc`

## 管理员后台的前后端直接用Django实现：
- **管理员端地址**: `http://localhost:8998/d/admin`

> [!IMPORTANT]
> Admin username : `developer`.
> Password: `development`

## License

This project is licensed under the [MIT License](LICENSE).