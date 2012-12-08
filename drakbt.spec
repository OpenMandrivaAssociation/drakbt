%define name	drakbt
%define version	0.17.5
%define release %mkrel 4

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
Requires:	drakxtools >= 10-57mdk, perl-libwww-perl >= 5.800-1mdk, perl-Digest-SHA1 >= 2.10-1mdk, transmission-gui
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

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%endif

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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.17.5-3mdv2011.0
+ Revision: 663850
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.17.5-2mdv2011.0
+ Revision: 604815
- rebuild

* Wed May 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.17.5-1mdv2010.1
+ Revision: 546254
- 0.17.5
- translation updates

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.17.4-4mdv2010.1
+ Revision: 522484
- rebuilt for 2010.1

* Tue Aug 25 2009 Frederik Himpe <fhimpe@mandriva.org> 0.17.4-3mdv2010.0
+ Revision: 421287
- Bittorrent-gui is dead, now require transmission-gui

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.17.4-2mdv2010.0
+ Revision: 413378
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.17.4-1mdv2009.1
+ Revision: 367399
- translation updates

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.17.3-1mdv2009.1
+ Revision: 362325
- translation updates

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.17.2-1mdv2009.0
+ Revision: 286976
- translation updates

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.17.1-2mdv2009.0
+ Revision: 264418
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 0.17.1-1mdv2009.0
+ Revision: 192826
- fix crash (#40045)

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.17-1mdv2008.1
+ Revision: 192090
- translation updates

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.16-1mdv2008.1
+ Revision: 190090
- translation updates
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 19 2007 Thierry Vignaud <tv@mandriva.org> 0.15-1mdv2008.1
+ Revision: 110413
- fix crash on opening help (#35271)

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 0.14-1mdv2008.0
+ Revision: 95059
- updated translation

* Sat Sep 15 2007 Thierry Vignaud <tv@mandriva.org> 0.13-1mdv2008.0
+ Revision: 86822
- translation snapshot

* Sat Sep 15 2007 Adam Williamson <awilliamson@mandriva.org> 0.12-2mdv2008.0
+ Revision: 85811
- rebuild for 2008
- clean up menu categories
- Fedora license policy


* Mon Mar 12 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.12-1mdv2007.1
+ Revision: 141858
- translation snapshot

* Thu Feb 15 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.11-2mdv2007.1
+ Revision: 121401
- fix build on x86_64
- Import drakbt

* Thu Feb 15 2007 Frederic Crozat <fcrozat@mandriva.com> 0.11-2mdv2007.1
- Fix XDG menu, drop old menu and mimetypes stuff (handled by freedesktop)

* Sun Sep 17 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.11-1mdv2007.0
- use %%mkrel
- updated translations
- XDG menu (steletcha)
- add requires(post,postun) and appropriate macros for mime type (steletcha)

* Fri Sep 16 2005 Daouda LO <daouda@mandriva.com> 0.10-9mdk
- fix typo
- update translations

* Fri Sep 16 2005 Daouda LO <daouda@mandriva.com> 0.10-8mdk
- pause option doesn't exist pour 10.1 shipped bittorrent package

* Thu Sep 15 2005 Daouda LO <daouda@mandriva.com> 0.10-7mdk
- Give correct URL to drakbt for public torrents
- po updates

* Thu Sep 15 2005 Daouda LO <daouda@mandriva.com> 0.10-6mdk
- fix crash when asking more infos about inexistent torrent
- fix requires
- Don't use '--no-check-certificate' with wget version <= 1.10

* Wed Sep 14 2005 Daouda LO <daouda@mandriva.com> 0.10-5mdk
- option --no-check-certificate with wget for access to club torrents

* Wed Sep 14 2005 Daouda LO <daouda@mandriva.com> 0.10-4mdk
- handle bittorrent binary name change for distros prior to 2006.0
- po updates

* Thu Sep 08 2005 Daouda LO <daouda@mandriva.com> 0.10-3mdk
- adapt to club server changes
- binary name change (btdownloadgui.py renamed bittorrent)
- Update requires

* Wed Jul 27 2005 Daouda LO <daouda@mandriva.com> 0.10-2mdk
- sync with changes in ugtk2 #17035 (oblin)

* Fri May 13 2005 Daouda LO <daouda@mandriva.com> 0.10-1mdk
- fix mime type file association 
- cleanup

* Sun May 08 2005 Daouda LO <daouda@mandriva.com> 0.9.1-1mdk
- switch to mandriva

* Sun Apr 03 2005 Daouda LO <daouda@mandrakesoft.com> 0.9.1-0.2mdk
- don't use --url option with btdownloadgui.py (#14500)
- Browse and launch local files through drakbt
- use --pause 0, to start download immediately

* Wed Feb 23 2005 Daouda LO <daouda@mandrakesoft.com> 0.9.1-0.1mdk
- 0.9.1 pre-release
- Use brand new btdownloadgui.py
- pass the --url option to btdownloadgui.py and strip http string out.
- fix FileSelector crash bug (#13939)

* Fri Jan 21 2005 Daouda LO <daouda@mandrakesoft.com> 0.8.1-7mdk
- fix main loop

* Wed Oct 06 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.8.1-6mdk
- Rebuild

* Tue Oct 05 2004 Daouda LO <daouda@mandrakesoft.com> 0.8.1-5mdk
- added command line file and http/ftp link handling
- don't try to get file attributes on combo entry changed (#)
- added mime type file (Initial pref for drakbt)

* Wed Sep 15 2004 Daouda LO <daouda@mandrakesoft.com> 0.8.1-4mdk
- po updates
- fix deep freeze in drakbt when parsing torrent files

* Sat Aug 28 2004 Daouda LO <daouda@mandrakesoft.com> 0.8.1-3mdk
- display help first
- drakbt src rpm lost in cyberspace

* Thu Aug 26 2004 Daouda LO <daouda@mandrakesoft.com> 0.8.1-2mdk
- help window
- strict requires on bittorrent-gui
- new icons
- retrieve correct seeds and leeches
- gui fixes and more error checkings

* Thu Aug 19 2004 Daouda LO <daouda@mandrakesoft.com> 0.8.1-1mdk
- first mdk release

