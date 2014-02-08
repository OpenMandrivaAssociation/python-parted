%define fname pyparted

Summary: Python module for GNU parted
Name:    python-parted
Version: 3.10
Release: 3
License: GPLv2+
Group:   System/Configuration/Hardware
URL:     http://fedorahosted.org/pyparted
Source0: https://fedorahosted.org/releases/p/y/pyparted/pyparted-%{version}.tar.gz
BuildRequires: python-devel
BuildRequires: parted-devel >= 1.9.0-20
BuildRequires: python-decorator
Requires: python-decorator
# Compatibility with packages <= 2013.0-beta 1
Obsoletes: pyparted < %EVRD
Provides: pyparted = %EVRD

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
