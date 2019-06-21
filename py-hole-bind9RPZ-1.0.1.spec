Name:           py-hole-bind9RPZ
Version:        1.0.1
Release:        0
Summary:        A Pi-hole inspired DNS firewall for use with bind/named using RPZ

Group:          Illallangi
BuildArch:      noarch
License:        GPL
URL:            https://bluedrill.github.io/py-hole
Source0:        py-hole-bind9RPZ-1.0.1.tar.gz

Requires:       python3-yaml => 5.1-1, python3-requests => 2.21.0-2.fc30
Obsoletes:      %{name} <= %{version}
Provides:       %{name} = %{version}

%description
A Pi-hole inspired DNS firewall for use with bind/named using RPZ

%prep

%setup -q

%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 0755 py-hole-bind9RPZ $RPM_BUILD_ROOT/usr/sbin/py-hole-bind9RPZ

%files
/usr/sbin/py-hole-bind9RPZ

%changelog
* Fri Jun 21 2019 Andrew Cole  1.0.1
  - Initial rpm release
