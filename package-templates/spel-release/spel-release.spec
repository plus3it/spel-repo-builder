Name:           spel-release
Version:        {{.Env.SPEL_RELEASE_VERSION}}
Release:        {{.Env.SPEL_RELEASE_RELEASE}}
Summary:        SPEL-managed RPM repository configuration

Group:          System Environment/Base
License:        Apache 2.0
URL:            https://github.com/plus3it/spel/
Vendor:         Plus3 IT Systems
Packager:       Plus3 IT Systems <spel@plus3it.com>

Source0:        RPM-GPG-KEY-SPEL
Source1:        LICENSE
Source2:        spel.repo
Source3:        spel-release

BuildArch:      noarch
BuildRequires:  rpm
Requires:       ((redhat-release >=  {{.Env.SPEL_RELEASE_VERSION}} and redhat-release < {{ math.Add .Env.SPEL_RELEASE_VERSION 1 }}) or (system-release >= 2023 and system-release < 2024))
Conflicts:      fedora-release

%description
This package contains the STIG-Partitioned Enterprise Linux (spel) repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# GPG Key
 install -Dpm 644 %{SOURCE0} \
   $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-SPEL

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
%ghost /etc/spel-release
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Fri Sep 8 2025 Loren Gordon <loren.gordon@plus3it.com>
- Increases repo priority to prefer amazonlinux on AL2023

* Wed Sep 6 2025 Loren Gordon <loren.gordon@plus3it.com>
- Update "Requires" to allow installation on Amazon Linux 2023

* Wed Sep 27 2023 Loren Gordon <loren.gordon@plus3it.com>
- Fix "Requires" to restrict major version correctly

* Mon Jan 03 2022 Loren Gordon <loren.gordon@plus3it.com>
- Fix base url to work across multiple platforms

* Tue Nov 02 2021 Loren Gordon <loren.gordon@plus3it.com>
- Rework packaging and repo automation using docker

* Thu Jul 18 2019 Thomas H Jones II <thomas.jones@plus3it.com>
- Initial packaging of spel-related repo definitions
