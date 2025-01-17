%global debug_package %{nil}
%define fname pyparted
%bcond_with python2

Summary:	Python module for GNU parted
Name:		python-parted
Version:	3.12.0
Release:	2
License:	GPLv2+
Group:		System/Configuration/Hardware
Url:		https://fedorahosted.org/pyparted
Source0:	https://github.com/dcantrell/pyparted/archive/v%{version}/%{fname}-%{version}.tar.gz
BuildRequires:	python-decorator
BuildRequires:	pkgconfig(libparted)
BuildRequires:	pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
Requires:	python-decorator
# Compatibility with packages <= 2013.0-beta 1
Obsoletes:	pyparted < %{EVRD}
Provides:	pyparted = %{EVRD}

%description
Python module for the parted library.  It is used for manipulating
partition tables.

%if %{with python2}
%package -n python2-parted
Summary:	Python 2.x module for GNU parted
Group:		System/Configuration/Hardware
BuildRequires:	pkgconfig(python2)

%description -n python2-parted
Python 2.x module for GNU parted
%endif

%prep
%setup -qn %{fname}-%{version}
%if %{with python2}
mkdir python2
cp -a `ls |grep -v python2` python2
%endif

%build
python setup.py build

%if %{with python2}
cd python2
python2 setup.py build
%endif

%install
python setup.py install --root=%{buildroot}

%if %{with python2}
cd python2
python2 setup.py install --root=%{buildroot}
%endif

%files
%doc AUTHORS COPYING NEWS README TODO
#{python_sitearch}/*
%{python_sitearch}/_ped.cpython-*-*-linux-gnu.so
%{python_sitearch}/parted/
%{python_sitearch}/pyparted-%{version}-py*.*.egg-info

%if %{with python2}
%files -n python2-parted
%{python2_sitearch}/*
%endif
