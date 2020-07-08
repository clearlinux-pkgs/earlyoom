#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : earlyoom
Version  : 1.6.1
Release  : 13
URL      : https://github.com/rfjakob/earlyoom/archive/v1.6.1/earlyoom-1.6.1.tar.gz
Source0  : https://github.com/rfjakob/earlyoom/archive/v1.6.1/earlyoom-1.6.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: earlyoom-bin = %{version}-%{release}
Requires: earlyoom-data = %{version}-%{release}
Requires: earlyoom-license = %{version}-%{release}
Requires: earlyoom-man = %{version}-%{release}
Requires: earlyoom-services = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : pandoc
BuildRequires : systemd
Patch1: 0001-Add-clear-telemetry-example.patch
Patch2: 0002-Clear-Telemetry-earlyoom-probe.patch

%description
earlyoom - The Early OOM Daemon
===============================
[![Build Status](https://api.travis-ci.org/rfjakob/earlyoom.svg)](https://travis-ci.org/rfjakob/earlyoom)
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

%description services
services components for the earlyoom package.


%prep
%setup -q -n earlyoom-1.6.1
cd %{_builddir}/earlyoom-1.6.1
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594219508
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  PREFIX=/usr


%install
export SOURCE_DATE_EPOCH=1594219508
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/earlyoom
cp %{_builddir}/earlyoom-1.6.1/LICENSE %{buildroot}/usr/share/package-licenses/earlyoom/49c65c4ad5a142b45b01486ac9df8f15d9d6d30b
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
