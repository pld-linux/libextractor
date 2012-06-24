#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Meta-data extraction library
Summary(pl):	Biblioteka do ekstrakcji metadanych
Name:		libextractor
Version:	0.5.8
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://gnunet.org/libextractor/download/%{name}-%{version}.tar.gz
# Source0-md5:	366840aabd421d61f9b5e8358274a2cc
Patch0:		%{name}-gcc4.patch
URL:		http://gnunet.org/libextractor/
BuildRequires:	ImageMagick-devel >= 1:6.0.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.5
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libvorbis-devel
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

%description -l pl
libextractor to prosta biblioteka s�u��ca do ekstrakcji metadanych.
libextractor u�ywa mechanizmu "wtyczek", dzi�ki czemu �atwo jest doda�
wsparcie dla nowych format�w plik�w.

libextractor obecnie pozwala na pozyskanie metadanych z plik�w w
formatach HTML, JPEG, Ogg, MP3, PNG, RPM, GIF, ZIP, QT, ASF, Real
Audio i Video, PostScript oraz PDF. Ponadto rozpoznaje du�o wi�cej
typ�w MIME w spos�b podobny do dobrze znanego narz�dzia "file".

Ka�da informacja pobrana z pliku nale�y do jednej z oko�o 40
kategorii (np. tytu�, autor, opis, typ MIME).

Ta paczka zawiera te� narz�dzie "extract", kt�re pozwala skorzysta� z
us�ug libextractor bezpo�rednio z linii polece�. "extract" mo�e by�
u�ywane w podobny spos�b, co "file". "file" zna wi�cej typ�w danych,
"extract" natomiast dostarcza bardziej precyzyjnych i szczeg�owych
informacji na temat obs�ugiwanych format�w (HTML, JPEG, Ogg, MP3, PNG,
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

%package thumbnail
Summary:	Thumbnail plugin for libextractor
Summary(pl):	Wtyczka obs�uguj�ce miniaturki obraz�w dla biblioteki libextractor
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.6.0

%description thumbnail
libextractor plugin that supports thumbnails.

%description thumbnail -l pl
Wtyczka biblioteki libextractor obs�uguj�ca miniaturki obraz�w.

%package devel
Summary:	Development files for libextractor
Summary(pl):	Pliki nag��wkowe libextractor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libltdl-devel

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
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize} --ltdl
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

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
%{_libdir}/%{name}/libextractor_thumbnail.la

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
