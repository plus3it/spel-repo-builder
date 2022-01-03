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
Requires:       redhat-release >=  %{version}
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
* Mon Jan 03 2022 Loren Gordon <loren.gordon@plus3it.com>
- Fix base url to work across multiple platforms

* Tue Nov 02 2021 Loren Gordon <loren.gordon@plus3it.com>
- Rework packaging and repo automation using docker

* Thu Jul 18 2019 Thomas H Jones II <thomas.jones@plus3it.com>
- Initial packaging of spel-related repo definitions
