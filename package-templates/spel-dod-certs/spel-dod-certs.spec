Name:           spel-dod-certs
Version:        {{.Env.SPEL_DOD_CERTS_VERSION}}
Release:        {{.Env.SPEL_DOD_CERTS_RELEASE}}
Summary:        Installs and updates DoD Certificates

Group:          System Environment/Base
License:        Apache 2.0
URL:            https://github.com/plus3it/spel/
Vendor:         Plus3 IT Systems
Packager:       Plus3 IT Systems <spel@plus3it.com>

Source0:        LICENSE
Source1:        DoD_CAs.pem
Source2:        WCF_CAs.pem

BuildArch:      noarch
BuildRequires:  rpm

%description
This package installs and updates DoD certificates.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build

%install
rm -rf $RPM_BUILD_ROOT

# Install certs
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/ca-trust/source/anchors/DoD_CAs.pem
install -Dpm 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/ca-trust/source/anchors/WCF_CAs.pem

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
/etc/pki/ca-trust/source/anchors/DoD_CAs.pem
/etc/pki/ca-trust/source/anchors/WCF_CAs.pem

%post
# update trust store
update-ca-trust force-enable
update-ca-trust extract

%changelog
* Thu Jun 30 2022 Loren Gordon <loren.gordon@plus3it.com>
- Initial packaging of spel-dod-certs
