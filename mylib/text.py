from re import sub

text = '[黑胶唱片原始利润成百倍]网友评论&nbsp&nbsp&nbsp已有_COUNT_条评论'

num = sub(r'&nbsp', '',text)
print(num)