Summary:	Meta-data extraction library
Summary(pl):	Biblioteka do ekstrakcji meta-danych
Name:		libextractor
Version:	0.2.4
Release:	1
License:	GPL
Group:		Libraries
Requires:	glibc >= 2.2.4
Requires:	libvorbis
Requires:	libogg
BuildRequires:	libvorbis-devel
BuildRequires:	libogg-devel
URL:		http://www.ovmj.org/%{name}/
Source0:	http://www.ovmj.org/%{name}/download/%{name}-%{version}.tar.bz2
# Source0-md5:	9d059e4b02cac89661816f19458d0bf5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%package devel
Summary:	Development files for libextractor
Summary(pl):	Pliki nag³ówkowe libextractor
Group:		Development/Libraries
Requires:	%{name} = %{version}

%package static
Summary:	Static libextractor libraries
Summary(pl):	Statyczne biblioteki libextractor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}


%description
libextractor is a simple library for meta-data extraction.
libextractor uses a plugin-mechanism that makes it easy to add support
for more file formats, allowing anybody to add new extractors quickly.

libextractor currently features meta-data extractors for HTML, JPEG,
OGG, MP3, PNG, RPM, GIF, ZIP, QT, ASF, Real audio and video,
PostScript and PDF documents. It also detects many more MIME-types in
a fashion similar to the well-known "file" tool.

Each item of meta-data that is extracted from a file is categorized
into one of currently about 40 meta-data categories (e.g. title,
author, description or MIME-type).

This libextractor package also contains a little binary tool "extract"
that can be used to invoke libextractor from the command line.
"extract" can be used similar to "file", but while "file" currently
supports a wider range of file types, "extract" should be able to
provide more precise and more detailed information for the supported
types of documents (HTML, JPEG, OGG, MP3, PNG, GIF, RPM, RA, RM, PS,
PDF, ZIP, QT, ASF).

%description -l pl
libextractor to prosta biblioteka s³u¿±ca do ekstrakcji meta-danych.
libextractor u¿ywa mechanizmu "wtyczek", dziêki czemu ³atwo jest dodaæ
wsparcie dla nowych formatów plików.

libextractor obecnie pozwala na pozyskanie meta-danych z plików w
formatach HTML, JPEG, OGG, MP3, PNG, RPM, GIF, ZIP, QT, ASF, Real
audio i video, PostScript oraz PDF. Ponadto rozpoznaje du¿o wiêcej
typów MIME, podobnie jak dobrze znane narzêdzie "file".

Ka¿da informacja pobrana z pliku nale¿y do jednej z ponad 400
kategorii (np. tytu³, autor, opis, typ MIME).

Ta paczka zawiera te¿ narzedzie "extract", które pozwala skorzystaæ z
us³ug libextractor bezpo¶rednio z linii komend. "extract" mo¿e byæ
u¿ywane w podobny sposób, co "file". "file" zna wiêcej typów danych,
"extract" natomiast dostarcza bardziej precyzyjnych i szczegó³owych
informacji na temat obs³ugiwanych formatów (HTML, JPEG, OGG, MP3, PNG,
GIF, RPM, RA, RM, PS, PDF, ZIP, QT, ASF).

%description devel
This package contains files to develop with libextractor, that is
either to create plugins or to compile applications with libextractor.

%description devel -l pl
Piki nag³ówkowe wymagane do tworzenia aplikacji i wtyczek
korzystaj±cych z libextractor.

%description static
This package contains static libraries of libextractor.

%description static -l pl
Statyczna wersja bibliotek libextractor.

%prep
%setup -q

%build
%configure
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libextractor.so
%attr(755,root,root) %{_libdir}/libextractor.so.*
%attr(755,root,root) %{_libdir}/libextractor_*.so
%attr(755,root,root) %{_libdir}/libextractor_*.so.*
%attr(755,root,root) %{_bindir}/extract
%doc %{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_includedir}/extractor.h
%doc %{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
