from _my_coco import lib, ffi

#Resource info class carrying device capabilities
class ResourceInfo:
    res_cmd_param1 = ffi.new("char[]", "res-1".encode('ascii'))
    res_cmd_param2 = ffi.new("char[]", "Illuminance Sensor".encode('ascii'))
    res_cmd_param3 = ffi.new("char[]", "Anchor".encode('ascii'))
    res_cmd_param4 = ffi.new("char[]", "V1".encode('ascii'))
    res_cmd_param5 = ffi.new("char[]", "1.0.0".encode('ascii'))
    res_cmd_param6 = ffi.new("char[]", "ILLUMINATION_SENSOR".encode('ascii'))

    resource_cmd = [None] * 13
    resource_cmd[0] = ffi.NULL
    resource_cmd[1] = 0
    resource_cmd[2] = res_cmd_param1
    resource_cmd[3] = res_cmd_param2
    resource_cmd[4] = res_cmd_param3
    resource_cmd[5] = res_cmd_param4
    resource_cmd[6] = res_cmd_param5
    resource_cmd[7] = res_cmd_param6
    resource_cmd[8] = lib.COCO_STD_POWER_SRC_BATTERY
    resource_cmd[9] = lib.COCO_STD_RCVR_TYPE_WHEN_STIMULATED
    resource_cmd[10] = 0 #COCO_STD_STATUS_SUCCESS
    resource_cmd[11] = 0
    resource_cmd[12] = 0

class Attributes:
    class RssiAttr:
        rssi_attr = ffi.new("coco_std_resource_attribute_info_t *")

        rssi_attr_param1 = ffi.new("char[]", "rssi".encode('ascii'))
        rssi_attr_param2 = ffi.new("char[]", "NetworkConfiguration".encode('ascii'))
        rssi_val_pointer = ffi.new("int *")
        rssi_val_pointer[0] = 4

        rssi_attr.networkId = ffi.NULL
        rssi_attr.deviceNodeId = 0
        rssi_attr.resourceEui = ResourceInfo.res_cmd_param1
        rssi_attr.capabilityId = lib.COCO_STD_CAP_NETWORK_CONFIGURATION
        rssi_attr.capabilityName = rssi_attr_param2
        rssi_attr.attributeId = lib.COCO_STD_ATTR_NW_CONFIG_RSSI
        rssi_attr.attribName = rssi_attr_param1
        rssi_attr.attribDesc = rssi_attr_param1
        rssi_attr.dataType = lib.COCO_STD_DATA_TYPE_INT32 #22 #COCO_STD_DATA_TYPE_DOUBLE
        rssi_attr.dataArrayLen = 0
        rssi_attr.minValue = rssi_val_pointer
        rssi_attr.maxValue = rssi_val_pointer
        rssi_attr.defaultValue = rssi_val_pointer
        rssi_attr.currentValue = rssi_val_pointer
        rssi_attr.minReportingIntervalMs = 0
        rssi_attr.maxReportingIntervalMs = 10
        rssi_attr.reportableChange = rssi_val_pointer
        rssi_attr.isRealTimeUpdate = 1
        rssi_attr.createdByUserId = 0
        rssi_attr.createdTimestamp = 0
        rssi_attr.lastUpdateTimestamp = 1556539804
    
    class LuxAttr:
        lux_attr = ffi.new("coco_std_resource_attribute_info_t *")

        lux_attr_param1 = ffi.new("char[]", "lux".encode('ascii'))
        lux_attr_param2 = ffi.new("char[]", "illuminance lux".encode('ascii'))
        lux_attr_param3 = ffi.new("char[]", "illuminance".encode('ascii'))

        lux_val_pointer = ffi.new("float *")
        lux_val_pointer[0] = 198.56

        lux_attr.networkId = ffi.NULL
        lux_attr.deviceNodeId = 0
        lux_attr.resourceEui = ResourceInfo.res_cmd_param1
        lux_attr.capabilityId = lib.COCO_STD_CAP_ILLUMINANCE_MEASUREMENT
        lux_attr.capabilityName = lux_attr_param3
        lux_attr.attributeId = lib.COCO_STD_ATTR_CURRENT_LUMINANCE_LUX
        lux_attr.attribName = lux_attr_param1
        lux_attr.attribDesc = lux_attr_param2
        lux_attr.dataType = lib.COCO_STD_DATA_TYPE_DOUBLE
        lux_attr.dataArrayLen = 0
        lux_attr.minValue = lux_val_pointer
        lux_attr.maxValue = lux_val_pointer
        lux_attr.defaultValue = lux_val_pointer
        lux_attr.currentValue = lux_val_pointer
        lux_attr.minReportingIntervalMs = 0
        lux_attr.maxReportingIntervalMs = 10
        lux_attr.reportableChange = lux_val_pointer
        lux_attr.isRealTimeUpdate = 1
        lux_attr.createdByUserId = 0
        lux_attr.createdTimestamp = 0
        lux_attr.lastUpdateTimestamp = 1556539804
    
    class LevelAttr:
        level_attr = ffi.new("coco_std_resource_attribute_info_t *")

        level_attr_param1 = ffi.new("char[]", "level control".encode('ascii'))
        level_attr_param2 = ffi.new("char[]", "controls level".encode('ascii'))
        level_attr_param3 = ffi.new("char[]", "level".encode('ascii'))
        min_level_pointer = ffi.new("int *")
        min_level_pointer[0] = 1
        mid_level_pointer = ffi.new("int *")
        mid_level_pointer[0] = 50
        max_level_pointer = ffi.new("int *")
        max_level_pointer[0] = 100

        level_attr.networkId = ffi.NULL
        level_attr.deviceNodeId = 0
        level_attr.resourceEui = ResourceInfo.res_cmd_param1
        level_attr.capabilityId = lib.COCO_STD_CAP_LEVEL_CTRL
        level_attr.capabilityName = level_attr_param3
        level_attr.attributeId = lib.COCO_STD_ATTR_LEVEL_PCT
        level_attr.attribName = level_attr_param1
        level_attr.attribDesc = level_attr_param2
        level_attr.dataType = lib.COCO_STD_DATA_TYPE_UINT32 #22 #COCO_STD_DATA_TYPE_DOUBLE
        level_attr.dataArrayLen = 0
        level_attr.minValue = min_level_pointer
        level_attr.maxValue = max_level_pointer
        level_attr.defaultValue = min_level_pointer
        level_attr.currentValue = mid_level_pointer
        level_attr.minReportingIntervalMs = 0
        level_attr.maxReportingIntervalMs = 10
        level_attr.reportableChange = min_level_pointer
        level_attr.isRealTimeUpdate = 1
        level_attr.createdByUserId = 0
        level_attr.createdTimestamp = 0
        level_attr.lastUpdateTimestamp = 1556539804

    class OnOffAttr:
        on_off_attr = ffi.new("coco_std_resource_attribute_info_t *")

        on_off_attr_param1 = ffi.new("char[]", "onoffswitch".encode('ascii'))
        on_off_attr_param2 = ffi.new("char[]", "showing on or off".encode('ascii'))
        on_off_attr_param3 = ffi.new("char[]", "on off".encode('ascii'))
        min_on_off = ffi.new_handle(False)
        max_on_off = ffi.new_handle(True)

        on_off_attr.networkId = ffi.NULL
        on_off_attr.deviceNodeId = 0
        on_off_attr.resourceEui = ResourceInfo.res_cmd_param1
        on_off_attr.capabilityId = lib.COCO_STD_CAP_ON_OFF_CONTROL
        on_off_attr.capabilityName = on_off_attr_param1
        on_off_attr.attributeId = lib.COCO_STD_ATTR_ON_FLAG 
        on_off_attr.attribName = on_off_attr_param3
        on_off_attr.attribDesc = on_off_attr_param2
        on_off_attr.dataType = lib.COCO_STD_DATA_TYPE_BOOLEAN #22 #COCO_STD_DATA_TYPE_DOUBLE
        on_off_attr.dataArrayLen = 0
        on_off_attr.minValue = min_on_off
        on_off_attr.maxValue = max_on_off
        on_off_attr.defaultValue = min_on_off
        on_off_attr.currentValue = min_on_off
        on_off_attr.minReportingIntervalMs = 0
        on_off_attr.maxReportingIntervalMs = 10
        on_off_attr.reportableChange = min_on_off
        on_off_attr.isRealTimeUpdate = 1
        on_off_attr.createdByUserId = 0
        on_off_attr.createdTimestamp = 0
        on_off_attr.lastUpdateTimestamp = 1556539804
    #class ColorAttr:
        #color_attr = ffi.new("coco_std_resource_attribute_info_t")

#Capability
class Capability:
    class IlluminanceCapability:
        cap_param = ffi.new("char[]", "illuminance".encode('ascii'))

        resource_capability_info = [None] * 9
        resource_capability_info[0] = ffi.NULL
        resource_capability_info[1] = 0
        resource_capability_info[2] = ResourceInfo.res_cmd_param1
        resource_capability_info[3] = lib.COCO_STD_CAP_ILLUMINANCE_MEASUREMENT
        resource_capability_info[4] = cap_param
        resource_capability_info[5] = 0
        resource_capability_info[6] = ffi.NULL
        resource_capability_info[7] = 0
        resource_capability_info[8] = 0

    class NetworkConfigurationCapability:
        cap_param = ffi.new("char[]", "Network Configuration".encode('ascii'))

        resource_capability_info = [None] * 9
        resource_capability_info[0] = ffi.NULL
        resource_capability_info[1] = 0
        resource_capability_info[2] = ResourceInfo.res_cmd_param1
        resource_capability_info[3] = lib.COCO_STD_CAP_NETWORK_CONFIGURATION
        resource_capability_info[4] = cap_param
        resource_capability_info[5] = 0
        resource_capability_info[6] = ffi.NULL
        resource_capability_info[7] = 0
        resource_capability_info[8] = 0

    class OnOffCapability:
        cap_param = ffi.new("char[]", "on off control".encode('ascii'))
        
        std_cmd_array = ffi.new("int32_t[2]")
        std_cmd_array[0] = lib.COCO_STD_CMD_ON
        std_cmd_array[1] = lib.COCO_STD_CMD_OFF

        resource_capability_info = [None] * 9
        resource_capability_info[0] = ffi.NULL
        resource_capability_info[1] = 0
        resource_capability_info[2] = ResourceInfo.res_cmd_param1
        resource_capability_info[3] = lib.COCO_STD_CAP_ON_OFF_CONTROL
        resource_capability_info[4] = cap_param
        resource_capability_info[5] = 2
        resource_capability_info[6] = std_cmd_array
        resource_capability_info[7] = 0
        resource_capability_info[8] = 0

    class LevelCapability:
        cap_param = ffi.new("char[]", "Color control".encode('ascii'))
        level_array = ffi.new("int32_t[5]")
        level_array[0] = lib.COCO_STD_CMD_LEVEL_MIN
        level_array[1] = lib.COCO_STD_CMD_SET_LEVEL
        level_array[2] = lib.COCO_STD_CMD_SET_LEVEL_WITH_ON_OFF
        level_array[3] = lib.COCO_STD_CMD_FETCH_LEVEL
        level_array[4] = lib.COCO_STD_CMD_LEVEL_MAX

        resource_capability_info = [None] * 9
        resource_capability_info[0] = ffi.NULL
        resource_capability_info[1] = 0
        resource_capability_info[2] = ResourceInfo.res_cmd_param1
        resource_capability_info[3] = lib.COCO_STD_CAP_LEVEL_CTRL
        resource_capability_info[4] = cap_param
        resource_capability_info[5] = 5
        resource_capability_info[6] = level_array
        resource_capability_info[7] = 0
        resource_capability_info[8] = 0

#Array of capabilities
class CapabilityArr:
    cap_array = ffi.new("coco_std_resource_capability_t[4]")

    #put more capabilites here
    cap_array[0].resourceCapabilityInfo = Capability.IlluminanceCapability.resource_capability_info
    cap_array[0].attributeArrCount = 1
    cap_array[0].attributeArr = Attributes.LuxAttr.lux_attr

    cap_array[1].resourceCapabilityInfo = Capability.NetworkConfigurationCapability.resource_capability_info
    cap_array[1].attributeArrCount = 1
    cap_array[1].attributeArr = Attributes.RssiAttr.rssi_attr

    cap_array[2].resourceCapabilityInfo = Capability.OnOffCapability.resource_capability_info
    cap_array[2].attributeArrCount = 1
    cap_array[2].attributeArr = Attributes.OnOffAttr.on_off_attr

    cap_array[3].resourceCapabilityInfo = Capability.LevelCapability.resource_capability_info
    cap_array[3].attributeArrCount = 1
    cap_array[3].attributeArr = Attributes.LevelAttr.level_attr

#Global Variable
resource_info = ffi.new("coco_std_resource_t *")
resource_info.resourceSummaryInfo = ResourceInfo.resource_cmd
resource_info.capabilityArrCount = 1
resource_info.capabilityArr = CapabilityArr.cap_array