学习笔记
Vscode 的使用

插件
Rainbow Fart - 括号对的颜色
Python - Python 的调试和 linting

快捷键
代码格式化：Option + Shift + F （Alt + Shift + F）
以单词为单位移动光标：Option + 左右箭头 （Ctrl + 左右方向键）
快速回到顶部/底部：Command + 上下箭头 （Ctrl + Home/End）
快速移到行首/行末：Command + 左右箭头 （Home/End）
移动行：Option + 上下箭头（Alt + 上下箭头）
滚动代码，不移动光标：Ctrl + 上下箭头
多行编辑：Ctrl + 上下箭头
单行注释：Command + /（Ctrl + /）

Python 基本数据类型
None	空对象
Bool	布尔值
数值	整数、浮点数、复数
序列	字符串、列表、元组
集合	字段
可调用	函数

logging
日志级别
info 记录日常信息
warning 出现不会影响程序运行的异常
error 报错
critical 灾难性错误
debug
info 级别以上的才会输出

logging.basicConfig()
格式	描述
filename	使用指定的文件名而不是 StreamHandler 创建 FileHandler。
filemode	如果指定了 filename，则用此模式打开该文件。默认模式为 'a'。
format	处理器使用的指定格式字符串。
datefmt	使用指定的日期/时间格式，与 time.strftime() 所接受的格式相同
style	如果指定了 format，将为格式字符串使用此风格。'%'，'{' 或 '$' 分别对应于 printf 风格，str.format() 或 string.Template。默认为 '%'。
level	设置跟记录器级别去指定 level。
stream	使用指定的流初始化 SteamHandler。请注意此参数与 filename 是不兼容的 - 如果两者同时存在，则会引发 ValueError。
handlers	如果指定，这应为一个包含要加入跟日志记录器的已创建处理程序的可迭代对象。任何尚未设置格式描述符的处理程序将被设置为此函数中创建的默认格式描述符。请注意此参数与 filename或 stream 是不兼容的 - 如果两者同时存在，则会引发 ValueError。


示例：	
import logging
from datetime import *
from pathlib import Path

p = Path(f'/var/log/python-{datetime.now().date()}')
p.mkdir(parents=True, exist_ok=True)
log_filename = p.joinpath(f'{__name__}.log')

logging.basicConfig(filename=log_filename,
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %X',
                    format='%(asctime)s %(name)-8s %(levelname)-8s '
                    '[line: %(lineno)d] %(message)s'
                    )

logging.error("error message")
