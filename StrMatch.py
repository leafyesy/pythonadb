import re

reStr = "124本贴最后由123编辑1234本贴最后由123999编辑1321"
formatStr = "本贴最后由(.*?)编辑"

pattern = re.compile(formatStr, re.I)  # re.I 表示忽略大小写
m = pattern.findall(reStr)

print(m)

