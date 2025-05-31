## Installation

Follow these steps to set up the project:

> [!NOTE]
> You need to have [Python>=3.13](https://python.org) and [Git](https://git-scm.com).

```sh
git clone https://github.com/csy0804/his_backend.git

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
```

## api文档的ui界面：
- **API Documentation**: `http://localhost:8998/api/docs`
- **Redoc Documentation**: `http://localhost:8998/api/redoc`

## 管理员后台的前后端直接用Django实现：
- **管理员端地址**: `http://localhost:8998/d/admin`


> 管理员用户名 : `developer`
> 密码: `development`

## License

This project is licensed under the [MIT License](LICENSE).