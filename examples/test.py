from _my_coco import lib, ffi

x = ffi.new("int32_t[2]")
x[0] = 40
x[1] = 230
print(x)