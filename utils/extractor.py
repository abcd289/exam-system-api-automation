import allure
import jsonpath
from utils.send_request import send_jdbc_request
import logging


def json_extractor(case, all, res):
    if case["jsonExData"]:
        with allure.step("4.JSON提取"):
            extract_result = {}
            for key, exp in eval(case["jsonExData"]).items():
                ret = jsonpath.jsonpath(res.json(), exp)
                if ret is False:
                    msg = f"JSON提取失败，key={key}, jsonpath表达式={exp}，未匹配到数据"
                    logging.error(msg)
                    raise Exception(msg)
                value = ret[0]
                all[key] = value
                extract_result[key] = value
            logging.info(f"4.JSON提取，根据{case['jsonExData']}提取数据，此时全局变量为{all}")
            allure.attach(
                str(extract_result),
                name="JSON提取结果",
                attachment_type=allure.attachment_type.TEXT
            )


def cookie_extractor(case, all, res):
    if case["cookieExData"]:
        with allure.step("4.Cookie提取"):
            extract_result = {}
            for key, cookie_name in eval(case["cookieExData"]).items():
                value = res.cookies.get(cookie_name)
                all[key] = value
                if value:
                    extract_result[key] = "提取成功"
                else:
                    extract_result[key] = f"提取失败：cookie[{cookie_name}]不存在"
                    logging.warning(f"Cookie提取失败，key={key}, cookie名称={cookie_name}")
            logging.info(f"4.Cookie提取，根据{case['cookieExData']}提取数据，此时全局变量为{all}")
            allure.attach(
                str(extract_result),
                name="Cookie提取结果",
                attachment_type=allure.attachment_type.TEXT
            )


def jdbc_extractor(case, all):
    if case["sqlExData"]:
        extract_result = {}
        with allure.step("4.数据库提取"):
            for key, sql in eval(case["sqlExData"]).items():
                value = send_jdbc_request(sql)
                all[key] = value
                extract_result[key] = value
            logging.info(f"4.JDBC提取，根据{case['sqlExData']}提取数据，此时全局变量为{all}")
            allure.attach(
                str(extract_result),
                name="JDBC提取结果",
                attachment_type=allure.attachment_type.TEXT
            )
