# -*- encoding:utf-8 -*-

# Ex7:More Printing

# 打印字符串："May had a little lamb." lamb -- 小羊羔
print "Mary had a little lamb."
# 打印字符串："It's fleece was white as snow", 这里使用%s格式化。 
# fleece -- 羊毛
print "It's fleece was white as %s." % 'snow'
# 打印字符串："And everywhere that Mary went."
print "And everywhere that Mary went."
# 打印10 个., 这里使用字符串乘法
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removeing it to see what happens
# print 后面的逗号 使print不换行，添加一个空格
#print end1 + end2 + end3 + end4 + end5 + end6,
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12
