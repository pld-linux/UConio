Summary:	Borland CONIO library port for Unix
Summary(pl):	Port biblioteki Borland CONIO dla Unixa
Name:		UConio
Version:	1.0.9
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://crazylovetrain.hypermart.net/files/uconio/%{name}-%{version}-PR.tar.gz
Patch0:		%{name}-make.patch
URL:		http://crazylovetrain.hypermart.net/projects.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UConio is a Unix port of the Borland Console Input/Output Library
(CONIO) for DOS, and includes some new features of its own.

%description -l pl
UConio jest Uniksowym portem biblioteki Borland Console Input/Output
(CONIO) dla DOS-a, zawiera te� troch� dodanych, nowych funkcji.

%package devel
Summary:	Header files and development documentation for %{name}
Summary(pl):	Pliki nag��wkowe i dokumentacja do %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for %{name}.

%description -l pl devel
Pliki nag��wkowe i dokumentacja do %{name}.

%prep
%setup -q -n %{name}-%{version}-PR
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3,%{_includedir}}

bzip2 -d man/*.bz2

install	 bin/libuconio.so.*	$RPM_BUILD_ROOT%{_libdir}
(cd $RPM_BUILD_ROOT%{_libdir}; ln -s libuconio.so.* libuconio.so)
install include/*.h		$RPM_BUILD_ROOT%{_includedir}
install	man/*.3			$RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/{AUTHOR,BUGS,ChangeLog,HELPERS,README}
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc tutorial/txt/*.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*
%{_includedir}/*.h
