Summary:	Meta-data extraction library
Summary(pl):	Biblioteka do ekstrakcji metadanych
Name:		libextractor
Version:	0.2.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.ovmj.org/%{name}/download/%{name}-%{version}.tar.bz2
# Source0-md5:	9d059e4b02cac89661816f19458d0bf5
URL:		http://www.ovmj.org/libextractor/
BuildRequires:	aspell-devel
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libextractor is a simple library for meta-data extraction.
libextractor uses a plugin-mechanism that makes it easy to add support
for more file formats, allowing anybody to add new extractors quickly.

libextractor currently features meta-data extractors for HTML, JPEG,
OGG, MP3, PNG, RPM, GIF, ZIP, QT, ASF, Real Audio and Video,
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
libextractor to prosta biblioteka s³u¿±ca do ekstrakcji metadanych.
libextractor u¿ywa mechanizmu "wtyczek", dziêki czemu ³atwo jest dodaæ
wsparcie dla nowych formatów plików.

libextractor obecnie pozwala na pozyskanie metadanych z plików w
formatach HTML, JPEG, OGG, MP3, PNG, RPM, GIF, ZIP, QT, ASF, Real
Audio i Video, PostScript oraz PDF. Ponadto rozpoznaje du¿o wiêcej
typów MIME w sposób podobny do dobrze znanego narzêdzia "file".

Ka¿da informacja pobrana z pliku nale¿y do jednej z oko³o 40
kategorii (np. tytu³, autor, opis, typ MIME).

Ta paczka zawiera te¿ narzedzie "extract", które pozwala skorzystaæ z
us³ug libextractor bezpo¶rednio z linii poleceñ. "extract" mo¿e byæ
u¿ywane w podobny sposób, co "file". "file" zna wiêcej typów danych,
"extract" natomiast dostarcza bardziej precyzyjnych i szczegó³owych
informacji na temat obs³ugiwanych formatów (HTML, JPEG, OGG, MP3, PNG,
GIF, RPM, RA, RM, PS, PDF, ZIP, QT, ASF).

%package devel
Summary:	Development files for libextractor
Summary(pl):	Pliki nag³ówkowe libextractor
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains files to develop with libextractor, that is
either to create plugins or to compile applications with libextractor.

%description devel -l pl
Piki nag³ówkowe wymagane do tworzenia aplikacji i wtyczek
korzystaj±cych z libextractor.

%package static
Summary:	Static libextractor libraries
Summary(pl):	Statyczne biblioteki libextractor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries of libextractor.

%description static -l pl
Statyczna wersja bibliotek libextractor.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless
rm -f $RPM_BUILD_ROOT%{_libdir}/libextractor_*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/extract
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
# libltld requires at least one of .la and .so for plugins
# let's leave *.la, because they are checked first
%{_libdir}/libextractor_*.la
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libextractor.so
%{_libdir}/libextractor.la
%{_includedir}/extractor.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libextractor.a
