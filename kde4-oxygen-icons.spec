#
# Conditional build:
#
%define		state		unstable
%define		orgname		oxygen-icons
%define		svn		979380

Summary:	KDE4 - Oxygen icons
Summary(pl.UTF-8):	Ikony Oxygen dla KDE4
Name:		kde4-oxygen-icons
Version:	4.2.91
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{state}/%{version}/src/%{orgname}-%{version}svn%{svn}.tar.bz2
# Source0-md5:	fcb5d4026c455cc94c1c818e480dc30f
#Source0:	ftp://ftp.kde.org/pub/kde/%{state}/%{version}/src/%{orgname}-%{version}.tar.bz2
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	rpmbuild(macros) >= 1.293
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE4 - Oxygen Icons.

%description -l pl.UTF-8
Ikony Oxygen dla KDE4.

%package -n kde4-icons-oxygen
Summary:	KDE icons - oxygen
Summary(pl.UTF-8):	Motyw ikon do KDE - oxygen
Group:		Themes
Provides:	kde4-icons
Obsoletes:	kde-icons-oxygen

%description -n kde4-icons-oxygen
KDE icons - oxygen.

%description -n kde4-icons-oxygen -l pl.UTF-8
Motyw ikon do KDE - oxygen.

%package -n kde4-icons-oxygen-svg
Summary:	KDE SVG icons - oxygen
Summary(pl.UTF-8):	Motyw ikon SVG do KDE - oxygen
Group:		Themes
Provides:	kde4-icons

%description -n kde4-icons-oxygen-svg
KDE icons - oxygen. This package contains SVG icons.

%description -n kde4-icons-oxygen-svg -l pl.UTF-8
Motyw ikon do KDE - oxygen. Ten pakiet zawiera ikony SVG.

%prep
%setup -q -n %{orgname}-%{version}svn%{svn}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -r scalable $RPM_BUILD_ROOT%{_iconsdir}/oxygen/

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde4-icons-oxygen
%defattr(644,root,root,755)
# digikam has it's own icon in digikam.spec
%dir %{_iconsdir}/oxygen/256x256
%dir %{_iconsdir}/oxygen/256x256/apps
%dir %{_iconsdir}/oxygen/256x256/devices
%dir %{_iconsdir}/oxygen/256x256/mimetypes
%dir %{_iconsdir}/oxygen/256x256/places
%dir %{_iconsdir}/oxygen/256x256/status
%exclude %{_iconsdir}/oxygen/*x*/apps/digikam.*
%exclude %{_iconsdir}/oxygen/*x*/apps/showfoto.*
%{_iconsdir}/oxygen/*x*/actions/*
%{_iconsdir}/oxygen/*x*/apps/*
%{_iconsdir}/oxygen/*x*/categories/*
%{_iconsdir}/oxygen/*x*/devices/*
%{_iconsdir}/oxygen/*x*/mimetypes/*
%{_iconsdir}/oxygen/*x*/places/*
%{_iconsdir}/oxygen/*x*/status/*
%{_iconsdir}/oxygen/*x*/animations/*
%{_iconsdir}/oxygen/*x*/emblems/*
%{_iconsdir}/oxygen/*x*/emotes/*
%{_iconsdir}/oxygen/index.theme

%files -n kde4-icons-oxygen-svg
%defattr(644,root,root,755)
%dir %{_iconsdir}/oxygen/scalable
# digikam has it's own icon in digikam.spec
%exclude %{_iconsdir}/oxygen/scalable/apps/digikam.*
%{_iconsdir}/oxygen/scalable/text-formatting.svg
%{_iconsdir}/oxygen/scalable/actions
%{_iconsdir}/oxygen/scalable/apps
%{_iconsdir}/oxygen/scalable/categories
%{_iconsdir}/oxygen/scalable/devices
%{_iconsdir}/oxygen/scalable/emblems
%{_iconsdir}/oxygen/scalable/emotes
%{_iconsdir}/oxygen/scalable/mimetypes
%{_iconsdir}/oxygen/scalable/places
%{_iconsdir}/oxygen/scalable/status
