#
# TODO:
#  - correct home_etc
#  - put highscores files in proper place
#  - fix problem with ttf font
#
Summary:	Neverball - 3D game with rolling the ball
Summary(pl.UTF-8):	Neverball - gra 3D polegająca na toczeniu kulki
Name:		neverball
Version:	1.5.3
Release:	0.1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://icculus.org/neverball/%{name}-%{version}.tar.gz
# Source0-md5:	e60039ba17a68f9b22b0d4d3c010b9df
Source1:	%{name}.desktop
Source2:	neverputt.desktop
Source3:	%{name}.png
Patch0:		%{name}-datadir.patch
URL:		http://icculus.org/neverball/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
#BuildRequires:	guile-devel >= 1.6.3
#BuildRequires:	home-etc-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Tilt the floor to roll the ball through the obstacle course before
time runs out. Neverball is part puzzle game, part action game, and
entirely a test of skill.

Also found here is Neverputt, a hot-seat multiplayer miniature golf
game using the physics and graphics of Neverball.

%description -l pl.UTF-8
Gra polega na przechylaniu stołu, aby przetoczyć kulkę przez tor z
przeszkodami przed upływem czasu. Neverball jest częściowo grą
logiczną, częściowo zręcznościową i w całości jest
sprawdzianem umiejętności.

Załączony jest również Neverputt, miniaturowy golf dla wielu
graczy siedzących przy jednym komputerze używający fizyki i grafiki
Neverballa.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -ansi `sdl-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_desktopdir}

install never{ball,putt} $RPM_BUILD_ROOT%{_bindir}
cp -R data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
