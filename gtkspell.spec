%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Spell-checking addon for GTK's TextView widget
Name:		gtkspell
Version:	2.0.16
Release:	5
License:	GPL+
URL:		http://gtkspell.sourceforge.net/
Group:		System/Libraries
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
Suggests:	%{libname} = %{version}-%{release}

%description -n %{libname}
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words in a
GtkTextView widget.  Right-clicking a misspelled word pops up a menu of
suggested replacements.  

%package -n %{develname}
Summary:	%{summary}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname gtkspell 0 -d}

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

%files -f %{name}.lang
%doc README AUTHORS ChangeLog

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

