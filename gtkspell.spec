%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	Spell-checking addon for GTK's TextView widget
Name:		gtkspell
Version:	2.0.16
Release:	14
License:	GPLv2
Group:		System/Libraries
Url:		http://gtkspell.sourceforge.net/
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz

BuildRequires:  docbook-dtd42-xml
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words in a
GtkTextView widget.  Right-clicking a misspelled word pops up a menu of
suggested replacements.  

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Requires:	%{name} >= %{version}

%description -n %{libname}
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words in a
GtkTextView widget.  Right-clicking a misspelled word pops up a menu of
suggested replacements.  

%package -n %{devname}
Summary:	%{summary}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS ChangeLog

%files -n %{libname}
%{_libdir}/libgtkspell.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

