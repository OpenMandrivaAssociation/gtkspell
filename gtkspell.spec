%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Spell-checking addon for GTK's TextView widget
Name:		gtkspell
Version:	2.0.16
Release:	5
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
License:	GPL+
URL:		http://gtkspell.sourceforge.net/
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	gtk+2-devel
BuildRequires:	enchant-devel
BuildRequires:  gtk-doc
BuildRequires:  docbook-dtd42-xml
BuildRequires:  intltool
#
BuildRequires:  gnome-common

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words in a
GtkTextView widget.  Right-clicking a misspelled word pops up a menu of
suggested replacements.  

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Requires: %name >= %version

%description -n %{libname}
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words in a
GtkTextView widget.  Right-clicking a misspelled word pops up a menu of
suggested replacements.  

%package -n %{develname}
Summary:	%{summary}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname gtkspell 0 -d}
Requires:	%{libname} = %{version}

%description -n %{develname}
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words in a
GtkTextView widget.  Right-clicking a misspelled word pops up a menu of
suggested replacements.  


%prep
%setup -q
#gw the gtk-doc 1.13 bug:
gnome-autogen.sh

%build
%configure2_5x \
    --disable-static

%make

%install
rm -rf %{buildroot} %{name}.lang
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

%find_lang %{name}

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.16-3mdv2011.0
+ Revision: 664959
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.16-2mdv2011.0
+ Revision: 605513
- rebuild

* Thu Dec 24 2009 Götz Waschk <waschk@mandriva.org> 2.0.16-1mdv2010.1
+ Revision: 482036
- new version
- regenerate gtk-doc

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.15-2mdv2010.0
+ Revision: 425079
- rebuild

* Thu Dec 04 2008 Götz Waschk <waschk@mandriva.org> 2.0.15-1mdv2009.1
+ Revision: 309900
- update to new version 2.0.15

* Sat Aug 16 2008 Götz Waschk <waschk@mandriva.org> 2.0.14-1mdv2009.0
+ Revision: 272533
- update build deps
- new version

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 2.0.13-1mdv2009.0
+ Revision: 242299
- fix buildrequires
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0.11-4mdv2009.0
+ Revision: 221118
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Nov 04 2007 Adam Williamson <awilliamson@mandriva.org> 2.0.11-3mdv2008.1
+ Revision: 105687
- rebuild for 2008.1
- new devel policy
- new license policy


* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.0.11-2mdv2007.0
+ Revision: 108672
- Import gtkspell

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.0.11-2mdv2007.1
- Rebuild

* Thu Dec 15 2005 Götz Waschk <waschk@mandriva.org> 2.0.11-1mdk
- New release 2.0.11
- use mkrel

* Tue Jun 14 2005 G�tz Waschk <waschk@mandriva.org> 2.0.10-1mdk
- drop merged patch
- New release 2.0.10

* Fri Mar 18 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.9-2mdk 
- Patch0: disable debug

* Wed Feb 23 2005 G�tz Waschk <waschk@linux-mandrake.com> 2.0.9-1mdk
- add translations
- reenable libtoolize
- new version

* Fri Apr 23 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.5-2mdk
- Fix BuildRequires

* Sat Apr 17 2004 Abel Cheung <deaddog@deaddog.org> 2.0.5-1mdk
- New version
- Remove patch0 (similar fix upstream)

