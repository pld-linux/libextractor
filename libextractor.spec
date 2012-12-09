# TODO: zzuf (for tests)
#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_with	tests		# perform tests [some problems with rpm extractor?]
%bcond_without	gstreamer	# GStreamer plugin
%bcond_without	mp4v2		# MP4v2 plugin
%bcond_without	tidy		# HTML plugin (based on tidy library)
#
Summary:	Meta-data extraction library
Summary(pl.UTF-8):	Biblioteka do ekstrakcji metadanych
Name:		libextractor
Version:	1.0.1
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/libextractor/%{name}-%{version}.tar.gz
# Source0-md5:	593c40670fd7fc8c3ae7adc3df557f64
Patch0:		%{name}-info.patch
Patch1:		%{name}-rpm5.patch
Patch2:		%{name}-sh.patch
Patch3:		%{name}-pl.po.patch
URL:		http://gnunet.org/libextractor/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.11
BuildRequires:	bzip2-devel
BuildRequires:	exiv2-devel
BuildRequires:	gettext-devel >= 0.16.1
# libavformat libavcodec libavutil libswscale
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 2.0.0
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 0.11.93
BuildRequires:	gstreamer-plugins-base >= 0.11.93
%endif
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libarchive-devel
BuildRequires:	libgsf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 2:2
BuildRequires:	libmagic-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	libsmf-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libvorbis-devel
%{?with_mp4v2:BuildRequires:	mp4v2-devel >= 2.0.0}
BuildRequires:	pkgconfig >= 1:0.7
# rpm5 patch supports rpm5.org's rpm 4.5.x and 5.x
BuildRequires:	rpm-devel >= 4.5
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
%{?with_tidy:BuildRequires:	tidy-devel}
BuildRequires:	zlib-devel
Obsoletes:	libextractor-printable
Obsoletes:	libextractor-thumbnail-qt
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

%package thumbnail-ffmpeg
Summary:	FFmpeg Thumbnail plugin for libextractor
Summary(pl.UTF-8):	Wtyczka obsługująca miniaturki obrazów poprzez FFmpeg dla biblioteki libextractor
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description thumbnail-ffmpeg
libextractor plugin that supports thumbnails through FFmpeg.

%description thumbnail-ffmpeg -l pl.UTF-8
Wtyczka biblioteki libextractor obsługująca miniaturki obrazów poprzez
FFmpeg.

%package thumbnail-gtk
Summary:	GTK+ Thumbnail plugin for libextractor
Summary(pl.UTF-8):	Wtyczka obsługująca miniaturki obrazów poprzez GTK+ dla biblioteki libextractor
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libextractor-thumbnail < 1.0.1

%description thumbnail-gtk
libextractor plugin that supports thumbnails through GTK+.

%description thumbnail-gtk -l pl.UTF-8
Wtyczka biblioteki libextractor obsługująca miniaturki obrazów poprzez
GTK+.

%package devel
Summary:	Development files for libextractor
Summary(pl.UTF-8):	Pliki nagłówkowe libextractor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	libltdl-devel
Requires:	zlib-devel

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
%patch3 -p1

%{__rm} po/stamp-po
%{__sed} -i -e 's,tidy/\(tidy\|buffio\)\.h,\1.h,' configure.ac src/plugins/html_extractor.c

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_tests:--disable-testruns} \
	--enable-experimental \
	%{?with_static_libs:--enable-static} \
	%{!?with_gstreamer:--without-gstreamer}

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# lt_dlopen is used, but .la files are not required now
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/libextractor_*.la
%if %{with static_libs}
# useless
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/libextractor_*.a
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/extract
%attr(755,root,root) %{_libdir}/libextractor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libextractor.so.3
%attr(755,root,root) %{_libdir}/libextractor_common.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libextractor_common.so.1
%dir %{_libdir}/%{name}
# R: libarchive
%attr(755,root,root) %{_libdir}/%{name}/libextractor_archive.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_deb.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_dvi.so
# R: exiv2
%attr(755,root,root) %{_libdir}/%{name}/libextractor_exiv2.so
# R: flac
%attr(755,root,root) %{_libdir}/%{name}/libextractor_flac.so
# R: giflib
%attr(755,root,root) %{_libdir}/%{name}/libextractor_gif.so
# R: gstreamer gstreamer-plugins-base
%attr(755,root,root) %{_libdir}/%{name}/libextractor_gstreamer.so
# R: libmagic tidy
%{?with_tidy:%attr(755,root,root) %{_libdir}/%{name}/libextractor_html.so}
%attr(755,root,root) %{_libdir}/%{name}/libextractor_it.so
# R: libjepg
%attr(755,root,root) %{_libdir}/%{name}/libextractor_jpeg.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_man.so
# R: libsmf
%attr(755,root,root) %{_libdir}/%{name}/libextractor_midi.so
# R: libmagic
%attr(755,root,root) %{_libdir}/%{name}/libextractor_mime.so
# R: mp4v2
%{?with_mp4v2:%attr(755,root,root) %{_libdir}/%{name}/libextractor_mp4.so}
# R: libmpeg2
%attr(755,root,root) %{_libdir}/%{name}/libextractor_mpeg.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_nsf.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_nsfe.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_odf.so
# R: libvorbis
%attr(755,root,root) %{_libdir}/%{name}/libextractor_ogg.so
# R: libgsf
%attr(755,root,root) %{_libdir}/%{name}/libextractor_ole2.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_png.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_ps.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_riff.so
# R: rpm-lib
%attr(755,root,root) %{_libdir}/%{name}/libextractor_rpm.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_s3m.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_sid.so
# R: libtiff
%attr(755,root,root) %{_libdir}/%{name}/libextractor_tiff.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_wav.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_xm.so
%attr(755,root,root) %{_libdir}/%{name}/libextractor_zip.so
%{_mandir}/man1/extract.1*

%files thumbnail-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libextractor_thumbnailffmpeg.so

%files thumbnail-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libextractor_thumbnailgtk.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libextractor.so
%attr(755,root,root) %{_libdir}/libextractor_common.so
%{_libdir}/libextractor.la
%{_libdir}/libextractor_common.la
%{_includedir}/extractor.h
%{_pkgconfigdir}/libextractor.pc
%{_mandir}/man3/libextractor.3*
%{_infodir}/libextractor.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libextractor.a
%{_libdir}/libextractor_common.a
%endif
