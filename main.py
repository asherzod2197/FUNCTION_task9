# 31
def ikkinchi_eng_katta(lst):
    return sorted(set(lst))[-2]

# 32
def harf_soni(matn, harf):
    return matn.count(harf)

# 33
def ildiz(n):
    return n ** 0.5

# 34
def matn_teng(a, b):
    return a == b

# 35
def teskari_tartib(lst):
    return sorted(lst, reverse=True)

# 36
def tasodifiy_tartib(lst):
    random.shuffle(lst)
    return lst

# 37
def katta_harf(matn):
    return matn.upper()

# 38
def sozlar_soni(matn):
    return len(matn.split())

# 39
def qiymat_bor(lst, val):
    return val in lst

# 40
from datetime import date
def vaqt_otgan(yil, oy, kun):
    berilgan = date(yil, oy, kun)
    return (date.today() - berilgan).days

print(ikkinchi_eng_katta([1, 3, 5, 7, 9]))
print(harf_soni("banana", "a"))
print(ildiz(16))
print(matn_teng("python", "python"))
print(teskari_tartib([3, 1, 4, 1, 5]))
print(tasodifiy_tartib([1, 2, 3, 4, 5]))
print(katta_harf("salom"))
print(sozlar_soni("Men Python o'rganaman"))
print(qiymat_bor([1, 2, 3], 2))
print(vaqt_otgan(2020, 1, 1))
