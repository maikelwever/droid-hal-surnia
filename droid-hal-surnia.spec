# These and other macros are documented in dhd/droid-hal-device.inc

%define device surnia
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto E 2015 (LTE)

%define installable_zip 1

%define android_config \
#define QCOM_BSP 1\
%{nil}


%define straggler_files\
/init.mmi.boot.sh\
/init.mmi.dtv.sh\
/init.mmi.early_boot.sh\
/init.mmi.touch.sh\
/init.mmi.usb.sh\
/init.surnia.sh\
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
