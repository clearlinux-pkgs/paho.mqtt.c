#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe40c24
#
Name     : paho.mqtt.c
Version  : 1.3.13
Release  : 16
URL      : https://github.com/eclipse/paho.mqtt.c/archive/v1.3.13/paho.mqtt.c-1.3.13.tar.gz
Source0  : https://github.com/eclipse/paho.mqtt.c/archive/v1.3.13/paho.mqtt.c-1.3.13.tar.gz
Summary  : MQTT C Client
Group    : Development/Tools
License  : BSD-3-Clause EPL-1.0 EPL-2.0
Requires: paho.mqtt.c-bin = %{version}-%{release}
Requires: paho.mqtt.c-lib = %{version}-%{release}
Requires: paho.mqtt.c-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : openssl-dev
BuildRequires : pkgconfig(openssl)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The Paho MQTT C Client is a fully fledged MQTT client written in ANSI standard C.

%package bin
Summary: bin components for the paho.mqtt.c package.
Group: Binaries
Requires: paho.mqtt.c-license = %{version}-%{release}

%description bin
bin components for the paho.mqtt.c package.


%package dev
Summary: dev components for the paho.mqtt.c package.
Group: Development
Requires: paho.mqtt.c-lib = %{version}-%{release}
Requires: paho.mqtt.c-bin = %{version}-%{release}
Provides: paho.mqtt.c-devel = %{version}-%{release}
Requires: paho.mqtt.c = %{version}-%{release}

%description dev
dev components for the paho.mqtt.c package.


%package lib
Summary: lib components for the paho.mqtt.c package.
Group: Libraries
Requires: paho.mqtt.c-license = %{version}-%{release}

%description lib
lib components for the paho.mqtt.c package.


%package license
Summary: license components for the paho.mqtt.c package.
Group: Default

%description license
license components for the paho.mqtt.c package.


%prep
%setup -q -n paho.mqtt.c-1.3.13
cd %{_builddir}/paho.mqtt.c-1.3.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701974181
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DPAHO_WITH_SSL=true \
-DPAHO_BUILD_SAMPLES=false \
-DPAHO_ENABLE_CPACK=false \
-DPAHO_ENABLE_TESTING=true
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701974181
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/paho.mqtt.c
cp %{_builddir}/paho.mqtt.c-%{version}/edl-v10 %{buildroot}/usr/share/package-licenses/paho.mqtt.c/03b5669874cbaabe055c6d130446ade35b3f8c65 || :
cp %{_builddir}/paho.mqtt.c-%{version}/epl-v20 %{buildroot}/usr/share/package-licenses/paho.mqtt.c/b086d72d0fe9af38418dab524fe76eea3cb1eec3 || :
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/share/doc/Eclipse\ Paho\ C/*.c

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/MQTTVersion

%files dev
%defattr(-,root,root,-)
/usr/include/MQTTAsync.h
/usr/include/MQTTClient.h
/usr/include/MQTTClientPersistence.h
/usr/include/MQTTExportDeclarations.h
/usr/include/MQTTProperties.h
/usr/include/MQTTReasonCodes.h
/usr/include/MQTTSubscribeOpts.h
/usr/lib64/cmake/eclipse-paho-mqtt-c/eclipse-paho-mqtt-cConfig-relwithdebinfo.cmake
/usr/lib64/cmake/eclipse-paho-mqtt-c/eclipse-paho-mqtt-cConfig.cmake
/usr/lib64/cmake/eclipse-paho-mqtt-c/eclipse-paho-mqtt-cConfigVersion.cmake
/usr/lib64/libpaho-mqtt3a.so
/usr/lib64/libpaho-mqtt3as.so
/usr/lib64/libpaho-mqtt3c.so
/usr/lib64/libpaho-mqtt3cs.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpaho-mqtt3a.so.1
/usr/lib64/libpaho-mqtt3a.so.1.3.13
/usr/lib64/libpaho-mqtt3as.so.1
/usr/lib64/libpaho-mqtt3as.so.1.3.13
/usr/lib64/libpaho-mqtt3c.so.1
/usr/lib64/libpaho-mqtt3c.so.1.3.13
/usr/lib64/libpaho-mqtt3cs.so.1
/usr/lib64/libpaho-mqtt3cs.so.1.3.13

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/paho.mqtt.c/03b5669874cbaabe055c6d130446ade35b3f8c65
/usr/share/package-licenses/paho.mqtt.c/b086d72d0fe9af38418dab524fe76eea3cb1eec3
