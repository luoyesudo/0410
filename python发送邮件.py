# coding = utf-8
# Author: 没有不同
# Date: 2021/1/16 19:43
# Year： 2021
# 十四：Python发送邮件
# Python群发一个excel表格中的所有联系人的邮件
# 1.多个sheet表格依次发送所有的邮件
# 2.每个邮件的内容不一样
import xlrd
import zmail
class mail_execel():
    # 构造方法，文件
    def __init__(self,file):
        self.file=file
    # 打开文件，读取工作目录
    def open_excel(self,sender):
        self.book=xlrd.open_workbook(self.file)
        for i in range(self.book.nsheets):
            self.sh1=self.book.sheet_by_index(i)
            self.st1 = []
            # 按行读取每行内容
            for i in range(self.sh1.nrows):
                self.st1.append(self.sh1.row_values(i))
            print(self.st1[1:])
            email=zmail.server(*sender)
            for i in self.st1[1:]:
                print(i)
                self.msg={
                    'subject':i[1],
                    'content_text':i[2]
                }
                email.send_mail(i[0], self.msg)
                print(i[0])
email=mail_execel('email.xls')
send=('2252683708@qq.com','dzpqnpfrbgnndjeg')
email.open_excel(send)

