Summary:	SNMP MIB browser
Summary(pl.UTF-8):	Przeglądarka MIB
Name:		mbrowse
Version:	0.4.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/mbrowse/%{name}-%{version}.tar.gz
# Source0-md5:	9857a88d2e6246384587350a647e605d
Patch0:		%{name}-no-common.patch
URL:		https://sourceforge.net/projects/mbrowse/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	net-snmp-devel >= 4.2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mbrowse is an SNMP MIB browser based on GTK+ and net-snmp.

%description -l pl.UTF-8
Mbrowse jest przeglądarką SNMP MIB bazującą na GTK+ i net-snmp.

%prep
%setup -q
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/mbrowse
