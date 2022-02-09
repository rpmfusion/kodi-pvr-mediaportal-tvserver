%global kodi_addon pvr.mediaportal.tvserver
%global kodi_version 19.0
%global kodi_codename Matrix

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        8.2.1
Release:        3%{?dist}
Summary:        MediaPortal PVR for Kodi

# Bundled live555 is LGPLv2+. See
# https://github.com/kodi-pvr/pvr.mediaportal.tvserver/pull/52#issuecomment-258505810
# for explanation about this bundling
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  pkgconfig(tinyxml)
Requires:       kodi >= %{kodi_version}
Provides:       bundled(live555) = 2010.03.16
ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename}


%build
%cmake3
%cmake3_build


%install
%cmake3_install


%files
%doc README.md %{kodi_addon}/changelog.txt src/README
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:8.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:8.2.1-1
- Update to 8.2.1

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:8.1.0-1
- Update to 8.1.0

* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:8.0.0-1
- Update to 8.0.0

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:6.0.1-1
- Update to 6.0.1 (switch to Matrix branch)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.18-1
- Update to 3.5.18

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.6-2
- Enable arm build

* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.5.6-1
- Update to 3.5.6
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.3-1
- Update to latest stable release for Kodi 18

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
