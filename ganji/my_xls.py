# coding:utf-8

import xlwt
import sqlite3

def data2xls(data):
    row_0 = ["标题", '租金', '户型', '地址',"装修程度", '面积', '楼层', '朝向','电话']

    book = xlwt.Workbook()  # 新建一个excel
    sheet = book.add_sheet('room_info_sheet')  # 添加一个sheet页
    for i, r in enumerate(row_0):
        sheet.write(0, i, r)

    for i, d in enumerate(data):
        for j in range(9):
            sheet.write(i + 1, j, d[j])

    book.save('room_info_full.xls')  # 保存到当前目录下




if __name__ == "__main__":
    con = sqlite3.connect("E:\my_scrapy\ganji\ganji.sqlite")
    cu = con.cursor()
    query_sql = "select * from rent_room_detail where address like '%闵行%' order by price"
    cu.execute(query_sql)
    data = cu.fetchall()
    data2xls(data)
    con.close()

