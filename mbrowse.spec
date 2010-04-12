Summary:	SNMP MIB browser
Summary(pl.UTF-8):	Przeglądarka MIB
Name:		mbrowse
Version:	0.3.1
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.kill-9.org/mbrowse/%{name}-%{version}.tar.gz
# Source0-md5:	52c6b0a7ad9bcc7be70a35ed6b0d0d89
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-gcc.patch
URL:		http://www.kill-9.org/mbrowse/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	net-snmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mbrowse is an SNMP MIB browser based on GTK+ and net-snmp.

%description -l pl.UTF-8
Mbrowse jest przeglądarką SNMP MIB bazującą na GTK+ i net-snmp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-snmp-lib=%{_libdir}
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
