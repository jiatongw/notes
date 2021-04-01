'''
Base62算法
    将6位的shortURL看作一个62进制数
    每个shortURL对应一个整数
    该整数对应数据库表中的primary key - sequential ID
'''

def shortURLtoID(shortURL):
    id = 0
    for i in range(0, len(shortURL)):
        id = id * 62 + toBase62(shortURL[i])
    return id

def toBase62(char):
    pass

def idToShortURL(id):
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    short_url = ""
    while id > 0:
        short_url = chars[id % 62] + short_url
        id = id // 62
    while len(short_url) < 6:
        short_url = "0" + short_url

    return short_url
