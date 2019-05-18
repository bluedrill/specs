Name:           ansible-soe
Version:        1.0.1
Release:        0
Summary:        Ansible SOE

Group:          Illallangi
BuildArch:      noarch
License:        GPL
URL:            https://bluedrill.github.io/ansible-soe
Source0:        ansible-soe-1.0.1.tar.gz

Requires:       git >= 1.8.3.1, ansible >= 2.7.5, python3-netaddr >= 0.7.19-14
Obsoletes:      %{name} <= %{version}
Provides:       %{name} = %{version}

%description
Applies an Ansible Playbook from a Git repository on service start

%prep

%setup -q

%build

%install

mkdir -p $RPM_BUILD_ROOT/sbin
install -m 0755 ansible-soe $RPM_BUILD_ROOT/sbin/ansible-soe
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
install -m 0644 ansible-soe.service $RPM_BUILD_ROOT/usr/lib/systemd/system/ansible-soe.service

%post

systemctl daemon-reload > /dev/null
systemctl enable ansible-soe.service > /dev/null

%files
/sbin/ansible-soe
/usr/lib/systemd/system/ansible-soe.service

%changelog
* Sun May 19 2019 Andrew Cole  1.0.1
  - Initial rpm release
