Summary: Minimal Abstraction Layer for Object-oriented C
Name: maloc
Version: 1.5
Release: 22%{?dist}
License: GPLv2+
URL: http://www.fetk.org
Source0: http://www.fetk.org/codes/download/%{name}-%{version}.tar.gz
# removes hardcoded libdir setting
Patch0: maloc-makefile.am.patch
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: doxygen
BuildRequires: libtool
BuildRequires: readline-devel

%description
MALOC is a small, portable, abstract C environment library for
object-oriented C programming. MALOC is used as the foundation layer
for a number of scientific applications, including MC, SG, and
APBS. MALOC can be used as a small stand-alone abstraction environment
for writing portable C programs which need access to resources which
are typically architecture-dependent, such as INET sockets, timing
routines, and so on. MALOC provides abstract datatypes, memory
management routines, timing routines, machine epsilon, access to UNIX
and INET sockets, MPI, and so on. All things that can vary from one
architecture to another are abstracted out of an application code and
placed in MALOC.

%package devel
Summary: Header files and library for developing programs with maloc
Requires: %{name} = %{version}-%{release}

%description devel

This package contains libraries and header files needed for program
development using MALOC.

%prep
%setup -n %{name} -q
%patch0 -p0
aclocal
libtoolize --automake
autoconf
automake --gnu --add-missing
autoheader

%build
%configure --disable-static
make %{?_smp_mflags}

make maloc_doc -C doc/doxygen

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*

%files devel
%doc doc/api/html/*
%{_libdir}/*.so
%{_includedir}/maloc

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5-18
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5-11
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Tim Fenn <tim.fenn@gmail.com> - 1.5-3
- fix autotools order

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Tim Fenn <fenn@stanford.edu> - 1.5-1
- update to 1.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Tim Fenn <fenn@stanford.edu> - 1.4-1
- update to 1.4

* Fri Aug 21 2009 Tim Fenn <fenn@stanford.edu> - 0.2-4
- patch to remove missing INPUT paths from doxygen build

* Thu Aug 06 2009 Tim Fenn <fenn@stanford.edu> - 0.2-3
- add doxygen as buildreq

* Sat Jul 11 2009 Tim Fenn <fenn@stanford.edu> - 0.2-2
- remove pkgconfig dependency
- build doc

* Fri Jul 10 2009 Tim Fenn <fenn@stanford.edu> - 0.2-1
- initial build
