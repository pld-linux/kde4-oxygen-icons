#
# Conditional build:
#
%define		_state		stable
%define		orgname		oxygen-icons

Summary:	KDE4 - Oxygen icons
Summary(pl.UTF-8):	Ikony Oxygen dla KDE4
Name:		kde4-oxygen-icons
Version:	4.6.1
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	a856835ed19dffcd4d0eeae9d7c5a3a9
Source1:	%{name}-pld_czarny.png
Source2:	kpld.tar.gz
# Source2-md5:	1111e8a60b33ad694e91d574233dde0e
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.600
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
%setup -q -n %{orgname}-%{version} -a2

%build
install -d build
cd build
%cmake \
	-DCMAKE_CXX_COMPILER_WORKS=1 \
	-DCMAKE_CXX_COMPILER="%{__cc}" \
	-DCMAKE_C_COMPILER_WORKS=1 \
	../

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -r scalable $RPM_BUILD_ROOT%{_iconsdir}/oxygen
install -d $RPM_BUILD_ROOT%{_iconsdir}/oxygen/42x42/{apps,devices,mimetypes,places}

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_iconsdir}/oxygen/48x48/apps/pld_czarny.png

# install PLD KMenu icon
install kpld/kde16x16.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/16x16/apps/kde-pld.png
install kpld/kde22x22.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/22x22/apps/kde-pld.png
install kpld/kde32x32.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/32x32/apps/kde-pld.png
install kpld/kde48x48.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/48x48/apps/kde-pld.png
install kpld/kde64x64.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/64x64/apps/kde-pld.png
install kpld/kde128x128.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/128x128/apps/kde-pld.png
install kpld/kde256x256.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/256x256/apps/kde-pld.png
install kpld/kde.svg $RPM_BUILD_ROOT%{_iconsdir}/oxygen/scalable/apps/kde-pld.svg
install kpld/kde16x16.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/16x16/places/start-here-kde.png
install kpld/kde22x22.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/22x22/places/start-here-kde.png
install kpld/kde32x32.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/32x32/places/start-here-kde.png
install kpld/kde48x48.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/48x48/places/start-here-kde.png
install kpld/kde64x64.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/64x64/places/start-here-kde.png
install kpld/kde128x128.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/128x128/places/start-here-kde.png
install kpld/kde256x256.png $RPM_BUILD_ROOT%{_iconsdir}/oxygen/256x256/places/start-here-kde.png

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde4-icons-oxygen
%defattr(644,root,root,755)
%dir %{_iconsdir}/oxygen/256x256
%dir %{_iconsdir}/oxygen/256x256/actions
%dir %{_iconsdir}/oxygen/256x256/apps
%dir %{_iconsdir}/oxygen/256x256/categories
%dir %{_iconsdir}/oxygen/256x256/devices
%dir %{_iconsdir}/oxygen/256x256/mimetypes
%dir %{_iconsdir}/oxygen/256x256/places
%dir %{_iconsdir}/oxygen/256x256/status
%dir %{_iconsdir}/oxygen/42x42
%dir %{_iconsdir}/oxygen/42x42/apps
%dir %{_iconsdir}/oxygen/42x42/devices
%dir %{_iconsdir}/oxygen/42x42/mimetypes
%dir %{_iconsdir}/oxygen/42x42/places
# digikam has it's own icon in digikam.spec
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
%{_iconsdir}/oxygen/scalable/object-rotate.svgz
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
