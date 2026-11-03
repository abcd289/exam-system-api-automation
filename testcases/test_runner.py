import pytest
from jinja2 import Template
from utils.allure_utils import allure_init
from utils.analyse_case import analyse_case
from utils.asserts import http_assert, jdbc_assert
from utils.excel_utils import read_excel
from utils.extractor import json_extractor, jdbc_extractor, cookie_extractor
from utils.send_request import send_http_request
import logging

class TestRunner:

    # 读测试数据
    data = read_excel()

    # 提取后的数据需要初始化一个全局属性来保存，可以用{}空字典,比如登录提取到的cookie或token，用户ID 数据库查询结果等
    all = {}

    @pytest.mark.parametrize("case", data)    #将data列表中的每一条数据分别传送给case
    def test_case(self,case):

        # 引用全局变量
        all = self.all  # 建立测试函数内外all变量的对应关系

        # 根据all的值渲染case   jinja2将测试用例中定义的模板变量替换成实际数据。
        case = eval(Template(str(case)).render(all))

        # 初始化allure报告
        allure_init(case=case)    # 形参是在初始化allure报告的参数case

        # 0.测试用例的描述信息日志
        logging.info(f"0.用例ID:{case['id']} 模块:{case['feature']} 场景:{case['story']} 标题:{case['title']}")

        # 判断是否为http请求
        if case["method"] and case["path"]:
            # 1.解析http请求数据
            request_data = analyse_case(case)
            # 2.发起http请求
            res = send_http_request(**request_data)
            # 3.HTTP断言
            http_assert(case, res)
            # 4.JSON提取
            json_extractor(case, all, res)
            # 4.Cookie提取
            cookie_extractor(case, all, res)

        # 不是http请求则发送数据库请求
        # 3.数据库断言
        jdbc_assert(case)
        # 4.数据库提取
        jdbc_extractor(case, all)









