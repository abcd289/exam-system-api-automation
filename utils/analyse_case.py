import allure
import json
from config.config import BASE_URL
import logging


# 解析Excel中的请求数据
def parse_data(value):
    if value is None or value == "":
        return None

    if isinstance(value, str):
        return json.loads(value)

    return value


@allure.step("1.解析请求数据")
def analyse_case(case):
    method = case["method"]
    url = BASE_URL + case["path"]

    headers = parse_data(case["headers"])
    params = parse_data(case["params"])
    data = parse_data(case["data"])
    json = parse_data(case["json"])
    files = parse_data(case["files"])

    request_data = {
        "method": method,
        "url": url,
        "headers": headers,
        "params": params,
        "data": data,
        "json": json,
        "files": files
    }

    logging.info(f"1.解析请求数据，请求数据为{request_data}")
    allure.attach(f"{request_data}", name="请求数据结果")

    return request_data