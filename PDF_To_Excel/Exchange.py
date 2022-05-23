# -*- coding: utf-8 -*- 
# @Time : 2022/5/11 9:22 
# @Author : Niko

import pdfplumber
import tkinter.filedialog as tf
import tkinter.messagebox as tm
import xlwt
from sys import *


def Main():
    workbook = xlwt.Workbook()  # 定义workbook
    sheet = workbook.add_sheet('Sheet1')  # 添加sheet
    i = 0  # Excel起始位置
    while True:
        path = tf.askopenfilename(title='请选择一个pdf文件',
                                  filetypes=[('所有文件', '.*'), ('PDF文件', '.pdf')])  # 获得选取文件的路径以及目前支持的文件类型
        file_name = path.split('/')[-1].split('.')[0]
        # 如果点击X或者取消退出程序
        if path == '':
            exit()
        # 选取的文件为pdf文件将要进行的操作
        else:
            try:
                pdf_path = pdfplumber.open(path)
                # 获取当前页面的全部文本信息，包括表格中的文字
                for page in pdf_path.pages:
                    for table in page.extract_tables():
                        for row in table:
                            # print(row)
                            for j in range(len(row)):
                                sheet.write(i, j, row[j])
                            i += 1
                pdf_path.close()
                break
            except:
                respond = tm.askyesno(title='提示！！！', message='无法解析，不是指定的可解读文件！！！\n 是否重新选择')
                if respond is True:
                    continue
                else:
                    exit()

    while True:
        try:
            path_save = tf.askdirectory(title='请指定一个文件夹保存')  # 指定一个文件夹
            if path_save == '':
                exit()
            else:
                file_path_save = path_save + '/' + file_name + '.xlsx'  # 拼接文件路径
                workbook.save(file_path_save)
                tm.showinfo('提示', '保存成功')
                break
        except PermissionError:
            ...


if __name__ == '__main__':
    Main()
