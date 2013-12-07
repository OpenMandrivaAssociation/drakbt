Summary:	The Mandriva Linux Bittorrent link and status checker
Name:		drakbt
Version:	0.17.5
Release:	6
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://qa.mandriva.com
#cvs source
# http://www.mandrivalinux.com/en/cvs.php3
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	perl-MDK-Common-devel
Requires:	drakxtools
Requires:	perl-libwww-perl
Requires:	perl-Digest-SHA1
Requires:	transmission-gui
Requires(post,postun):	desktop-file-utils

%description
Drakbt reports status information for a given torrent file or URL. 
It can connect automatically to Mandriva Linux websites to grab and 
display available torrents.
You should provide login and password if you want to connect to club
member restricted torrents. 
After all checks are done, you can trigger the download process from
drakbt.

Information displayed are :
- current number of complete copies (seeds) 
- incomplete copies (leeches) currently active.
- Bittorrent port reachability
- Hash info ....

%prep
%setup -q

%build

%install
make PREFIX=%{buildroot} install 

#menu-xdg
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Bittorrent Checker
Comment=Mandriva Linux Bittorrent checker
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
MimeType=application/x-bittorrent;
Categories=GTK;Network;FileTransfer;P2P;X-MandrivaLinux-CrossDesktop;
EOF

#install lang
%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING
%{_bindir}/*
/usr/lib/libDrakX/network/*.pm
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}*.desktop
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png

