import jieba    # 分词
import matplotlib.pyplot as plt # 绘图
from wordcloud import WordCloud # 词云
from PIL import Image           # 图像处理
import numpy as np         # 矩阵运算
import sqlite3             # 数据库

conn = sqlite3.connect('movieTop250')
cur = conn.cursor()
sql = 'select instroduction from moviesTop250'
data = cur.execute(sql)
text = ""
for item in data:
    text += item[0]
# print(text)
cur.close()
conn.close()

# 导入停用词
stopwords = []
with open('./stopwords.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for word in lines:
        stopwords.append(word)
stopwords = set(stopwords)  # 去重

cut = jieba.cut(text)
wordlist = (" ".join(cut)).split(' ')

string = ""
# 去停用词
for word in wordlist:
    if word not in stopwords:
        string += word + " "


img = Image.open(r'./static/assets/img/image.jpg')
img_arr = np.array(img) # 将图片转换为数组

wc = WordCloud(
    background_color='white',
    mask=img_arr,
    font_path='msyh.ttc'    # 微软雅黑字体
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')
plt.show()
