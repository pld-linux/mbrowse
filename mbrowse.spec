Summary:	SNMP MIB browser
Summary(pl):	Przegl±darka MIB
Name:		mbrowse
Version:	0.2.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://goldplated.atlcartel.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://goldplated.atlcartel.com/mbrowse.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	ucd-snmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Mbrowse is an SNMP MIB browser based on GTK and net-snmp.

%description -l pl
Mbrowse jest przegl±dark± SNMP MIB bazuj±c± na GTK i net-snmp.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
