Name:     libqmatrixclient-qt5
Summary:  Matrix Qt library

%define version_major 0
%define version_minor 5
%define version_patch 1.2

Version: %{version_major}.%{version_minor}.%{version_patch}
Release:  1
Group:    Development/Libraries
License:  LGPL2.1
URL:      https://github.com/QMatrixClient/libqmatrixclient
Source0:  %{name}-%{version}.tar.xz
Requires: qt5-qtcore
Requires: qt5-qtnetwork
Requires: qt5-qtgui
Requires: qt5-qtmultimedia
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: cmake >= 3.1
BuildRequires: opt-gcc6

BuildRequires: qt5-qtmultimedia-plugin-mediaservice-gstcamerabin
BuildRequires: qt5-qtmultimedia-plugin-mediaservice-gstmediacapture
BuildRequires: qt5-qtmultimedia-plugin-audio-alsa
BuildRequires: qt5-qtmultimedia-plugin-mediaservice-gstaudiodecoder
BuildRequires: qt5-qtmultimedia-plugin-mediaservice-gstmediaplayer
BuildRequires: qt5-qtmultimedia-plugin-playlistformats-m3u
BuildRequires: qt5-qtmultimedia-plugin-audio-pulseaudio
BuildRequires: qt5-qtmultimedia-plugin-resourcepolicy-resourceqt

%description
%{summary}.

%package devel
Summary:    Development files for Matrix Qt library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   qt5-qtmultimedia-devel
%description devel
%{summary}.

%package example
Summary:    An example application for Matrix Qt library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
%description example
%{summary}.


%prep
%setup -q

%build
%define cmake_build %__cmake --build .
%define cmake_install DESTDIR=%{?buildroot} %__cmake --build . --target install


%cmake \
    -DCMAKE_CXX_COMPILER=/opt/gcc6/bin/g++ \
    -DCMAKE_SHARED_LINKER_FLAGS="-L/opt/gcc6/lib -static-libstdc++" \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/libqmatrixclient-qt5 \
    -DBUILD_SHARED_LIBS=ON

%cmake_build

%install
rm -rf %{buildroot}
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libQMatrixClient.so.%{version_major}.%{version_minor}.%{version_patch}
%{_libdir}/libQMatrixClient.so.%{version}
%{_libdir}/libQMatrixClient.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/libqmatrixclient-qt5
%{_libdir}/libQMatrixClient.so
%{_libdir}/pkgconfig/QMatrixClient.pc
%{_libdir}/cmake/QMatrixClient

%files example
%defattr(-,root,root,-)
%{_bindir}/* 
