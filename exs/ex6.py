# -*- encoding:utf-8 -*-

# Ex6:String And Text

# 定义一个字符串x, 使用% 格式化
x = "There are %d types of people." % 10
# 定义一个字符串binary, 内容为"binary"
binary = "binary"
# 定义一个字符串do_not, 内容为"don't"
do_not = "don't"
# 定义一个字符串y, 使用% 格式化，使用元组，格式化两个参数
y = "Those who know %s and those who %s." % (binary, do_not)

# 打印x
print x
# 打印y
print y

# 把x的内容打印，使用%r.
print "I said: %r." % x
# 把y的内容打印，使用%s
print "I also said: '%s'." % y

hilarious = False
# 定义一个格式化字符串，其中使用了%r
joke_evaluation = "Isn't that joke so funny?! %r"

# 使用 hilarious 来格式化joke_evaluation字符串，并打印
print joke_evaluation % hilarious
print joke_evaluation

w = "This is the left side of..."
e = "a string with a right side."

# 把w和e拼接起来，然后打印
print w + e
