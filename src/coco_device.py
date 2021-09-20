from _my_coco import lib, ffi
import device_callback as dc
import time

#Initializes the cocoDevice
class CocoDevice:
    instance = None
    def __init__(self, cwd, config_path, version, temp_path):
        #Under the hood FFI layer
        self.cwd_path = ffi.new("char[]", "{}".format(cwd).encode('ascii'))
        self.config_path = ffi.new("char[]", "{}".format(config_path).encode('ascii'))
        self.firmware_version = ffi.new("char[]", "{}".format(version).encode('ascii'))
        self.temp_path = ffi.new("char[]", "{}".format(temp_path).encode('ascii'))

    def device_init(self):
        if CocoDevice.instance == None:
            print("New Initialization\n")
            device_init_params = ffi.new("coco_device_init_params_t *")
            device_init_params.cwdPath = self.cwd_path
            device_init_params.configFilePath = self.config_path
            device_init_params.downloadPath = self.cwd_path
            device_init_params.firmwareVersion = self.firmware_version
            device_init_params.isExtendable = True
            device_init_params.powerSource = 4 
            device_init_params.receiverType = 0 
            device_init_params.skipSSLVerification = 1
            device_init_params.tempPath = self.temp_path

            ret_val = lib.coco_device_init(device_init_params)
            print(ret_val)
            if (-1 == ret_val):
                print("App: coco_device_init failed\n")
                exit(1)
            if (0 == ret_val):
                while(-1 == lib.coco_device_init_auth()):
                    print("app: will try re-auth in 3 seconds")
                    time.sleep(3)
            CocoDevice.instance = CocoDevice(self.cwd_path, self.config_path, self.firmware_version, self.temp_path)
        else:
            print("Device is already initialized")
        return CocoDevice.instance

#Main testing
if __name__ == "__main__":
    callbacks = [dc.coco_device_join_nw_status_cb, dc.coco_device_add_res_status_cb, dc.coco_device_attribute_update_status, dc.coco_device_data_corruption_cb, dc.coco_device_resource_cmd_cb]
    my_device_initializer = CocoDevice("/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/examples/c/device-app-boilerplate/build_cwd/is-2",
                                    "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/examples/c/device-app-boilerplate/build_cwd/is-2/configpython.txt",
                                     "1.0.0",
                                    "/tmp")
    my_device = my_device_initializer.device_init()
    another_device_initializer = CocoDevice("/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/examples/c/device-app-boilerplate/build_cwd/is-2",
                                    "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/examples/c/device-app-boilerplate/build_cwd/is-2/configpython.txt",
                                     "1.0.0",
                                    "/tmp")
    another_device = another_device_initializer.device_init()
    if my_device != another_device:
        exit(1)
    while 1:
        time.sleep(5)