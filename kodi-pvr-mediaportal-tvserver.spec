%global commit d261c83a4ab40441be32c1202138fc6409a22974
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170407

%global kodi_addon pvr.mediaportal.tvserver
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        2.4.19
Release:        1%{?dist}
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
* Sat Apr 29 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:2.4.19-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.13.9-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.9-1
- Initial RPM release
