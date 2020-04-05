%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: apbs
Summary: Adaptive Poisson Boltzmann Solver
Version: 1.5
Release: 4.1%{?dist}.ors
# License of pmgZ, aqua and contrib/blas/mblasd.f is LGPLv2+, the rest is BSD.
License: LGPLv2+ and BSD
URL: http://apbs.sourceforge.net/
Source0: https://github.com/Electrostatics/apbs-pdb2pqr/archive/apbs-%{version}.tar.gz
Patch0: apbs-cmake.patch
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: arpack-devel
BuildRequires: atlas-devel
BuildRequires: blas-devel
BuildRequires: maloc-devel
BuildRequires: tex(latex)
BuildRequires: zlib-devel

%description
APBS is a software package for the numerical solution of the
Poisson-Boltzmann equation (PBE), one of the most popular continuum
models for describing electrostatic interactions between molecular
solutes in salty, aqueous media.  APBS was designed to efficiently
evaluate electrostatic properties for such simulations for a wide
range of length scales to enable the investigation of molecules with
tens to millions of atoms. It is also widely used in molecular
visualization (in such applications as PyMOL).

%package tools
Summary: utility programs that utilize the APBS package
Requires: %{name} = %{version}-%{release}

%description tools

The apbs-tools package contains several utility programs for
conversion, analysis and preparation of files that use the adaptive
poisson boltzmann solver library.

%package devel
Summary: Libraries and header files for the APBS package
Requires: %{name} = %{version}-%{release}

%description devel

The apbs-devel package contains the header files and libraries
necessary for developing programs using the adaptive poisson boltzmann
(APBS) solver library.

%package doc
Summary: Documentation for the APBS package
Requires: %{name} = %{version}-%{release}

%description doc

The apbs-doc package contains API reference inforemation for
development using the adaptive poisson boltzmann (APBS) solver
library.

%prep
%setup -q -n %{name}-pdb2pqr-apbs-%{version}
cd apbs
%patch0 -p0

%build
cd apbs
# %cmake -D BUILD_DOC:BOOL=ON .
%cmake -D BUILD_DOC:BOOL=OFF .
make %{?_smp_mflags}
cd doc/programmer
doxygen

%install
rm -rf %{buildroot}

cd apbs
make install DESTDIR=%{buildroot}

# tools
for bin in %{buildroot}%{_bindir}/{coulomb,born,mgmesh,dxmath,mergedx2,mergedx,value,uhbd_asc2bin,smooth,dx2mol,dx2uhbd,similarity,multivalue,benchmark,analysis,del2dx,tensor2dx} tools/manip/psize.py; do
    mv $bin %{buildroot}%{_bindir}/apbs-`basename $bin`
done

%ldconfig_scriptlets

%files
%doc apbs/doc/license/LICENSE.txt apbs/doc/README apbs/doc/ChangeLog.md
%{_bindir}/apbs
%{_libdir}/libapbs*.so.*

%files tools
%{_bindir}/apbs-psize.py
%{_bindir}/apbs-coulomb
%{_bindir}/apbs-born
%{_bindir}/apbs-mgmesh
%{_bindir}/apbs-dxmath
%{_bindir}/apbs-mergedx2
%{_bindir}/apbs-mergedx
%{_bindir}/apbs-value
%{_bindir}/apbs-uhbd_asc2bin
%{_bindir}/apbs-smooth
%{_bindir}/apbs-dx2mol
%{_bindir}/apbs-dx2uhbd
%{_bindir}/apbs-similarity
%{_bindir}/apbs-multivalue
%{_bindir}/apbs-benchmark
%{_bindir}/apbs-analysis
%{_bindir}/apbs-del2dx
%{_bindir}/apbs-tensor2dx

%files devel
%{_libdir}/libapbs*.so
%{_includedir}/apbs

%files doc
%doc apbs/doc/programmer/html

%changelog
* Sun Apr 05 2020 Yoshihiro Okumura <orrisroot@gmail.com> - 1.5-4.1
- Rebuild for EPEL 8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 19 2018 Tim Fenn <tim.fenn@gmail.com> - 1.5-1
- update to 1.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Tim Fenn <tim.fenn@gmail.com> - 1.4-1
- update to 1.4

* Wed Jun 18 2014 Tim Fenn <tim.fenn@gmail.com> - 1.3-8
- fix for bug 1105956 (apbslib.c patch for format-security error)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 30 2013 Tim Fenn <tim.fenn@gmail.com> - 1.3-7
- rebuild for atlas 3.10.1 (consolidates lapack and blas)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Tim Fenn <fenn@stanford.edu> - 1.3-1
- update to 1.3

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Dec 01 2009 Tim Fenn <fenn@stanford.edu> - 1.2.1-2
- add RPM_OPT_FLAGS

* Wed Nov 25 2009 Tim Fenn <fenn@stanford.edu> - 1.2.1-1
- update to 1.2.1

* Tue Nov 24 2009 Tim Fenn <fenn@stanford.edu> - 1.2.0-2
- fix broken source

* Thu Nov 04 2009 Tim Fenn <fenn@stanford.edu> - 1.2.0-1
- update to 1.2.0

* Mon Jul 27 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-7
- remove python byte compiled files in bindir
- loop to add tools

* Sun Jul 26 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-6
- remove check macro

* Fri Jul 24 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-5
- enable and add arpack, python to buildrequires, fix files section accordingly
- add check macro
- move tools to a subpackage
- move doc into subpackage
- spec cleanup

* Thu Jul 23 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-4
- merge aqua and pmgZ into libapbs

* Fri Jul 10 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-3
- separate aqua and pmgZ into separate libraries/packages
- add maloc BuildRequires

* Mon May 04 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-2
- fix RPM_BUILD_ROOT
- rename patches
- add "-q" to setup
- add README to doc
- edit description
- edit license

* Fri Apr 24 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-1
- initial build
