#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/19 13:39
# @Author : Zhangmi
# @Site : 
# @File : talk.py
# @Software: PyCharm



from tkinter import *
from tkinter import messagebox
import time
import dxlb
import threading

def main():

  def sendMsg():#发送消息
    strMsg = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",
                                  time.localtime()) + '\n '
    txtMsgList.insert(END, strMsg, 'greencolor')
    inStr = txtMsg.get('0.0', END)+'\n'
    txtMsgList.insert(END, inStr,'greencolor')
    txtMsg.delete('0.0', END)
    msg.append(inStr)
    file.write(strMsg)
    file.write(inStr)

  def cancelMsg():#取消内容
    txtMsg.delete('0.0', END)

  def sendMsgEvent(event): #发送消息事件
    if event.keysym == "Up":
      sendMsg()

  def nlpProc(msg):
    while(1):
      time.sleep(8)
      if file.closed:
        break

      node = msg.getNode()

      if node is not None:
        strMsg = '小娜:' + time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.localtime()) + '\n '
        txtMsgList.insert(END, strMsg, 'bluecolor')
        txtMsgList.insert(END, node, 'bluecolor')
        file.write(strMsg)
        file.write(node)

  #创建窗口
  t = Tk()
  t.title('4S店小娜聊天中')

  def my_close():
    # True or Flase
    file.close()
    res = messagebox.askokcancel('提示', '是否关闭窗口')
    if res == True:
      t.destroy()


  # 为右上角的关闭事件添加一个响应函数
  t.protocol('WM_DELETE_WINDOW', my_close)




  #创建frame容器(宽度，高度，背景)
  frmLT = Frame(width=500, height=320, bg='white')
  frmLC = Frame(width=500, height=150, bg='white')
  frmLB = Frame(width=500, height=30)
  frmRT = Frame(width=200, height=500)

  #创建控件
  txtMsgList = Text(frmLT)

  txtMsgList.tag_config('greencolor', foreground='green')#创建tag
  txtMsgList.tag_config('bluecolor', foreground='blue')

  txtMsgList.tag_config('yellowcolor', foreground='#00cccc')
  txtMsg = Text(frmLC);
  #发送消息事件
  # txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
  btnSend = Button(frmLB, text='发送', width = 8, command=sendMsg)
  btnCancel = Button(frmLB, text='取消', width = 8, command=cancelMsg)
  imgInfo = PhotoImage(file = "talk.PNG")
  lblImage = Label(frmRT, image = imgInfo)
  lblImage.image = imgInfo

  #窗口布局(span为跨越数，LT中columnspan(2)意为LT跨越两列，padx/pady意为分割比例为1/3)
  frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
  frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
  frmLB.grid(row=2, column=0, columnspan=2)
  frmRT.grid(row=0, column=2, rowspan=3, padx=2, pady=3)
  #固定大小
  frmLT.grid_propagate(0)
  frmLC.grid_propagate(0)
  frmLB.grid_propagate(0)
  frmRT.grid_propagate(0)
  #第3行第1列插入按钮Send
  btnSend.grid(row=2, column=0)
  btnCancel.grid(row=2, column=1)
  lblImage.grid()
  txtMsgList.grid()
  txtMsg.grid()

  # 创建聊天记录
  file = open('./output/log.txt','a',encoding='GBK')

  msg = dxlb.SingleLinkedList()

  td = threading.Thread(target=nlpProc, args=(msg,))
  td.start()

  #主事件循环
  t.mainloop()




if __name__ == '__main__':
  main()
  # threading.Thread(target=main, args=(msg,))

