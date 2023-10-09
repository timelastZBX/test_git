# 这是一个示例 Python 脚本。



# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

import math
import numpy as np
import os
import pandas as pd
from openpyxl.workbook import Workbook
import pywt
import matplotlib as plt
def get_feature(data_list, n):
    X_rms = math.sqrt(sum([x ** 2 for x in data_list]) / len(data_list))  # """均方根值 反映的是有效值而不是平均值 """
    X_p_p = max(data_list) - min(data_list)   # """峰峰值"""
    X_p = max([abs(x) for x in data_list])  # """峰值"""
    X_ma = sum([abs(x) for x in data_list]) / len(data_list)  # """平均幅值"""
    X_r = pow(sum([math.sqrt(abs(x)) for x in data_list]) / len(data_list), 2)   # """方根幅值"""
    C_f = X_p / X_rms   # """峰值因子"""
    C_s = X_rms / X_ma  # """波形因子"""
    C_if = X_p / X_ma   # """脉冲因子"""
    C_mf = X_p / X_r   # """裕度因子"""
    C_kf = (sum([x ** 4 for x in data_list]) / len(data_list)) / pow(X_rms, 4)   # """峭度因子"""
    X_a = sum(x for x in data_list) / len(data_list)  # """均值"""
    X_var = sum((x - X_a)**2 for x in data_list) / len(data_list)  # """方差"""
    X_e = 10 * math.log(sum((x - X_a)**2 for x in data_list), 10)  # """能量"""
    X_skew = sum(((x - X_a) / math.sqrt(X_var))**3 for x in data_list) / len(data_list)  # """偏度"""
    X_ste = sum(x**2 for x in data_list)  # """短时能量"""
    X_a_e = X_ste / len(data_list)  # """均方值"""
    feature = [round(X_rms, 3), round(X_p_p, 3), round(C_f, 3), round(C_s, 3), round(C_if, 3), round(X_r, 3),
               round(C_mf, 3), round(C_kf, 3), round(X_a, 3), round(X_var, 3), round(X_e, 3),
               round(X_skew, 3), round(X_ste, 3), round(X_a_e, 3), n]
    feature_dist = {'均方根值': round(X_rms, 3), '峰峰值': round(X_p_p, 3),  # '峰值': X_p, '平均幅值': X_ma,
                   '方根幅值': round(X_r, 3), '峰值因子': round(C_f, 3), '波形因子': round(C_s, 3), '脉冲因子': round(C_if, 3),
                   '裕度因子': round(C_mf, 3), '峭度因子': round(C_kf, 3), '均值': round(X_a, 3), '方差': round(X_var, 3),
                   '能量': round(X_e, 3), '偏度': round(X_skew, 3), '短时能量': round(X_ste, 3), '均方值': round(X_a_e, 3),
                    '类别': n}

    return feature, feature_dist

def VisitDir(path):
    document_file = []
    for root, dirs, files in os.walk(path):
        for filenames in files:

            b = os.path.join(root, filenames)
            document_file.append(b)
    return document_file

def Loaddata(document_file, split_codes:str):
    fr2 = []
    # index1 = []
    # index2 = []
    for ii in document_file:
        fp1 = open(ii, 'r')
        fr1 = fp1.read()
        fr1 = fr1.split(split_codes)
        if fr1[-1] == '':
            fr1.pop()

        for j in np.arange(len(fr1)):
            # index2.append(j)
            fr1[j] = float(fr1[j])



        fr2.append(fr1)
        # index1.append(index)
        fp1.close()

    return fr2

def prepare_dask(lst):
    for i_4 in range(len(lst)):
        max_l = max(lst[i_4])
        min_l = min(lst[i_4])  # 需添加预处理
        for j in range(len(lst[i_4])):
            lst[i_4][j] = (lst[i_4][j] - min_l) / (max_l - min_l)

    return lst


def pandas_to_excelsheet1(data, filename):
    df_data = data
    df = pd.DataFrame(df_data)
    df = df.T
    df.index.name = '样本\\特征'
    df.to_excel(filename, index=False, sheet_name='Sheet1')


#
# path_1 = r"C:\Users\zhangboxuan\Documents\WeChat Files\wxid_9ftijj71i89h22\FileStorage\File\2023-08\车辆经过\txt"
# path_2 = r"C:\Users\zhangboxuan\Documents\WeChat Files\wxid_9ftijj71i89h22\FileStorage\File\2023-08\机械挖掘\txt"
# path_3 = r"C:\Users\zhangboxuan\Documents\WeChat Files\wxid_9ftijj71i89h22\FileStorage\File\2023-08\人工挖掘\txt"
# all_ft = []
#
# feature_list = ['均方根值', '峰峰值', '方根幅值', '峰值因子', '波形因子', '脉冲因子', '裕度因子', '峭度因子', '均值', '方差', '能量', '偏度', '短时能量', '均方值',
#                 '类别']
#
# path = [path_1, path_2, path_3]
#
# for ptn in range(len(path)):
#     a = VisitDir(path[ptn])
#
#     print(len(a))
#     d_f = []
#     for i in range(len(a)):
#
#         if i % 2 == 1:
#             d_f.append(a[i])
#
#
#     lt = Loaddata(d_f, ',')
#     lt = prepare_dask(lt)
#
# #
# #     for i in range(len(lt)):
# #         ft, ft_d = get_feature(lt[i], ptn)
# #
# #         all_ft.append(ft)
# #
# # a_dft_d = {}
# # for i in range(len(all_ft)):
# #     a_dft = {}
# #     for j in range(len(all_ft[i])):
# #         a = all_ft[i][j]
# #         b = feature_list[j]
# #         a_dft.setdefault(b, a)
# #     a_dft_d.setdefault(i, a_dft)
# #
# #
# #
# #
# # # def pandas_to_excel(data, filename):
# # #     df_data = data
# # #     df = pd.DataFrame(df_data)
# # #     df = df.T
# # #     df.index.name = '特征\\样本'
# # #     df.to_excel(filename, index=True)
# # #
# # # def pandas_add_to_excel(data, filename):
# # #     df_data = data
# # #     df = pd.DataFrame(df_data)
# # #     df = df.T
# # #     df.to_excel(filename, index=True)
# # pandas_to_excelsheet1(a_dft_d, 'data3.xlsx')
# #
# #
# # # https://www.bilibili.com/video/BV18U4y1E7jQ?t=7362.7&p=2
# # # https://www.bilibili.com/video/BV18U4y1E7jQ?t=5940.2&p=2
