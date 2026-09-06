import re

# 1. 读取文章内容
with open('in.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. 提取所有纯字母单词（自动忽略数字、标点、符号）
words = re.findall(r'[a-zA-Z]+', content)

# 3. 转小写 + 去重
word_set = set(word.lower() for word in words)

# 4. 按字典序排序
sorted_words = sorted(word_set)

# 5. 写入输出文件 out.txt，每个单词一行
with open('out.txt', 'w', encoding='utf-8') as f:
    for word in sorted_words:
        f.write(word + '\n')