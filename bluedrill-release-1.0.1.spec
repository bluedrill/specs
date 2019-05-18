Name:           bluedrill-release
Version:        1.0.1
Release:        0
Summary:        Installs the BlueDrill Repository

Group:          Illallangi
BuildArch:      noarch
License:        GPL
URL:            https://bluedrill.github.io/bluedrill-release
Source0:        bluedrill-release-1.0.1.tar.gz

%description
Installs the BlueDrill Repository

%prep
%setup -q
%build
%install
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 0644 bluedrill.repo $RPM_BUILD_ROOT/etc/yum.repos.d/bluedrill.repo

%files
/etc/yum.repos.d/bluedrill.repo

%changelog
* Sat May 18 2019 Andrew Cole  1.0.1
  - Initial rpm release
