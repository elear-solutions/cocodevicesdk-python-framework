from _my_coco import ffi, lib
import device_callback as dc

#Local variables
firmware_version = ffi.new("char[]", "1.0.0".encode('ascii'))
callbacks = [dc.coco_device_join_nw_status_cb, dc.coco_device_add_res_status_cb, dc.coco_device_attribute_update_status, dc.coco_device_data_corruption_cb, dc.coco_device_resource_cmd_cb]
app_config_cwd = ffi.new("char[]", "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/examples/c/device-app-boilerplate/build_cwd/is-2".encode('ascii'))
app_config_config_file_path = ffi.new("char[]", "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/examples/c/device-app-boilerplate/build_cwd/is-2/configpython.txt".encode('ascii'))
app_config_temp_path = ffi.new("char[]", "/tmp".encode('ascii'))

class DeviceInitParams:
    device_init_params = ffi.new("coco_device_init_params_t *")
    device_init_params.cwdPath = app_config_cwd
    device_init_params.configFilePath = app_config_config_file_path
    device_init_params.downloadPath = app_config_cwd
    device_init_params.coconetConnStatusCb = ffi.new_handle(callbacks[0])
    device_init_params.addResStatusCb = ffi.new_handle(callbacks[1])
    device_init_params.attributeUpdateCb = ffi.new_handle(callbacks[2])
    device_init_params.dataCorruptionCb = ffi.new_handle(callbacks[3])
    device_init_params.resourceCmdCb = ffi.new_handle(callbacks[4])
    device_init_params.firmwareVersion = firmware_version
    device_init_params.isExtendable = True
    device_init_params.powerSource = 4 #COCO_STD_POWER_SRC_BATTERY
    device_init_params.receiverType = 0 #COCO_STD_RCVR_TYPE_RX_ON_WHEN_IDLE
    device_init_params.skipSSLVerification = 1
    device_init_params.tempPath = app_config_temp_path

