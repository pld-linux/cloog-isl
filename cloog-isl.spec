Summary:	The Chunky Loop Generator
Summary(pl.UTF-8):	Chunky Loop Generator - generator pętli cząstkowych
Name:		cloog-isl
Version:	0.17.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Tools
Source0:	http://www.bastoul.net/cloog/pages/download/cloog-%{version}.tar.gz
# Source0-md5:	0aa3302c81f65ca62c114e5264f8a802
URL:		http://www.cloog.org/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
BuildRequires:	gmp-devel >= 5.0.2
BuildRequires:	gmp-c++-devel >= 5.0.2
BuildRequires:	libtool
BuildRequires:	isl-devel >= 0.08
Requires:	%{name}-libs = %{version}-%{release}
Provides:	cloog = %{version}
Obsoletes:	cloog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLooG is a software which generates loops for scanning Z-polyhedra.
That is, CLooG finds the code or pseudo-code where each integral point
of one or more parametrized polyhedron or parametrized polyhedra union
is reached. CLooG is designed to avoid control overhead and to produce
a very efficient code.

This version is based on isl.

%description -l pl.UTF-8
CLooG to oprogramowanie generujące pętle do przeszukiwania
Z-wielościanów (Z-polyhedra). Oznacza to, że CLooG znajduje kod lub
pseudokod osiągający każdy punkt całkowity jednego lub większej liczby
sparametryzowanych wielościanów lub sum sparametryzowanych
wielościanów. CLooG jest zaprojektowany z myślą o zapobieganiu
narzutowi na sterowaniu oraz generowaniu bardzo wydajnego kodu.

Ta wersja jest oparta na bibliotece isl.

%package libs
Summary:	Chunky Loop Generator shared library - isl based version
Summary(pl.UTF-8):	Biblioteka współdzielona Chunky Loop Generatora - wersja oparta na isl
Group:		Libraries
Requires:	isl >= 0.08

%description libs
Chunky Loop Generator shared library - isl based version.

%description libs -l pl.UTF-8
Biblioteka współdzielona Chunky Loop Generatora - wersja oparta na
isl.

%package devel
Summary:	Header files for the isl based version of Chunky Loop Generator
Summary(pl.UTF-8):	Pliki nagłówkowe opartej na isl wersji Chunky Loop Generatora
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gmp-devel >= 5.0.2
Requires:	gmp-c++-devel >= 5.0.2
Requires:	isl-devel >= 0.08
Provides:	cloog-devel = %{version}

%description devel
The header files for Chunky Loop Generator library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Chunky Loop Generatora.

%package static
Summary:	Static library of isl based version of Chunky Loop Generator
Summary(pl.UTF-8):	Statyczna biblioteka opartej na isl wersji Chunky Loop Generatora
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library of isl based version of Chunky Loop Generator.

%description static -l pl.UTF-8
Statyczna biblioteka opartej na isl wersji Chunky Loop Generatora.

%prep
%setup -q -n cloog-%{version}

%build
%configure \
	--disable-silent-rules \
	--with-isl=system

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cloog

%files libs
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libcloog-isl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcloog-isl.so.3

%files devel
%defattr(644,root,root,755)
%doc doc/cloog.pdf
%attr(755,root,root) %{_libdir}/libcloog-isl.so
%{_libdir}/libcloog-isl.la
%dir %{_includedir}/cloog
%{_includedir}/cloog/*.h
%{_includedir}/cloog/isl
%{_includedir}/cloog/matrix
%{_pkgconfigdir}/cloog-isl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcloog-isl.a