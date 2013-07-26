%define fname pyparted

Summary: Python module for GNU parted
Name:    python-parted
Version: 3.10
Release: 1
License: GPLv2+
Group:   System/Configuration/Hardware
URL:     http://fedorahosted.org/pyparted
Source0: https://fedorahosted.org/releases/p/y/pyparted/pyparted-%{version}.tar.gz
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



%changelog
* Mon May 21 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.8-2
+ Revision: 799813
- rebuild for parted

* Mon Jul 11 2011 Funda Wang <fwang@mandriva.org> 3.8-1
+ Revision: 689560
- new version 3.8
- new verison 3.6
- link with py2.7
- rebuild for new parted

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3.0-3mdv2011.0
+ Revision: 592314
- rebuild for python 2.7

* Sat Feb 27 2010 Funda Wang <fwang@mandriva.org> 3.0-2mdv2010.1
+ Revision: 512204
- rebuild for new parted

* Tue Jan 19 2010 Frederik Himpe <fhimpe@mandriva.org> 3.0-1mdv2010.1
+ Revision: 493818
- update to new version 3.0

* Sun Dec 27 2009 Thierry Vignaud <tv@mandriva.org> 2.5-3mdv2010.1
+ Revision: 482658
- use full parted API now that RH patches are merged upstream

* Sun Dec 27 2009 Funda Wang <fwang@mandriva.org> 2.5-2mdv2010.1
+ Revision: 482623
- rebuild for new parted

* Sun Dec 20 2009 Thierry Vignaud <tv@mandriva.org> 2.5-1mdv2010.1
+ Revision: 480263
- import python-parted


* Sun Dec 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.5-1mdv2010.1
- initial release based on fedora package
- patch 0: build fixes

