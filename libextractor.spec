Summary:	Meta-data extraction library
Summary(pl):	Biblioteka do ekstrakcji metadanych
Name:		libextractor
Version:	0.3.3
Release:	1
License:	GPL
Group:		Libraries
# strange, .tar.gz is ~500kB smaller than .tar.bz2
Source0:	http://www.ovmj.org/libextractor/download/%{name}-%{version}.tar.gz
# Source0-md5:	0e70401b3a1574bf16caf17a4af78398
URL:		http://www.ovmj.org/libextractor/
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
libextractor to prosta biblioteka s�u��ca do ekstrakcji metadanych.
libextractor u�ywa mechanizmu "wtyczek", dzi�ki czemu �atwo jest doda�
wsparcie dla nowych format�w plik�w.

libextractor obecnie pozwala na pozyskanie metadanych z plik�w w
formatach HTML, JPEG, OGG, MP3, PNG, RPM, GIF, ZIP, QT, ASF, Real
Audio i Video, PostScript oraz PDF. Ponadto rozpoznaje du�o wi�cej
typ�w MIME w spos�b podobny do dobrze znanego narz�dzia "file".

Ka�da informacja pobrana z pliku nale�y do jednej z oko�o 40
kategorii (np. tytu�, autor, opis, typ MIME).

Ta paczka zawiera te� narzedzie "extract", kt�re pozwala skorzysta� z
us�ug libextractor bezpo�rednio z linii polece�. "extract" mo�e by�
u�ywane w podobny spos�b, co "file". "file" zna wi�cej typ�w danych,
"extract" natomiast dostarcza bardziej precyzyjnych i szczeg�owych
informacji na temat obs�ugiwanych format�w (HTML, JPEG, OGG, MP3, PNG,
GIF, RPM, RA, RM, PS, PDF, ZIP, QT, ASF).

%package printable
Summary:	Printable text support plugins for libextractor
Summary(pl):	Wtyczki obs�uguj�ce tekst dla biblioteki libextractor
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description printable
libextractor plugins that support printable text in few languages.

%description printable -l pl
Wtyczki biblioteki libextractor obs�uguj�ce tekst w kilku j�zykach.

%package devel
Summary:	Development files for libextractor
Summary(pl):	Pliki nag��wkowe libextractor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains files to develop with libextractor, that is
either to create plugins or to compile applications with libextractor.

%description devel -l pl
Piki nag��wkowe wymagane do tworzenia aplikacji i wtyczek
korzystaj�cych z libextractor.

%package static
Summary:	Static libextractor libraries
Summary(pl):	Statyczne biblioteki libextractor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libraries of libextractor.

%description static -l pl
Statyczna wersja bibliotek libextractor.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub .
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless
rm -f $RPM_BUILD_ROOT%{_libdir}/libextractor_[!u]*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/extract
%attr(755,root,root) %{_libdir}/libextractor.so.*.*.*
# plugins are lt_dlopened without extension, so *.la are needed
%attr(755,root,root) %{_libdir}/libextractor_asf.so
%attr(755,root,root) %{_libdir}/libextractor_elf.so
%attr(755,root,root) %{_libdir}/libextractor_filename.so
%attr(755,root,root) %{_libdir}/libextractor_gif.so
%attr(755,root,root) %{_libdir}/libextractor_html.so
%attr(755,root,root) %{_libdir}/libextractor_jpeg.so
%attr(755,root,root) %{_libdir}/libextractor_lower.so
%attr(755,root,root) %{_libdir}/libextractor_mime.so
%attr(755,root,root) %{_libdir}/libextractor_mp3.so
%attr(755,root,root) %{_libdir}/libextractor_mpeg.so
%attr(755,root,root) %{_libdir}/libextractor_ogg.so
%attr(755,root,root) %{_libdir}/libextractor_pdf.so
%attr(755,root,root) %{_libdir}/libextractor_png.so
%attr(755,root,root) %{_libdir}/libextractor_ps.so
%attr(755,root,root) %{_libdir}/libextractor_qt.so
%attr(755,root,root) %{_libdir}/libextractor_real.so
%attr(755,root,root) %{_libdir}/libextractor_riff.so
%attr(755,root,root) %{_libdir}/libextractor_rpm.so
%attr(755,root,root) %{_libdir}/libextractor_split.so
%attr(755,root,root) %{_libdir}/libextractor_tiff.so
%attr(755,root,root) %{_libdir}/libextractor_wav.so
%attr(755,root,root) %{_libdir}/libextractor_zip.so
%{_libdir}/libextractor_asf.la
%{_libdir}/libextractor_elf.la
%{_libdir}/libextractor_filename.la
%{_libdir}/libextractor_gif.la
%{_libdir}/libextractor_html.la
%{_libdir}/libextractor_jpeg.la
%{_libdir}/libextractor_lower.la
%{_libdir}/libextractor_mime.la
%{_libdir}/libextractor_mp3.la
%{_libdir}/libextractor_mpeg.la
%{_libdir}/libextractor_ogg.la
%{_libdir}/libextractor_pdf.la
%{_libdir}/libextractor_png.la
%{_libdir}/libextractor_ps.la
%{_libdir}/libextractor_qt.la
%{_libdir}/libextractor_real.la
%{_libdir}/libextractor_riff.la
%{_libdir}/libextractor_rpm.la
%{_libdir}/libextractor_split.la
%{_libdir}/libextractor_tiff.la
%{_libdir}/libextractor_wav.la
%{_libdir}/libextractor_zip.la
%{_mandir}/man1/*

%files printable
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libextractor_printable_*.so
%{_libdir}/libextractor_printable_*.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libextractor.so
%{_libdir}/libextractor.la
%{_includedir}/extractor.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libextractor.a
