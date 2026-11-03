
import os
from pathlib import Path
from dotenv import load_dotenv

# 获取项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 加载项目根目录下的.env文件
load_dotenv(BASE_DIR / ".env")

# 环境基准地址
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

# Excel格式测试用例文件配置
EXCEL_FILE = "./data/测试用例.xlsx"
SHEET_NAME = "Sheet2"

# MySQL配置
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "xzs")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_CHARSET = "utf8"
