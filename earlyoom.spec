#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: c1050fe
#
Name     : earlyoom
Version  : 1.7
Release  : 18
URL      : https://github.com/rfjakob/earlyoom/archive/v1.7/earlyoom-1.7.tar.gz
Source0  : https://github.com/rfjakob/earlyoom/archive/v1.7/earlyoom-1.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: earlyoom-bin = %{version}-%{release}
Requires: earlyoom-data = %{version}-%{release}
Requires: earlyoom-license = %{version}-%{release}
Requires: earlyoom-man = %{version}-%{release}
Requires: earlyoom-services = %{version}-%{release}
BuildRequires : pandoc
BuildRequires : systemd
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-clear-telemetry-example.patch
Patch2: 0002-Clear-Telemetry-earlyoom-probe.patch

%description
earlyoom - The Early OOM Daemon
===============================
[![CI](https://github.com/rfjakob/earlyoom/actions/workflows/ci.yml/badge.svg)](https://github.com/rfjakob/earlyoom/actions/workflows/ci.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/release/rfjakob/earlyoom.svg)](https://github.com/rfjakob/earlyoom/releases)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/rfjakob/earlyoom.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/rfjakob/earlyoom/alerts/)
[![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/rfjakob/earlyoom.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/rfjakob/earlyoom/context:cpp)

%package bin
Summary: bin components for the earlyoom package.
Group: Binaries
Requires: earlyoom-data = %{version}-%{release}
Requires: earlyoom-license = %{version}-%{release}
Requires: earlyoom-services = %{version}-%{release}

%description bin
bin components for the earlyoom package.


%package data
Summary: data components for the earlyoom package.
Group: Data

%description data
data components for the earlyoom package.


%package license
Summary: license components for the earlyoom package.
Group: Default

%description license
license components for the earlyoom package.


%package man
Summary: man components for the earlyoom package.
Group: Default

%description man
man components for the earlyoom package.


%package services
Summary: services components for the earlyoom package.
Group: Systemd services
Requires: systemd

%description services
services components for the earlyoom package.


%prep
%setup -q -n earlyoom-1.7
cd %{_builddir}/earlyoom-1.7
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701953209
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
make  %{?_smp_mflags}  PREFIX=/usr


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
export SOURCE_DATE_EPOCH=1701953209
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/earlyoom
cp %{_builddir}/earlyoom-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/earlyoom/49c65c4ad5a142b45b01486ac9df8f15d9d6d30b || :
%make_install PREFIX=/usr
## install_append content
install -D %{buildroot}/etc/default/earlyoom %{buildroot}/usr/share/defaults/earlyoom/earlyoom
install -D %{buildroot}/etc/systemd/system/earlyoom.service %{buildroot}/usr/lib/systemd/system/earlyoom.service
install -m0755 earlyoom-clr-telemetry %{buildroot}/usr/bin/earlyoom-clr-telemetry
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/earlyoom
/usr/bin/earlyoom-clr-telemetry

%files data
%defattr(-,root,root,-)
/usr/share/defaults/earlyoom/earlyoom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/earlyoom/49c65c4ad5a142b45b01486ac9df8f15d9d6d30b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/earlyoom.1.gz

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/earlyoom.service
