#
# TODO: summary, description (check), cleanups, check BRs
#       add .desktop
#
Summary:	Neverball is 3d game with rolling the ball.
Summary(pl):	Neverball jest gr± 3d z tocz±c± siê kulk±.
Name:		neverball
Version:	0805b
Release:	0.3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://aoeu.snth.net/neverball/neverball-%{version}.zip
# Source0-md5:	4638fbdeb8b672b974ab57cc84b54bd4
Patch0:		%{name}-datadir.patch
URL:		http://aoeu.snth.net/
BuildRequires:	guile-devel >= 1.6.3
BuildRequires:	libstdc++-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_prefix}/games
%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Tilt the floor to roll the ball through the obstacle course before
time runs out.

%description -l pl
Trackballs jest prost± gr± podobn± do klasycznej Marble Madness
napisanej na Amigê w latach 80-ych. Gracz zdobywa punkty steruj±c
marmurow± kulk± w labiryncie wype³nionym okrutnymi m³otami, ka³u¿ami
kwasu i innymi przeszkodami. Gdy kilka osi±gnie cel, przenosi siê do
nastêpnego, trudniejszego, toru. Chyba ¿e skoñczy siê czas.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} X11_LIBS="-L/usr/X11R6/lib -lGLU -lGL -lm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name}}
install neverball $RPM_BUILD_ROOT%{_bindir}
cp -R data/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt MAPPING.txt
%attr(2755,root,games) %{_bindir}/neverball
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/back
%dir %{_datadir}/games/%{name}/map
%dir %{_datadir}/games/%{name}/mtrl
%dir %{_datadir}/games/%{name}/png
%dir %{_datadir}/games/%{name}/snd
%dir %{_datadir}/games/%{name}/sol
%dir %{_datadir}/games/%{name}/ttf
%{_datadir}/games/%{name}/levels.txt
%{_datadir}/games/%{name}/*/*
