Summary:	Borland CONIO library port for Unix
Summary(pl):	Port biblioteki Borland CONIO dla Uniksa
Name:		UConio
Version:	1.0.9
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://crazylovetrain.hypermart.net/files/uconio/%{name}-%{version}-PR.tar.gz
# Source0-md5:	08a6caac1daa6ab4cd27804ce99a79c5
Patch0:		%{name}-make.patch
Patch1:		%{name}-va_end.patch
URL:		http://crazylovetrain.hypermart.net/projects.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch ppc
%define		optflags	-O0
%endif

%description
UConio is a Unix port of the Borland Console Input/Output Library
(CONIO) for DOS, and includes some new features of its own.

%description -l pl
UConio jest uniksowym portem biblioteki Borland Console Input/Output
(CONIO) dla DOS-a, zawiera te¿ trochê dodanych, nowych funkcji.

%package devel
Summary:	Header files and development documentation for UConio
Summary(pl):	Pliki nag³ówkowe i dokumentacja do UConio
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for UConio.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do UConio.

%prep
%setup -q -n %{name}-%{version}-PR
%patch0 -p1
%patch1 -p0

bzip2 -d man/*.bz2

%build
%{__make} "CFLAGS=%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3,%{_includedir}}

install	bin/libuconio.so.* $RPM_BUILD_ROOT%{_libdir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}
install	man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3

(cd $RPM_BUILD_ROOT%{_libdir}; ln -s libuconio.so.* libuconio.so)

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
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
