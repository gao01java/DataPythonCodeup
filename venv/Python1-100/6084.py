



# 如果 数据 每大于一次 1024 则 每一次都会升级一个kb=


h,b,c,s = map(int,input().split())
m = (h* b * c * s) /8/1024/1024
print('%.1f MB' %m)