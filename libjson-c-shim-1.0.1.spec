Name:           libjson-c-shim
Version:        1.0.1
Release:        0
Summary:        Shim to provide libjson-c.so.2 from Fedora's libjson package

Group:          Illallangi
BuildArch:      noarch
License:        GPL
URL:            https://bluedrill.github.io/libjson-c-shim
Source0:        libjson-c-shim-1.0.1.tar.gz

Requires:       json-c >= 0.13.1
Obsoletes:      %{name} <= %{version}
Provides:       json-c = 0.11-4.el7_0,json-c(x86-64) = 0.11-4.el7_0,libjson-c.so.2()(64bit),libjson.so.0()(64bit)


%description
Shim to provide libjson-c.so.2 from Fedora's libjson package

%prep

%setup -q

%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/lib64/

%post

ln -s $RPM_BUILD_ROOT/usr/lib64/libjson-c.so.4.0.0 $RPM_BUILD_ROOT/usr/lib64/libjson-c.so.2.0.0
ln -s $RPM_BUILD_ROOT/usr/lib64/libjson-c.so.4.0.0 $RPM_BUILD_ROOT/usr/lib64/libjson-c.so.2

%postun
rm -f $RPM_BUILD_ROOT/usr/lib64/libjson-c.so.2.0.0
rm -f $RPM_BUILD_ROOT/usr/lib64/libjson-c.so.2

%files

%changelog
* Sun May 19 2019 Andrew Cole  1.0.1
  - Initial RPM release
