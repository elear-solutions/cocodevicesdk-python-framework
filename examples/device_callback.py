from _my_coco import lib, ffi

#Defining callback functions

@ffi.def_extern()
def coco_device_join_nw_status_cb(status):
    print("App: coco_device_join_nw_status_cb() status: {}}\n".format(status))
    return

def coco_device_add_res_status_cb(status, context):
    print("App: coco_device_join_nw_status_cb() status: {}}\n".format(status))
    return

def coco_device_attribute_update_status(status, context):
    print("App: coco_device_attribute_update_status() status: {}}\n".format(status))
    return

def coco_device_data_corruption_cb():
    print("App: cocodevicesdk data corrupted\n")
    exit(1)
