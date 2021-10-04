#To mimic the functionalities of main.c in ../device-app-boilerplate
from _my_coco import lib, ffi

import sys
sys.path.append('/mnt/host/tmp/workspace/cocosdk/pycoco-framework/src')

import coco_client
import device_declarations as dd
import time

ret_val = lib.coco_device_init(coco_client.DeviceInitParams.device_init_params) ####Remove this stuff because the class now gets intiailzied

if (-1 == ret_val):
    print("App: coco_device_init failed\n")
    exit(1)

if (0 == ret_val):
    while(-1 == lib.coco_device_init_auth()):
        print("app: will try re-auth in 3 seconds")
        time.sleep(3)

#Add a resource using COCO device SDK API
res_cmd = dd.ResourceInfo.resource_cmd

#Capabilities
illuminance_capability = dd.Capability.IlluminanceCapability.resource_capability_info
network_config_capability = dd.Capability.NetworkConfigurationCapability.resource_capability_info
on_off_capability = dd.Capability.OnOffCapability.resource_capability_info
level_capability = dd.Capability.LevelCapability.resource_capability_info

#Attributes
rssi_attr = dd.Attributes.RssiAttr.rssi_attr
lux_attr = dd.Attributes.LuxAttr.lux_attr
level_attr = dd.Attributes.LevelAttr.level_attr
on_off_attr = dd.Attributes.OnOffAttr.on_off_attr

#Capability Arr
capability_arr = dd.CapabilityArr.cap_array

#Res Info
resource_info = ffi.new("coco_std_resource_t *")
resource_info.resourceSummaryInfo = dd.ResourceInfo.resource_cmd
resource_info.capabilityArrCount = 5
resource_info.capabilityArr = capability_arr

#Main function
def main():
    if (-1 == lib.coco_device_add_resource(resource_info, 1, 0, 0, ffi.NULL)):
        print("App: Add resource failed\n")
        exit(1)

    print(resource_info)

    def get_next_lux_val(lux):
        increment = np.random.randint(5, size=1)
        new_lux = lux + increment[0]
        return ffi.new_handle(new_lux)

    while(1):
        print("App: Update attribute\n")
        lux_attr.currentValue = get_next_lux_val(lux_attr.currentValue)
        if (-1 == lib.coco_device_resource_attribute_update(lux_attr, ffi.NULL)):
            print("App: Update attribute failed\n")
        time.sleep(2)

if __name__ == "__main__":
    main()