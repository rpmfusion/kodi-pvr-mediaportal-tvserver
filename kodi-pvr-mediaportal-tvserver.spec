%global commit dece80d3f144c3bfd0026e67d0e9f6f95eae6db8
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170621

%global kodi_addon pvr.mediaportal.tvserver
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        2.4.20
Release:        3%{?dist}
Summary:        Kodi's MediaPortal TVServer client addon

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
BuildRequires:  tinyxml-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
Kodi frontend for the MediaPortal TV Server (FFmpeg + TSReader
version). Supports streaming of live TV & recordings, listening to radio
channels, EPG and timers. This addon combines the former FFmpeg and TSReader
addons.

Note: this package requires the TVServerXBMC plugin (available at
http://www.scintilla.utwente.nl/~marcelg/xbmc/tvserverxbmc.html) to be installed
on the MediaPortal TVServer backend.


%prep
%autosetup -n %{kodi_addon}-%{commit}


%build
export CFLAGS="$RPM_OPT_FLAGS -DXLOCALE_NOT_USED=1"
export CXXFLAGS="$RPM_OPT_FLAGS -DXLOCALE_NOT_USED=1"
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md src/README
%license %{kodi_addon}/LICENSE.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:2.4.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.20-2
- Fix build with glibc 2.26 (xlocale.h no longer available)

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.4.20-1
- Update to 2.4.20

* Sat Apr 29 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:2.4.19-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.13.9-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.9-1
- Initial RPM release
