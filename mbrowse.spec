Summary:	SNMP MIB browser
Summary(pl):	Przegl±darka MIB
Name:		mbrowse
Version:	0.3.0
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.kill-9.org/mbrowse/%{name}-%{version}.tar.gz
# Source0-md5:	f32e8481115b3051973414a24e5505bc
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.kill-9.org/mbrowse/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	net-snmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mbrowse is an SNMP MIB browser based on GTK and net-snmp.

%description -l pl
Mbrowse jest przegl±dark± SNMP MIB bazuj±c± na GTK i net-snmp.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
