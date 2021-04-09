



r,g,b = map(int,input().split())



#需要先把 所输入的数字全部 乘起来 然后 再换算为byte 换算为Byte 之后
# 再换算成 1024 1024byte=1kb 1024kb=1mb 所以 需要进行三次除法
#以便获得 最后的mb 如果换算成 gb 则就是在除一次1024 即可
m = (r* g * b ) /8/1024/1024
print('%.2f MB' %m)