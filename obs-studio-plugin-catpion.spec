%global srcname obs-catpion
%global commit 5d63d70293e6f5baa3d52ae62d53aef0a7690e84
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250320

Name:           obs-studio-plugin-catpion
Version:        0~git%{commitdate}.%{shortcommit}
Release:        %autorelease
Summary:        OBS text display plugin with many advanced features

License:        GPL-2.0-or-later
URL:            https://github.com/grillo-delmal/obs-catpion
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  g++
BuildRequires:  cmake(libobs)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(april-asr)
BuildRequires:  qt-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtbase-gui

Supplements:    obs-studio%{?_isa}

%description
Speech to text plugin for OBS.

%prep
%autosetup -n %{srcname}-%{commit}

%build
%cmake \
    -D CMAKE_INSTALL_LIBDIR=/usr/lib64/ \
    -D CMAKE_INSTALL_PREFIX=/usr \
    -D LINUX_PORTABLE=OFF \
    -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/obs-plugins/%{srcname}*
%{_datadir}/obs/obs-plugins/%{srcname}/

%changelog
%autochangelog
