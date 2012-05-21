%define fname pyparted

Summary: Python module for GNU parted
Name:    python-parted
Version: 3.8
Release: 2
License: GPLv2+
Group:   System/Configuration/Hardware
URL:     http://fedorahosted.org/pyparted
Source0: http://fedorahosted.org/releases/p/y/%{fname}/%{fname}-%{version}.tar.gz
BuildRequires: python-devel
BuildRequires: parted-devel >= 1.9.0-20
BuildRequires: python-decorator

Requires: python-decorator

%description
Python module for the parted library.  It is used for manipulating
partition tables.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{python_sitearch}/*

