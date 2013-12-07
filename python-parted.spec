%define fname pyparted

Summary:	Python module for GNU parted
Name:		python-parted
Version:	3.10
Release:	4
License:	GPLv2+
Group:		System/Configuration/Hardware
Url:		http://fedorahosted.org/pyparted
Source0:	https://fedorahosted.org/releases/p/y/pyparted/pyparted-%{version}.tar.gz
BuildRequires:	python-decorator
BuildRequires:	pkgconfig(libparted)
BuildRequires:	pkgconfig(python)
Requires:	python-decorator
# Compatibility with packages <= 2013.0-beta 1
Obsoletes:	pyparted < %{EVRD}
Provides:	pyparted = %{EVRD}

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

