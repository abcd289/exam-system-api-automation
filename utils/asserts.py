
import logging
import allure
import jsonpath
from utils.send_request import send_jdbc_request


@allure.step("3.HTTP响应断言")
def http_assert(case, res):
    check = case.get("check")
    expected = case.get("expected")

    # 没有配置HTTP断言时，跳过HTTP断言
    if not check and (expected is None or str(expected).strip() == ""):
        logging.info("未配置HTTP响应断言，跳过HTTP断言")
        return

    if check:
        result = jsonpath.jsonpath(res.json(), check)

        if not result:
            raise AssertionError(
                f"JSONPath未匹配到结果：{check}，响应内容：{res.text}"
            )

        actual = result[0]

        logging.info(
            f"3.HTTP响应断言内容：实际结果({actual}) == 预期结果({expected})"
        )

        allure.attach(
            f"断言方式：JSONPath\n"
            f"实际结果：{actual}\n"
            f"预期结果：{expected}",
            name="HTTP响应断言详情",
            attachment_type=allure.attachment_type.TEXT
        )

        assert actual == expected, (
            f"HTTP断言失败，实际结果：{actual}，预期结果：{expected}"
        )

    else:
        logging.info(
            f"3.HTTP响应断言内容：预期结果({expected}) in 实际结果({res.text})"
        )

        allure.attach(
            f"断言方式：文本包含\n"
            f"实际响应：{res.text}\n"
            f"预期结果：{expected}",
            name="HTTP响应断言详情",
            attachment_type=allure.attachment_type.TEXT
        )

        assert str(expected) in res.text


def jdbc_assert(case):
    if case.get("sql_check") and case.get("sql_expected") is not None:

        with allure.step("3.数据库响应断言"):

            # 1.发送JDBC请求
            result = send_jdbc_request(case["sql_check"])

            # 2.提取实际查询结果
            actual = result[0] if isinstance(result, (tuple, list)) else result

            # 3.处理MySQL BIT类型返回的bytes
            if isinstance(actual, bytes):
                actual = bool(int.from_bytes(actual, byteorder="big"))

            expected = case["sql_expected"]

            logging.info(
                f"3.数据库响应断言内容：实际结果({actual}) == 预期结果({expected})"
            )

            allure.attach(
                f"SQL语句：{case['sql_check']}\n"
                f"实际结果：{actual}\n"
                f"预期结果：{expected}",
                name="数据库断言详情",
                attachment_type=allure.attachment_type.TEXT
            )

            assert actual == expected, (
                f"数据库断言失败，实际结果：{actual}，预期结果：{expected}"
            )
