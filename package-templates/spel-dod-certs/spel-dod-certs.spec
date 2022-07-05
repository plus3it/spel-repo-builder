Name:           spel-dod-certs
Version:        5.9
Release:        1%{?dist}
Summary:        Installs and updates DoD CA Certificates

Group:          System Environment/Base
License:        Apache 2.0
URL:            https://github.com/plus3it/spel/
Vendor:         Plus3 IT Systems
Packager:       Plus3 IT Systems <spel@plus3it.com>

Source0:        LICENSE
Source1:        DoD_CAs.pem

BuildArch:      noarch
BuildRequires:  rpm

%description
This package installs and updates DoD CA certificates.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# Install certs
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/ca-trust/source/anchors/SPEL_DoD_CAs.pem

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
/etc/pki/ca-trust/source/anchors/SPEL_DoD_CAs.pem

%post
# update trust store
update-ca-trust force-enable
update-ca-trust extract

%changelog
* Thu Jun 30 2022 Loren Gordon <loren.gordon@plus3it.com>
- Initial packaging of spel-dod-certs, v5.9
