#
# TODO:
#  - correct home_etc
#  - put highscores files in proper place
#
Summary:	Neverball - 3D game with rolling the ball
Summary(pl):	Neverball - gra 3D polegaj±ca na toczeniu kulki
Name:		neverball
Version:	1.2.2
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://icculus.org/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	d08817da57078b0fb8e5998fc45fc10a
Source1:	%{name}.desktop
Patch0:		%{name}-home_etc-datadir.patch
URL:		http://icculus.org/neverball/
BuildRequires:	OpenGL-devel
BuildRequires:	home-etc-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
#BuildRequires:	guile-devel >= 1.6.3
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Tilt the floor to roll the ball through the obstacle course before
time runs out.

%description -l pl
Przechylaj stó³, aby przetoczyæ kulkê przez tor z przeszkodami przed
up³ywem czasu.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -ansi `sdl-config --cflags`" \
	OGL_LIBS="-L/usr/X11R6/lib -lGLU -lGL -lm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT%{_desktopdir}

install neverball $RPM_BUILD_ROOT%{_bindir}
cp -R data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README MAPPING CHANGES
#%%attr(2755,root,games) %{_bindir}/neverball
%attr(755,root,root) %{_bindir}/neverball
%{_datadir}/%{name}
%{_desktopdir}/*
