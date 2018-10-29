# -*-encoding:utf-8-*-

# Ex8 Printing, Printing

# 定义格式化模版字符串，内容为四个 %r
formatter = "%r %r %r %r"

# 使用formatter模版字符串打印，使用1, 2, 3, 4来格式化
print(formatter % (1, 2, 3, 4))
# 使用formatter模版字符串打印，使用“one”， “two”， “three”， “four”来格式化
print(formatter % ("one", "two", "three", "four"))
# 使用formatter模版字符串打印，使用True， False， False， True来格式化
print(formatter % (True, False, False, True))
# 使用formatter模版字符串打印，使用formatter本身来格式化
print(formatter % (formatter, formatter, formatter, formatter))
# 使用formatter模版字符串打印，使用四个字符串来格式化
print(formatter % (
    "I had this thing. 测试中文",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
