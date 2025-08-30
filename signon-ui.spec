#
# Conditional build:
%bcond_with	qt5	# build with qt5-based signon

%if %{with qt5}
%define	qtmajor		5
%define	qt_ver		5.0
%define	signon_ver	8.58
%else
%define	qtmajor		6
%define	qt_ver		6.0
%define	signon_ver	8.62
%endif
Summary:	Single Sign-on UI
Summary(pl.UTF-8):	Interfejs użytkownika do wspólnego logowania
Name:		signon-ui
Version:	0.17
%define	gitref	%{version}+15.10.20150810-0ubuntu1
Release:	1
License:	GPL v3
Group:		X11/Applications
#Source0Download: https://gitlab.com/accounts-sso/signon-ui/tags
Source0:	https://gitlab.com/accounts-sso/signon-ui/-/archive/%{gitref}/%{name}-%{gitref}.tar.bz2
# Source0-md5:	5ecb7fabe073dc3132fbda9eb8aab431
Patch0:		%{name}-git.patch
URL:		https://gitlab.com/accounts-sso/signon-ui
BuildRequires:	Qt%{qtmajor}Core-devel >= %{qt_ver}
BuildRequires:	Qt%{qtmajor}DBus-devel >= %{qt_ver}
BuildRequires:	Qt%{qtmajor}Gui-devel >= %{qt_ver}
BuildRequires:	Qt%{qtmajor}Network-devel >= %{qt_ver}
BuildRequires:	Qt%{qtmajor}Quick-devel >= %{qt_ver}
BuildRequires:	Qt%{qtmajor}WebEngine-devel >= %{qt_ver}
BuildRequires:	Qt%{qtmajor}Widgets-devel >= %{qt_ver}
BuildRequires:	libaccounts-qt%{qtmajor}-devel
BuildRequires:	libnotify-devel
BuildRequires:	libproxy-devel
BuildRequires:	libsignon-qt%{qtmajor}-devel
BuildRequires:	pkgconfig
BuildRequires:	qt%{qtmajor}-build >= %{qt_ver}
BuildRequires:	qt%{qtmajor}-qmake >= %{qt_ver}
BuildRequires:	signon-devel >= %{signon_ver}
BuildRequires:	xorg-lib-libX11-devel
%if %{without qt5}
# WebEngine required
ExclusiveArch:	%{x8664} aarch64
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UI for the signond Single Signon service.

%description -l pl.UTF-8
Interfejs użytkownika dla usługi signond mechanizmu Single Signon
(wspólnego logowania do wielu usług).

%prep
%setup -q -n %{name}-%{gitref}
%patch -P0 -p1

%build
qmake-qt%{qtmajor} \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{signon-ui-unittest,tst_inactivity_timer}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/signon-ui
%{_datadir}/dbus-1/services/com.canonical.indicators.webcredentials.service
%{_datadir}/dbus-1/services/com.nokia.singlesignonui.service
