%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Spell-checking addon for GTK's TextView widget
Name:		gtkspell
Version:	2.0.11
Release:	%mkrel 3
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.bz2
License:	GPL+
URL:		http://gtkspell.sourceforge.net/
Group:		System/Libraries
BuildRequires:	gtk+2-devel
BuildRequires:	aspell-devel >= 0.50.2
BuildRequires:  gtk-doc
BuildRequires:  docbook-dtd42-xml

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

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang

%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*


