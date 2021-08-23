#APIn  Method of Linking
import os
from cffi import FFI
import ctypes

from sys import exit, platform

ffi = FFI()
cdef_from_file = None   
header = '/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocodevicesdk/coco_device_api.h'

#Accessing C header file try and exceptions
try:
    with open(header, 'r') as libtestcffi_header:
        cdef_from_file = libtestcffi_header.read()
except FileNotFoundError:
    print('Unable to find "%s"' % header)
    exit(-1)
except IOError:
    print('Unable to open "%s"' % header)
    exit(-1)
finally:
    if cdef_from_file == '':
        print('File "s" is empty' % header)
        exit(-1)

#ffi.cdef(cdef_from_file)
ffi.cdef(""" 
    double sqrt(double x);
    double sin(double x);

    void coco_device_perror(const char *str);
    typedef struct {
        char *cwd;
        char *configFilePath;
        char *tempPath;
    }   cmdline_params_t;

    typedef struct {
        char *networkId;
        uint32_t deviceNodeId;
        char *resourceEui;
        int32_t capabilityId;
        uint32_t cmdSenderNodeId;
        uint32_t cmdSeqNum;
        uint32_t timeoutMs;
        int32_t cmdId;
        void *cmdParams;
    } coco_std_resource_cmd_t;

    typedef struct {
        char *networkId;
        uint32_t deviceNodeId;
        uint32_t cmdSenderNodeId;
        uint32_t cmdSeqNum;
        uint32_t timeoutMs;
        char *accessToken;
        int32_t cmdId;
        void *cmdParams;
    } coco_std_device_cmd_t;

    typedef struct {
        int32_t key; 
        void *value;
    } coco_std_parameter_t;

    typedef struct {
        char *networkId;
        uint32_t reqNodeId;
        uint32_t requestId;
        uint32_t cmdSeqNum;
        uint32_t respNodeId;
        uint32_t mandatoryInfoRequestArrCount;
        coco_std_parameter_t *mandatoryInfoRequestArr;
        uint32_t optionalInfoRequestArrCount;
        coco_std_parameter_t *optionalInfoRequestArr;
        char *messageText;
        uint32_t timeoutMs;
    } coco_std_info_request_t;

    typedef struct {
        char *networkId;
        uint32_t reqNodeId;
        uint32_t requestId;
        uint32_t cmdSeqNum;
        uint32_t infoResponseArrCount;
        coco_std_parameter_t *infoResponseArr;
    } coco_std_info_response_t;

    typedef struct {
        uint32_t nodeId;
    } coco_device_tunnel_handle_t;

    typedef struct {
        char *version;
        char *filePath;
    } coco_device_fw_update_details_t;

    typedef enum {
        COCO_STD_STATUS_CODE_MIN = -1,
        COCO_STD_STATUS_SUCCESS,
        COCO_STD_STATUS_INVALID,
        COCO_STD_STATUS_FAILURE,
        COCO_STD_STATUS_PARTIAL_SUCCESS,
        COCO_STD_STATUS_TIMEOUT,
        COCO_STD_STATUS_REJECTED,
        COCO_STD_STATUS_DEVICE_BUSY,
        COCO_STD_STATUS_IN_PROGRESS,
        COCO_STD_STATUS_AUTH_FAILED,
        COCO_STD_STATUS_RESOURCE_NOT_SUPPORTED,
        COCO_STD_STATUS_SUCCESS_INSECURE,
        COCO_STD_STATUS_PARTIAL_SUCCESS_INSECURE,
        COCO_STD_STATUS_CONNECTIVITY_ERROR,
        COCO_STD_STATUS_CMD_NOT_SUPPORTED,
        COCO_STD_STATUS_TOKEN_NOT_SET,
        COCO_STD_STATUS_TOKEN_REFRESH_FAILED,
        COCO_STD_STATUS_DISCOVERY_NOT_APPLICABLE,
        COCO_STD_STATUS_NETWORK_DISCONNECTED,
        COCO_STD_STATUS_CODE_MAX,
        COCO_STD_STATUS_CODE_UBOUND = 0x7FFFFFFF
    } coco_std_status_code_t;
    
    typedef void (* coco_device_free_tunnel_params_cb_t)(void *deviceTunnelParams);

    typedef struct {
        char *hostname;
        uint16_t port;
        int32_t ipVersion;
        coco_device_free_tunnel_params_cb_t freeTunnelParamsCb;
    } coco_device_tunnel_params_t;
    
    typedef struct {
        void  *context;
        uint16_t channelPort;
    } coco_device_channel_handle_t;

    typedef  struct {
        uint32_t cmdSenderNodeId;
        char *resourceEui;
        uint32_t streamId;
        int32_t streamSessionId;
        uint32_t channelHandleCount;
        coco_device_channel_handle_t **channelHandleArr;
        char *streamDescription;
        void *streamContext;
    } coco_device_media_stream_handle_t;

    typedef struct {
        char *networkId;
        uint32_t nodeId;
        char *resourceEUI;
        int32_t capabilityId;
        int32_t attributeId;
    } coco_std_source_uri_t;
    typedef struct {
        char *networkId;
        uint32_t nodeId;
        char *resourceEUI;
        int32_t capabilityId;
        int32_t attributeId;
        uint16_t sceneId;
        uint16_t ruleId;
    } coco_std_upload_triggered_uri_t;

    typedef int64_t time_t;

    typedef struct {
        int32_t contentType;
        int32_t uploadTriggerType;
        coco_std_source_uri_t sourceUri;
        coco_std_upload_triggered_uri_t uploadTriggeredUri;
        uint16_t channelPortArrCount;
        uint16_t *channelPortArr;
        int32_t appendFlag;
        uint32_t offset;
        uint32_t size;
        char **channelDescriptionArr;
        uint32_t *channelRxBuffSizeArr;
        time_t createdTimestamp;
    } coco_std_cmd_storage_upload_t;

    typedef  struct {
        int32_t contentType;
        int32_t uploadTriggerType;
        coco_std_source_uri_t sourceUri;
        coco_std_upload_triggered_uri_t uploadTriggeredUri;
        uint16_t channelHandleCount;
        coco_device_channel_handle_t **channelHandleArr;
        void *uploadContext;
    } coco_device_storage_upload_handle_t;

    typedef void (* coco_device_resource_cmd_cb_t)(coco_std_resource_cmd_t *resourceCmd);
    typedef void (* coco_device_mgmt_cmd_cb_t)(coco_std_device_cmd_t *deviceCmd);
    typedef void (* coco_device_add_resource_status_cb_t)(int32_t status, void *context);
    typedef void (* coco_device_remove_resource_status_cb_t)(int32_t status, void *context);
    typedef void (* coco_device_mgmt_cmd_status_update_cb_t)(int32_t status, void *context);
    typedef void (* coco_device_resource_cmd_status_update_cb_t)(int32_t status, void *context);
    typedef void (* coco_device_advertise_resource_status_cb_t)(int32_t status, void *context);
    typedef void (* coco_device_show_message_status_cb_t)(int32_t status, void *context);
    typedef void (* coco_device_info_request_status_cb_t)(int32_t status, void *context);
    typedef void (* coco_device_info_response_cb_t)(coco_std_info_response_t *infoResponse, void *context);
    typedef void (* coco_device_info_response_status_cb_t)(int32_t status, void *context);
    typedef void (* coco_device_info_request_cb_t)(coco_std_info_request_t *infoRequest);
    typedef void (*coco_device_connect_status_cb_t)(int32_t status);
    typedef void (* coco_device_attribute_update_status_cb_t)(int32_t status, void *context);
    typedef void (*coco_device_tunnel_status_cb_t)(coco_device_tunnel_handle_t *tunnelHandle,
                                               int32_t tunnelStatus, uint16_t listeningPort);
    typedef void (* coco_device_firmware_update_cb_t)(coco_device_fw_update_details_t *fwUpdateDetails);
    typedef void (* coco_device_capability_update_status_cb_t)(int32_t status, void *context);
    typedef coco_device_tunnel_params_t *(* coco_device_get_tunnel_params_cb_t)(coco_std_resource_cmd_t *resourceCmdInfo,
                                                                            coco_std_status_code_t *status);
    typedef bool (*coco_device_media_stream_accept_cb_t)(char *resourceUri, uint16_t channelCount, uint16_t *portArray,
                                                     int32_t *streamTransportTypeArr, char *streamDescription,
                                                     void **streamContext, coco_std_status_code_t *status);
    typedef void (*coco_device_media_stream_status_cb_t)(coco_device_media_stream_handle_t *handle,
                                                     coco_device_channel_handle_t *channelHandle,
                                                     int32_t status, void *streamContext,
                                                     void *channelContext);
    typedef bool (*coco_device_storage_upload_accept_cb_t)(coco_std_cmd_storage_upload_t *storageUploadData,
                                                       char *resourceEui, void **uploadContext);
    typedef void (*coco_device_storage_upload_status_cb_t)(coco_device_storage_upload_handle_t *uploadHandle,
                                                       coco_device_channel_handle_t *channelHandle,
                                                       int32_t status, void *uploadContext,
                                                       void *channelContext);
    typedef void (*coco_device_active_tunnel_clients_cb_t)(uint32_t *activeTunnelClientArr,
                                                       uint16_t activeTunnelClientCount,
                                                       void *requestContext);
    typedef void (*coco_device_remove_status_cb_t)(int32_t status);
    typedef int32_t (*coco_device_remove_request_cb_t)(int32_t factoryResetFlag);
    typedef void (*coco_device_ap_listen_status_cb_t)(int32_t status, void *context);
    typedef void (*coco_device_ap_disconnect_status_cb_t)(int32_t status, void *context);
    typedef struct {
        uint32_t fastRetryDuration;
        uint32_t backgroundMaxRetryPeriod;
        uint32_t foregroundMaxRetryPeriod;
        uint32_t keepAliveInterval;
        uint32_t keepAliveTimeout;
    } coco_device_connectivity_timers_t;
    typedef void (*coco_device_ap_scan_ssid_cb_t)();
    typedef void (*coco_device_ap_send_ssid_status_cb_t)(int32_t status, void *context);
    typedef void (*coco_device_ap_wifi_cred_cb_t)(char *ssid, char*password);
    typedef void (*coco_device_internet_status_cb_t)(int32_t status, void *context);
    typedef bool (*coco_device_capture_snapshot_request_cb_t)(uint32_t snapshotId, char *resourceEui,
                                                          uint16_t pixelHeight, uint16_t pixelWidth);
    typedef void (*coco_device_capture_snapshot_status_cb_t)(uint32_t snapshotId, int status,
                                                         char *filePath, void *context);
    typedef void (*coco_device_removed_device_cb_t)(uint32_t deviceNodeId);
    typedef void (*coco_device_data_corruption_cb_t)();
    """)

ffi.cdef("""
typedef struct {
  char *cwdPath; //Used
  void *encryptionKey;
  uint32_t encryptionKeyLen;
  char *configFilePath; //Used
  char *downloadPath; //Used
  char *tempPath; //Used
  char *firmwareVersion; //Used
  int32_t *protocolIdArr;
  uint32_t protocolIdArrCnt;
  int32_t isExtendable; //Used
  int32_t powerSource; //Used
  int32_t receiverType; //Used
  int32_t skipSSLVerification; //Used
  char *canonicalHostNameList;
  uint16_t clusterPort;
  int32_t ssidScanAvailable;
  int32_t dontPersistData;
  char *tmpCwdPath;

  coco_device_resource_cmd_cb_t resourceCmdCb; //Used

  coco_device_mgmt_cmd_cb_t devMgmtCmdCb;
  coco_device_add_resource_status_cb_t addResStatusCb; //Used
  coco_device_remove_resource_status_cb_t remResStatusCb;
  coco_device_mgmt_cmd_status_update_cb_t devMgmtCmdStatusCb;
  coco_device_resource_cmd_status_update_cb_t resourceCmdStatusCb;
  coco_device_advertise_resource_status_cb_t advResStatusCb;
  coco_device_show_message_status_cb_t showMsgStatusCb;
  coco_device_info_request_status_cb_t infoReqStatusCb;
  coco_device_info_response_cb_t infoResponseCb;
  coco_device_info_response_status_cb_t infoRespStatusCb;
  coco_device_info_request_cb_t infoRequestCb;
  coco_device_connect_status_cb_t coconetConnStatusCb; //Used
  coco_device_attribute_update_status_cb_t attributeUpdateCb; //Used
  coco_device_tunnel_status_cb_t tunnelStatusCb;
  coco_device_firmware_update_cb_t firmwareUpdateCb;
  coco_device_capability_update_status_cb_t capabilityUpdateCb;
  coco_device_get_tunnel_params_cb_t getTunnelParamsCb;
  coco_device_media_stream_accept_cb_t mediaStreamAcceptCb;
  coco_device_media_stream_status_cb_t mediaStreamStatusCb;
  coco_device_storage_upload_accept_cb_t storageUploadAcceptCb;
  coco_device_storage_upload_status_cb_t storageUploadStatusCb;
  coco_device_active_tunnel_clients_cb_t activeTunnelClientsCb;
  coco_device_remove_status_cb_t removeDeviceStatusCb;
  coco_device_remove_request_cb_t removeDeviceRequestCb;
  coco_device_ap_listen_status_cb_t apListenStatusCb;
  coco_device_ap_disconnect_status_cb_t apDisconnectStatusCb;
  coco_device_connectivity_timers_t *connectivityTimers;
  coco_device_ap_scan_ssid_cb_t scanSsidCb;
  coco_device_ap_send_ssid_status_cb_t sendSsidStatusCb;
  coco_device_ap_wifi_cred_cb_t wifiCredCb;
  coco_device_internet_status_cb_t internetCb;
  coco_device_capture_snapshot_request_cb_t captureSnapshotRequestCb;
  coco_device_capture_snapshot_status_cb_t captureSnapshotStatusCb;
  coco_device_removed_device_cb_t removedDeviceCb;
  coco_device_data_corruption_cb_t dataCorruptionCb; //Used
} coco_device_init_params_t;

    int32_t coco_device_init(coco_device_init_params_t *params);

    typedef struct {
        char *networkId;
        uint32_t deviceNodeId;
        char *resourceEui;
        char *resourceName;
        char *manufacturer;
        char *model;
        char *firmwareVersion;
        char *metadata;
        int32_t powerSource;        // It will take values from the enum - coco_std_power_source_t
        int32_t receiverType;       // It will take values from the enum - coco_std_receiver_type_t
        int32_t explorationStatus;  // It takes values from the enum coco_std_status_code_t.
                                    // The possible values are COCO_STD_STATUS_SUCCESS,
                                    // COCO_STD_STATUS_PARTIAL_SUCCESS,
                                    // COCO_STD_STATUS_RESOURCE_NOT_SUPPORTED,
                                    // COCO_STD_STATUS_SUCCESS_INSECURE,
                                    // COCO_STD_STATUS_PARTIAL_SUCCESS_INSECURE
        uint16_t createdByUserId;   // Used internally by the COCO SDKs
        time_t createdTimestamp;    // Used internally by the COCO SDKs
    } coco_std_resource_summary_info_t;

    typedef enum {
        COCO_STD_DATA_TYPE_MIN = -1,
        COCO_STD_DATA_TYPE_BOOLEAN,
        COCO_STD_DATA_TYPE_BOOLEAN_ARR,
        COCO_STD_DATA_TYPE_STRING,
        COCO_STD_DATA_TYPE_STRING_ARR,
        COCO_STD_DATA_TYPE_UINT8,
        COCO_STD_DATA_TYPE_UINT8_ARR,
        COCO_STD_DATA_TYPE_UINT16,
        COCO_STD_DATA_TYPE_UINT16_ARR,
        COCO_STD_DATA_TYPE_UINT32,
        COCO_STD_DATA_TYPE_UINT32_ARR,
        COCO_STD_DATA_TYPE_UINT64,
        COCO_STD_DATA_TYPE_UINT64_ARR,
        COCO_STD_DATA_TYPE_INT8,
        COCO_STD_DATA_TYPE_INT8_ARR,
        COCO_STD_DATA_TYPE_INT16,
        COCO_STD_DATA_TYPE_INT16_ARR,
        COCO_STD_DATA_TYPE_INT32,
        COCO_STD_DATA_TYPE_INT32_ARR,
        COCO_STD_DATA_TYPE_INT64,
        COCO_STD_DATA_TYPE_INT64_ARR,
        COCO_STD_DATA_TYPE_FLOAT,
        COCO_STD_DATA_TYPE_FLOAT_ARR,
        COCO_STD_DATA_TYPE_DOUBLE,
        COCO_STD_DATA_TYPE_DOUBLE_ARR,
        COCO_STD_DATA_TYPE_JSON_STRING,
        COCO_STD_DATA_TYPE_JSON_STRING_ARR,
        COCO_STD_DATA_TYPE_MAX,
        COCO_STD_DATA_TYPE_UBOUND = 0x7FFFFFFF
    } coco_std_data_type_t;

    typedef enum {
        COCO_STD_CAP_MIN = -1,
        COCO_STD_CAP_ON_OFF_CONTROL,
        COCO_STD_CAP_LEVEL_CTRL,
        COCO_STD_CAP_COLOR_CTRL,
        COCO_STD_CAP_LOCK_CONTROL,
        COCO_STD_CAP_ENERGY_METERING,
        COCO_STD_CAP_MOTION_SENSING,
        COCO_STD_CAP_OCCUPANCY_SENSING,
        COCO_STD_CAP_CONTACT_SENSING,
        COCO_STD_CAP_FLUID_LEVEL_MEASUREMENT,
        COCO_STD_CAP_FIRE_SENSING,
        COCO_STD_CAP_TEMPERATURE_MEASUREMENT,
        COCO_STD_CAP_ILLUMINANCE_MEASUREMENT,
        COCO_STD_CAP_POWER_LEVEL_MEASUREMENT,
        COCO_STD_CAP_TUNNEL_CONTROL,
        COCO_STD_CAP_REL_HUMIDITY_MEASUREMENT,
        COCO_STD_CAP_KEYPRESS_SENSING,
        COCO_STD_CAP_WARNING_DEV_CONTROL,
        COCO_STD_CAP_NETWORK_CONFIGURATION,
        COCO_STD_CAP_MEDIA_STREAM,
        COCO_STD_CAP_STORAGE_CONFIG,
        COCO_STD_CAP_STORAGE_CONTROL,
        COCO_STD_CAP_MOTOR_CTRL,
        COCO_STD_CAP_IMAGE_CTRL,
        COCO_STD_CAP_SNAPSHOT,
        COCO_STD_CAP_STATIONARY_POSITION,
        COCO_STD_CAP_REAL_TIME_POSITION,
        COCO_STD_CAP_VIBRATION_SENSING,
        COCO_STD_CAP_AIR_QUALITY_SENSING,
        COCO_STD_CAP_WINDOW_COVERING,
        COCO_STD_CAP_MAX,
        COCO_STD_CAP_UBOUND = 0x7FFFFFFF
    } coco_std_capability_t;

    typedef enum {
        COCO_STD_POWER_SRC_MIN = -1,
        COCO_STD_POWER_SRC_UNKNOWN,
        COCO_STD_POWER_SRC_MAINS_SINGLE_PHASE,
        COCO_STD_POWER_SRC_MAINS_3_PHASE,
        COCO_STD_POWER_SRC_MAINS_UNKNOWN_PHASE,
        COCO_STD_POWER_SRC_BATTERY,
        COCO_STD_POWER_SRC_DC_SOURCE,
        COCO_STD_POWER_SRC_EMERGENCY_CONST_POWER,
        COCO_STD_POWER_SRC_EMERGENCY_TRANSFER_SWITCH,
        COCO_STD_POWER_SRC_NOT_AVAILABLE,
        COCO_STD_POWER_SRC_MAX,
        COCO_STD_POWER_SRC_UBOUND = 0x7FFFFFFF
    } coco_std_power_source_t;

    typedef enum {
        COCO_STD_RCVR_TYPE_MIN = -1,
        COCO_STD_RCVR_TYPE_RX_ON_WHEN_IDLE,
        COCO_STD_RCVR_TYPE_PERIODIC,
        COCO_STD_RCVR_TYPE_WHEN_STIMULATED,
        COCO_STD_RCVR_TYPE_NOT_AVAILABLE,
        COCO_STD_RCVR_TYPE_MAX,
        COCO_STD_RCVR_TYPE_UBOUND = 0x7FFFFFFF
    } coco_std_receiver_type_t;

    typedef enum {
    COCO_STD_ATTR_NW_CONFIG_MIN = -1,
    COCO_STD_ATTR_NW_CONFIG_RSSI,
    COCO_STD_ATTR_NW_CONFIG_NW_NAME,
    COCO_STD_ATTR_NW_CONFIG_MAX,
    COCO_STD_ATTR_NW_CONFIG_UBOUND = 0x7FFFFFFF
    } coco_std_attr_nw_config_t;

    typedef enum {
        COCO_STD_ATTR_ILLUMINANCE_MIN = -1,
        COCO_STD_ATTR_CURRENT_LUMINANCE_LUX,
        COCO_STD_ATTR_ILLUMINANCE_MAX,
        COCO_STD_ATTR_ILLUMINANCE_UBOUND = 0x7FFFFFFF
    } coco_std_attr_illuminance_t;

    typedef enum {
        COCO_STD_ATTR_LEVEL_MIN = -1,
        COCO_STD_ATTR_LEVEL_PCT,
        COCO_STD_ATTR_LEVEL_MAX,
        COCO_STD_ATTR_LEVEL_UBOUND = 0x7FFFFFFF
    } coco_std_attr_level_t;

    typedef enum {
        COCO_STD_ATTR_ON_OFF_MIN = -1,
        COCO_STD_ATTR_ON_FLAG,
        COCO_STD_ATTR_ON_OFF_MAX,
        COCO_STD_ATTR_ON_OFF_UBOUND = 0x7FFFFFFF
    } coco_std_attr_on_off_t;

    typedef enum {
        COCO_STD_CMD_ON_OFF_MIN = -1,
        COCO_STD_CMD_ON,
        COCO_STD_CMD_OFF,
        COCO_STD_CMD_ON_OFF_TOGGLE,
        COCO_STD_CMD_FETCH_ON_OFF_STATUS,
        COCO_STD_CMD_ON_OFF_MAX,
        COCO_STD_CMD_ON_OFF_UBOUND = 0x7FFFFFFF
    } coco_std_cmd_on_off_t;

    typedef enum {
        COCO_STD_CMD_LEVEL_MIN = -1,
        COCO_STD_CMD_SET_LEVEL,
        COCO_STD_CMD_SET_LEVEL_WITH_ON_OFF,
        COCO_STD_CMD_FETCH_LEVEL,
        COCO_STD_CMD_LEVEL_MAX,
        COCO_STD_CMD_LEVEL_UBOUND = 0x7FFFFFFF
    } coco_std_cmd_level_t;
    
    typedef struct {
        char *networkId;
        uint32_t deviceNodeId;
        char *resourceEui;
        int32_t capabilityId; // It will take values from the enum - coco_std_capability_t
        char *capabilityName;
        uint32_t stdCmdArrCount;
        int32_t *stdCmdArr;
        uint16_t createdByUserId;           // Used internally by the COCO SDKs
        time_t createdTimestamp;            // Used internally by the COCO SDKs
    } coco_std_resource_capability_info_t;

    typedef struct {
        char *networkId;
        uint32_t deviceNodeId;
        char *resourceEui;
        int32_t capabilityId;             // It will take values from the enum - coco_std_capability_t
        char *capabilityName;
        int32_t attributeId;
        char *attribName;
        char *attribDesc;
        int32_t dataType;                 // It will take values from the enum - coco_std_data_type_t
        uint32_t dataArrayLen;            // Length of the array if dataType is an array
        void *minValue;
        void *maxValue;
        void *defaultValue;
        void *currentValue;
        uint32_t minReportingIntervalMs;
        uint32_t maxReportingIntervalMs;
        void *reportableChange;
        int32_t isRealTimeUpdate;         // If this is being sent as a result of resource updating its state,
                                            // set it as 1. Otherwise, if the old state is being sent, set it as 0
        uint16_t createdByUserId;         // Used internally by the COCO SDKs
        time_t createdTimestamp;          // Used internally by the COCO SDKs
        time_t lastUpdateTimestamp;
    } coco_std_resource_attribute_info_t;

    typedef struct {
        coco_std_resource_capability_info_t resourceCapabilityInfo;
        uint32_t attributeArrCount;
        coco_std_resource_attribute_info_t *attributeArr;
    } coco_std_resource_capability_t;

    typedef struct {
        coco_std_resource_summary_info_t resourceSummaryInfo;
        uint32_t capabilityArrCount;
        coco_std_resource_capability_t *capabilityArr;
    } coco_std_resource_t;

    int32_t coco_device_add_resource(coco_std_resource_t *resourceArr, uint32_t resourceArrCnt,
                                 uint32_t cmdSeqNum, uint32_t cmdSenderNodeId,
                                 void *context);

    int32_t  coco_device_resource_attribute_update(coco_std_resource_attribute_info_t *resourceAttribute,
                                              void *context);

    int32_t coco_device_init_auth(void);
    """)


    #for callbacks
ffi.cdef("""
    extern "Python+C" void coco_device_join_nw_status_cb(int32_t status);
    extern "Python+C" void coco_device_add_res_status_cb(int32_t status, void *context);
    extern "Python+C" void coco_device_attribute_update_status(int32_t status, void *context);
    extern "Python+C" void coco_device_data_corruption_cb();
    extern "Python+C" void coco_device_resource_cmd_cb(coco_std_resource_cmd_t *resourceCmd);
    """)


 #The C library to open
ffi.set_source("_my_coco",
"""
    #include <stdlib.h>

    #include <string.h>
    #include <stdio.h>
    #include <unistd.h>
    #include <time.h>
    #include <stdbool.h>
    #include <stdint.h>
    #include "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocodevicesdk/coco_device_api.h"
    #include "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocostandard/coco_std_api.h"
    #include "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocostandard/coco_std_data_storage_control_types.h"
    #include "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocostandard/coco_std_data_network_config_types.h"
    #include "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocostandard/coco_std_data_illuminance_types.h"
    #include "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocostandard/coco_std_data_level_types.h"
    #include "/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocostandard/coco_std_data_on_off_types.h"
    
    
    
""", 
    library_dirs = ['/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocodevicesdk/', 
                    '/mnt/host/tmp/workspace/cocosdk/cocodevicesdk/dist/c/0.65.2/include/cocostandard/'],
    libraries = ["cocodevicesdk"])


ffi.compile(verbose=True)

