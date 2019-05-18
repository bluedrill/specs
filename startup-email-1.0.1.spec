Name:           startup-email
Version:        1.0.1
Release:        0
Summary:        A Bash Script to send Startup Notification Emails

Group:          Illallangi
BuildArch:      noarch
License:        GPL
URL:            https://bluedrill.github.io/startup-email
Source0:        startupemail-1.0.1.tar.gz

Requires:       mailx >= 12.5
Obsoletes:      %{name} <= %{version}
Provides:       %{name} = %{version}

%description
Sends an email to the Illallangi list server about a server starting up.
Original idea from https://savedlog.com/linux/server-send-email-on-boot/

%prep

%setup -q

%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 0755 startup-email $RPM_BUILD_ROOT/usr/sbin/startup-email
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
install -m 0644 startup-email.service $RPM_BUILD_ROOT/usr/lib/systemd/system/startup-email.service

%post

systemctl daemon-reload > /dev/null
systemctl enable startup-email.service > /dev/null

%files
/usr/sbin/startup-email
/usr/lib/systemd/system/startup-email.service

%changelog
* Sun May 19 2019 Andrew Cole  1.0.1
  - Initial rpm release

