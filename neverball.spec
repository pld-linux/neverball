#
# TODO: check BRs
#       add .desktop
#
Summary:	Neverball - 3D game with rolling the ball
Summary(pl):	Neverball - gra 3D polegaj±ca na toczeniu kulki
Name:		neverball
Version:	0805b
Release:	0.3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://aoeu.snth.net/neverball/%{name}-%{version}.zip
# Source0-md5:	4638fbdeb8b672b974ab57cc84b54bd4
Patch0:		%{name}-datadir.patch
URL:		http://aoeu.snth.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	guile-devel >= 1.6.3
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_prefix}/games
%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Tilt the floor to roll the ball through the obstacle course before
time runs out.

%description -l pl
Przechylaj stó³, aby przetoczyæ kulkê przez tor z przeszkodami przed
up³ywem czasu.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -ansi `sdl-config --cflags`" \
	X11_LIBS="-L/usr/X11R6/lib -lGLU -lGL -lm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name}}

install neverball $RPM_BUILD_ROOT%{_bindir}
cp -R data/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}

rm -f $RPM_BUILD_ROOT%{_datadir}/games/%{name}/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt MAPPING.txt
%attr(2755,root,games) %{_bindir}/neverball
%{_datadir}/games/%{name}
