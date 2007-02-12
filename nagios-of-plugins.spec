%include	/usr/lib/rpm/macros.perl
Summary:	Open Fusion Nagios Plugins
Summary(pl.UTF-8):   Wtyczki Nagiosa Open Fusion
Name:		nagios-of-plugins
Version:	0.5.2
Release:	0.3
License:	GPL
Group:		Networking
Source0:	http://www.openfusion.com.au/labs/dist/%{name}-%{version}.tar.gz
# Source0-md5:	ce52d3a15c909cf2d44737b40d9d7473
Patch0:		%{name}-jabber.patch
URL:		http://www.openfusion.com.au/labs/nagios/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
Requires:	perl-Nagios-Plugin = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios

%description
Nagios Plugin Package for monitoring of outstanding updates via 'yum'
or 'up2date', various constraints on a given file, inode usage across
all partitions, status of all Linux software RAID devices, kernel
version, length of the qmail mail queue.

%description -l pl.UTF-8
Pakiet wtyczek Nagiosa do monitorowania zaległych uaktualnień przez
yuma lub up2daet, różnych ograniczeń dla danego pliku, wykorzystania
i-węzłów na wszystkich partycjach, stanu wszystkich programowych
linuksowych urządzeń RAID, wersji jądra, długości kolejki pocztowej
qmaila.

%package -n perl-Nagios-Plugin
Summary:	Perl module for creating Nagios plugins
Summary(pl.UTF-8):   Moduł Perla do tworzenia wtyczek Nagiosa
Group:		Development/Languages/Perl

%description -n perl-Nagios-Plugin
Nagios::Plugin is a Perl module for simplifying the creation of Nagios
plugins, mainly by standardising some of the argument parsing and
handling stuff most plugins require.

%description -n perl-Nagios-Plugin -l pl.UTF-8
Nagios::Plugin to moduł Perla upraszczający tworzenie wtyczek Nagiosa,
głównie poprzez standaryzację przetwarzania niektórych argumentów i
obsługi rzeczy wymaganych przez większość wtyczek.

%package -n nagios-notify_by_jabber
Summary:	Utility to send Nagios alerts using Jabber
Summary(pl.UTF-8):   Narzędzie do wysyłania alarmów Nagiosa przy użyciu Jabbera
Group:		Networking
Requires:	nagios-core
Requires:	perl-IO-Socket-SSL

%description -n nagios-notify_by_jabber
Utility to send Nagios alerts using Jabber.

%description -n nagios-notify_by_jabber -l pl.UTF-8
Narzędzie do wysyłania alarmów Nagiosa przy użyciu Jabbera.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir},%{perl_vendorlib}}

cp -a check* notify* $RPM_BUILD_ROOT%{_plugindir}
cp -a Nagios $RPM_BUILD_ROOT%{perl_vendorlib}
cat <<EOF > $RPM_BUILD_ROOT%{_sysconfdir}/jabber.cfg
;jabber_user=
;jabber_pass=
;jabber_server=jabber.org
;jabber_port=5222
;jabber_resource=nagios
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_plugindir}/check_file
%attr(755,root,root) %{_plugindir}/check_inodes
%attr(755,root,root) %{_plugindir}/check_kernel_version
%attr(755,root,root) %{_plugindir}/check_linux_raid
%attr(755,root,root) %{_plugindir}/check_qmailq
%attr(755,root,root) %{_plugindir}/check_yum

%files -n nagios-notify_by_jabber
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/jabber.cfg
%attr(755,root,root) %{_plugindir}/notify_by_jabber

%files -n perl-Nagios-Plugin
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Nagios
%{perl_vendorlib}/Nagios/Plugin.pm
