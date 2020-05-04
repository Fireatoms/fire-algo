# 大小写数字字符：按照小写字符，数字，大写字符的顺序排序。小写字符，数字和大写字符内部无需有序
# 1. 桶排序，分成小写字符，数字，大写字符三个桶，遍历字符串将字符放入正确的桶，然后合并桶
# 2. 双指针，左指针指向大写字符，右指针指向小写字符时交换两指针所指字符。按照此逻辑使用两次即可完成排序


def str_bucket_sort(s):
    sl = []
    su = []
    sd = []
    for v in s:
        if v.islower():
            sl.append(v)
        elif v.isupper():
            su.append(v)
        else:
            sd.append(v)
    ss = ''.join(sl) + ''.join(sd) + ''.join(su)
    return ss


def str_double_pointer_sort(s):
    lp = 0
    rp = len(s) - 1
    sa = list(s)
    while lp < rp:
        if not sa[lp].islower() and sa[rp].islower():
            sa[lp], sa[rp] = sa[rp], sa[lp]
            lp += 1
            rp -= 1
            continue
        if sa[lp].islower():
            lp += 1
        if not sa[rp].islower():
            rp -= 1

    # 左指针的指向有多种情况，所以简便来写，重新遍历下即可
    for i, v in enumerate(sa):
        if not v.islower():
            lp = i
            break

    # 右指针要回到字符串末尾
    rp = len(s) - 1
    while lp < rp:
        if sa[lp].isupper() and sa[rp].isdigit():
            sa[lp], sa[rp] = sa[rp], sa[lp]
            lp += 1
            rp -= 1
            continue
        if sa[lp].isdigit():
            lp += 1
        if sa[rp].isupper():
            rp -= 1
    return ''.join(sa)


if __name__ == '__main__':
    s = 'aD3D5Greg9'
    ss = str_bucket_sort(s)
    print(ss)
    print(str_double_pointer_sort(s))