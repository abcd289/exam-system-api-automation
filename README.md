# 学之思在线教育考试系统接口自动化测试项目

## 一、项目简介

本项目基于 Python + Pytest + Requests 搭建，针对学之思在线教育考试系统开展接口自动化测试。

项目采用 Excel 驱动测试用例的方式，实现测试数据与测试代码分离，并通过公共方法封装、参数化执行、响应断言、数据提取及 Allure 测试报告等功能，提高接口测试效率和维护性。

## 二、技术栈

- Python
- Pytest
- Requests
- OpenPyXL
- Allure
- MySQL
- PyMySQL

## 三、项目主要功能

1. Excel 驱动测试用例，实现测试数据与测试代码分离。
2. 封装 HTTP 请求方法，支持常见接口请求方式。
3. 实现 Cookie 提取与传递，处理接口登录鉴权。
4. 支持响应数据提取，为后续接口提供动态参数。
5. 封装响应断言，验证接口执行结果。
6. 连接 MySQL 数据库，进行数据库校验。
7. 集成 Allure，生成自动化测试报告。

## 四、项目目录结构

```text
jkzdhcs/
├── config/          # 项目配置
├── data/            # Excel测试数据及图片
├── testcases/       # 自动化测试用例
├── utils/           # 公共工具类
├── conftest.py      # Pytest公共配置
├── pytest.ini       # Pytest配置
├── run.py           # 测试执行入口
├── requirements.txt # 项目依赖
├── README.md        # 项目说明
├── .gitignore       # Git忽略配置
└── .env.example     # 环境配置模板
```

## 五、环境安装

安装 Python 及项目依赖：

```bash
pip install -r requirements.txt
```

根据 `.env.example` 创建本地 `.env` 文件，并填写自己的测试环境和数据库连接信息。

## 六、运行方式

在项目根目录执行：

```bash
python run.py
```

## 七、测试报告

项目集成 Allure 测试报告，可通过测试执行结果查看用例执行情况、成功失败统计及测试步骤。

## 八、项目说明

本项目用于在线教育考试系统接口自动化测试实践，涉及接口功能测试、自动化测试、接口鉴权、数据提取、数据库校验及测试报告生成。