import allure
import pymysql
import requests
import logging
from config.config import DB_HOST
from config.config import DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_CHARSET


@allure.step("2.发送http请求")
def send_http_request(**request_data):
    res = requests.request(**request_data)
    logging.info(f"2.发送http请求，响应文本为{res.text}")
    return res

@allure.step("2.发送JDBC请求")
def send_jdbc_request(sql,index=0):
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        charset=DB_CHARSET
    )
    # 建立游标和连接
    cur = conn.cursor()
    # 执行语句
    cur.execute(sql)
    result = cur.fetchone()
    logging.info(f"2.发送JDBC请求：请求SQL={sql}，查询结果={result}")
    # 关闭连接 游标
    cur.close()
    conn.close()
    return result[index] if result else None