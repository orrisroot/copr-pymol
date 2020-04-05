%global debug_package %{nil}

%bcond_without doc

# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

Name:    mmtf-cpp
Version: 1.0.0
Release: 4.1%{?dist}.ors
Summary: The Macromolecular Transmission Format (MMTF) header only files
License: MIT
URL:     https://github.com/rcsb/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake3, %{?dts}gcc, %{?dts}gcc-c++

%description
The Macromolecular Transmission Format (MMTF) is a new compact binary format to transmit and
store biomolecular structures for fast 3D visualization and analysis.
This package holds the C++-03 compatible API, encoding and decoding libraries.

%package devel
Summary: Development files for %{name}
Requires: msgpack-devel%{?_isa} >= 2.1.5
Provides: %{name}-static = %{version}-%{release}
%description devel
Header only files for developing applications that use mmtf-cpp.

%if %{with doc}
%package doc
Summary: Documentation files
BuildRequires:  doxygen
BuildArch: noarch
%description doc
HTML documentation files for mmtf-cpp.
%endif

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p build && pushd build
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif
%cmake3 ..
%make_build
popd

%if %{with doc}
pushd docs
doxygen
popd
%endif

%install
%make_install -C build

%files devel
%doc *.md
%license LICENSE
%{_includedir}/mmtf/
%{_includedir}/mmtf.hpp

%if %{with doc}
%files doc
%license LICENSE
%doc docs/html
%endif

%changelog
* Sun Apr 05 2020 Yoshihiro Okumura <orrisroot@gmail.com> - 1.0.0-4.1
- Rebuild for EPEL 8

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.0.0-3
- Use cmake3

* Sun Dec 08 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.0.0-2
- Provide virtual static libraries

* Sat Dec 07 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.0.0-1
- Release 1.0.0
