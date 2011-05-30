%define fname pyparted

Summary: Python module for GNU parted
Name:    python-parted
Version: 3.0
Release: %mkrel 4
License: GPLv2+
Group:   System/Configuration/Hardware
URL:     http://fedorahosted.org/pyparted

Source0: http://fedorahosted.org/releases/p/y/%{fname}/%{fname}-%{version}.tar.gz
Patch0: pyparted-3.0-link.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-devel
BuildRequires: parted-devel >= 1.9.0-20
BuildRequires: pkgconfig
BuildRequires: python-decorator

Requires: python-decorator

%description
Python module for the parted library.  It is used for manipulating
partition tables.

%prep
%setup -q -n %fname-%version
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{python_sitearch}/_pedmodule.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{python_sitearch}/_pedmodule.so
%{python_sitearch}/parted

