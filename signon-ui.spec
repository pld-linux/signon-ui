Summary:	Single Sign-on UI
Summary(pl.UTF-8):	Interfejs użytkownika do wspólnego logowania
Name:		signon-ui
Version:	0.16
Release:	1
License:	GPL v3
Group:		X11/Applications
#Source0Download: https://gitlab.com/accounts-sso/signon-ui/tags
# TODO: in the future use fake GET arg to force sane filename on df
#Source0:	https://gitlab.com/accounts-sso/signon-ui/repository/archive.tar.bz2?ref=%{version}&fake_out=/%{name}-%{version}.tar.bz2
Source0:	archive.tar.bz2%3Fref=%{version}
# Source0-md5:	f8206f24d0b8050419ba55df37b4e990
URL:		https://gitlab.com/accounts-sso/signon-ui
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Network-devel >= 5
BuildRequires:	Qt5Quick-devel >= 5
BuildRequires:	Qt5WebKit-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	libaccounts-qt5-devel
BuildRequires:	libnotify-devel
BuildRequires:	libproxy-devel
BuildRequires:	libsignon-qt5-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
BuildRequires:	signon-devel >= 8.58
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UI for the signond Single Signon service.

%description -l pl.UTF-8
Interfejs użytkownika dla usługi signond mechanizmu Single Signon
(wspólnego logowania do wielu usług).

%prep
%setup -q -n %{name}-%{version}-fbe810a5a55c949f6f3e81deb859e2ecd8acc863

%build
qmake-qt5 \
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
