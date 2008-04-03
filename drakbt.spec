%define name	drakbt
%define version	0.17
%define release %mkrel 1

Summary:	The Mandriva Linux Bittorrent link and status checker
Name:		%{name}
Version:	%{version}
Release:    %{release}
#cvs source
# http://www.mandrivalinux.com/en/cvs.php3
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2+
URL:		http://qa.mandriva.com
Group:		Networking/File transfer
Requires:	drakxtools >= 10-57mdk, perl-libwww-perl >= 5.800-1mdk, perl-Digest-SHA1 >= 2.10-1mdk, bittorrent-gui
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils

BuildArch:	noarch
BuildRequires:	perl-MDK-Common-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
rm -rf %{buildroot}
make PREFIX=%{buildroot} install 

#menu-xdg
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%post
%{update_menus}
%{update_desktop_database}

%postun
%{clean_menus}
%{clean_desktop_database}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
/usr/lib/libDrakX/network/*.pm
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}*.desktop
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png

