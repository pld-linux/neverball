#
# TODO: summary, description (check), cleanups, check BRs
#       add .desktop, make it build
#
Summary:	Game similar to Marble Madness
Summary(pl):	Gra podobna do Marble Madness
Name:		neverball
Version:	0805b
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://aoeu.snth.net/neverball/neverball-%{version}.zip
# Source0-md5:	4638fbdeb8b672b974ab57cc84b54bd4
URL:		http://aoeu.snth.net/
BuildRequires:	guile-devel >= 1.6.3
BuildRequires:	libstdc++-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	%{_prefix}/games
%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Trackballs is a simple game similar to the classical game Marble
Madness on the Amiga in the 80's. By steering a marble ball through a
labyrinth filled with vicious hammers, pools of acid and other
obstacles the player collects points. When the ball reaches the
destination it continues to the next, more difficult track - unless
the time runs out.

%description -l pl
Trackballs jest prost± gr± podobn± do klasycznej Marble Madness
napisanej na Amigê w latach 80-ych. Gracz zdobywa punkty steruj±c
marmurow± kulk± w labiryncie wype³nionym okrutnymi m³otami, ka³u¿ami
kwasu i innymi przeszkodami. Gdy kilka osi±gnie cel, przenosi siê do
nastêpnego, trudniejszego, toru. Chyba ¿e skoñczy siê czas.

%prep
%setup -q -n %{name}

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%{__make} CFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -I/usr/X11R6/include -I/usr/include/SDL"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README README.html TODO
%attr(2755,root,games) %{_bindir}/trackballs
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/music
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_datadir}/%{name}/levels
%{_datadir}/%{name}/sfx
%{_mandir}/man6/*
%attr(664,root,games) %config(noreplace) %verify(not,md5,size,mtime) /var/games/trackballs

%{_applnkdir}/Games/*
%{_pixmapsdir}/*
