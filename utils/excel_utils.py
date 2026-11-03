# excel文件读取工具
import openpyxl

from config.config import EXCEL_FILE, SHEET_NAME


def read_excel(file_path=EXCEL_FILE, sheet_name=SHEET_NAME):
    # 打开excel文件
    workbook = openpyxl.load_workbook(file_path)

    # 选择表单
    worksheet = workbook[sheet_name]

    data = []  #空列表，用于组装字典
    keys = [cell.value for cell in worksheet[2]]   #拿key行即表中第二行生成一个key列表

    for row in worksheet.iter_rows(min_row=3, values_only=True):   #从第三行开始拿只返回值
        dict_data = dict(zip(keys, row))
        # 如果读取的is_true字段值是true则append
        if dict_data["is_true"]:
            data.append(dict_data)

    # 关闭文件
    workbook.close()

    return data

