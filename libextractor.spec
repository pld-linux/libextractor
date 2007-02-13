#
# Conditional build:
%bcond_without	qt		# don't build Qt-based thumbnail plugin
%bcond_without	static_libs	# don't build static library
#
Summary:	Meta-data extraction library
Summary(pl.UTF-8):	Biblioteka do ekstrakcji metadanych
Name:		libextractor
Version:	0.5.16
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://gnunet.org/libextractor/download/%{name}-%{version}.tar.gz
# Source0-md5:	537c79b827406741a2f9c62ab77cc513
Patch0:		%{name}-64bit.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-qt.patch
URL:		http://gnunet.org/libextractor/
%if %{with qt}
BuildRequires:	QtGui-devel >= 4.0
BuildRequires:	QtSvg-devel >= 4.0
%endif
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel >= 0.14.5
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libgsf-devel
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libvorbis-devel
BuildRequires:	mpeg2dec-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libextractor is a simple library for meta-data extraction.
libextractor uses a plugin-mechanism that makes it easy to add support
for more file formats, allowing anybody to add new extractors quickly.

libextractor currently features meta-data extractors for HTML, JPEG,
Ogg, MP3, PNG, RPM, GIF, ZIP, QT, ASF, Real Audio and Video,
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
types of documents (HTML, JPEG, Ogg, MP3, PNG, GIF, RPM, RA, RM, PS,
PDF, ZIP, QT, ASF).

%description -l pl.UTF-8
libextractor to prosta biblioteka służąca do ekstrakcji metadanych.
libextractor używa mechanizmu "wtyczek", dzięki czemu łatwo jest dodać
wsparcie dla nowych formatów plików.

libextractor obecnie pozwala na pozyskanie metadanych z plików w
formatach HTML, JPEG, Ogg, MP3, PNG, RPM, GIF, ZIP, QT, ASF, Real
Audio i Video, PostScript oraz PDF. Ponadto rozpoznaje dużo więcej
typów MIME w sposób podobny do dobrze znanego narzędzia "file".

Każda informacja pobrana z pliku należy do jednej z około 40
kategorii (np. tytuł, autor, opis, typ MIME).

Ta paczka zawiera też narzędzie "extract", które pozwala skorzystać z
usług libextractor bezpośrednio z linii poleceń. "extract" może być
używane w podobny sposób, co "file". "file" zna więcej typów danych,
"extract" natomiast dostarcza bardziej precyzyjnych i szczegółowych
informacji na temat obsługiwanych formatów (HTML, JPEG, Ogg, MP3, PNG,
GIF, RPM, RA, RM, PS, PDF, ZIP, QT, ASF).

%package printable
Summary:	Printable text support plugins for libextractor
Summary(pl.UTF-8):	Wtyczki obsługujące tekst dla biblioteki libextractor
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description printable
libextractor plugins that support printable text in few languages.

%description printable -l pl.UTF-8
Wtyczki biblioteki libextractor obsługujące tekst w kilku językach.

%package thumbnail
Summary:	GTK+ Thumbnail plugin for libextractor
Summary(pl.UTF-8):	Wtyczka obsługująca miniaturki obrazów poprzez GTK+ dla biblioteki libextractor
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.6.0

%description thumbnail
libextractor plugin that supports thumbnails through GTK+.

%description thumbnail -l pl.UTF-8
Wtyczka biblioteki libextractor obsługująca miniaturki obrazów poprzez
GTK+.

%package thumbnail-qt
Summary:	Qt Thumbnail plugin for libextractor
Summary(pl.UTF-8):	Wtyczka obsługujące miniaturki obrazów poprzez Qt dla biblioteki libextractor
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description thumbnail-qt
libextractor plugin that supports thumbnails through Qt.

%description thumbnail-qt -l pl.UTF-8
Wtyczka biblioteki libextractor obsługująca miniaturki obrazów poprzez
Qt.

%package devel
Summary:	Development files for libextractor
Summary(pl.UTF-8):	Pliki nagłówkowe libextractor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	libgsf-devel
Requires:	libltdl-devel

%description devel
This package contains files to develop with libextractor, that is
either to create plugins or to compile applications with libextractor.

%description devel -l pl.UTF-8
Piki nagłówkowe wymagane do tworzenia aplikacji i wtyczek
korzystających z libextractor.

%package static
Summary:	Static libextractor libraries
Summary(pl.UTF-8):	Statyczne biblioteki libextractor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libraries of libextractor.

%description static -l pl.UTF-8
Statyczna wersja bibliotek libextractor.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__libtoolize} --ltdl
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%{?with_qt:CPPFLAGS="-I/usr/include/qt4 -I/usr/include/qt4/Qt"}
%configure \
	%{?with_static_libs:--enable-static} \
	%{?with_qt:--with-qt}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/libextractor_*.a

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/extract
%attr(755,root,root) %{_libdir}/libextractor.so.*.*.*
# plugins are lt_dlopened without extension, so *.la are needed
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libextractor_asf.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_deb.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_dvi.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_elf.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_exiv2.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_filename.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_gif.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_hash_md5.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_hash_rmd160.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_hash_sha1.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_html.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_id3v2.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_id3v23.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_id3v24.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_jpeg.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_lower.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_man.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_mime.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_mp3.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_mpeg.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_nsf.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_ogg.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_ole2.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_oo.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_pdf.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_png.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_ps.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_qt.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_real.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_riff.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_rpm.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_split.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_tar.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_tiff.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_translit.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_wav.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_zip.so
%{_libdir}/%{name}/libextractor_asf.la
%{_libdir}/%{name}/libextractor_deb.la
%{_libdir}/%{name}/libextractor_dvi.la
%{_libdir}/%{name}/libextractor_elf.la
%{_libdir}/%{name}/libextractor_exiv2.la
%{_libdir}/%{name}/libextractor_filename.la
%{_libdir}/%{name}/libextractor_gif.la
%{_libdir}/%{name}/libextractor_hash_md5.la
%{_libdir}/%{name}/libextractor_hash_rmd160.la
%{_libdir}/%{name}/libextractor_hash_sha1.la
%{_libdir}/%{name}/libextractor_html.la
%{_libdir}/%{name}/libextractor_id3v2.la
%{_libdir}/%{name}/libextractor_id3v23.la
%{_libdir}/%{name}/libextractor_id3v24.la
%{_libdir}/%{name}/libextractor_jpeg.la
%{_libdir}/%{name}/libextractor_lower.la
%{_libdir}/%{name}/libextractor_man.la
%{_libdir}/%{name}/libextractor_mime.la
%{_libdir}/%{name}/libextractor_mp3.la
%{_libdir}/%{name}/libextractor_mpeg.la
%{_libdir}/%{name}/libextractor_nsf.la
%{_libdir}/%{name}/libextractor_ogg.la
%{_libdir}/%{name}/libextractor_ole2.la
%{_libdir}/%{name}/libextractor_oo.la
%{_libdir}/%{name}/libextractor_pdf.la
%{_libdir}/%{name}/libextractor_png.la
%{_libdir}/%{name}/libextractor_ps.la
%{_libdir}/%{name}/libextractor_qt.la
%{_libdir}/%{name}/libextractor_real.la
%{_libdir}/%{name}/libextractor_riff.la
%{_libdir}/%{name}/libextractor_rpm.la
%{_libdir}/%{name}/libextractor_split.la
%{_libdir}/%{name}/libextractor_tar.la
%{_libdir}/%{name}/libextractor_tiff.la
%{_libdir}/%{name}/libextractor_translit.la
%{_libdir}/%{name}/libextractor_wav.la
%{_libdir}/%{name}/libextractor_zip.la
%{_mandir}/man1/*

%files printable
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libextractor_printable_*.so
%{_libdir}/%{name}/libextractor_printable_*.la

%files thumbnail
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libextractor_thumbnail.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_thumbnailgtk.so
%{_libdir}/%{name}/libextractor_thumbnailgtk.la

%files thumbnail-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libextractor_thumbnailqt.so
%{_libdir}/%{name}/libextractor_thumbnailqt.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libextractor.so
%{_libdir}/libextractor.la
%{_includedir}/extractor.h
%{_mandir}/man3/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libextractor.a
%endif
