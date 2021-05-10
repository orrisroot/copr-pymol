# PyMOL rpm spec files for Fedora Copr build
This repository maintains the packaging files to build packages on the Fedora Copr.

https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/

## Installation Instructions of Fedora Copr build packages
Currently, Copr repository is provided only CentOS 8 packages.
```
$ sudo dnf install dnf-plugins-core
$ sudo dnf copr enable orrisroot/pymol
$ sudo dnf config-manager --set-enabled PowerTools
$ sudo dnf install epel-release
$ sudo dnf install pymol
```

## Providing Packages
* pymol : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/pymol/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/pymol/)
  * pymol-2.3.0-7.1.el8.ors.src.rpm
  * pymol-2.3.0-7.1.el8.ors.x86_64.rpm
  * pymol-debuginfo-2.3.0-7.1.el8.ors.x86_64.rpm
  * pymol-debugsource-2.3.0-7.1.el8.ors.x86_64.rpm
* apbs : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/apbs/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/apbs/)
  * apbs-1.5-4.1.el8.ors.src.rpm
  * apbs-1.5-4.1.el8.ors.x86_64.rpm
  * apbs-debuginfo-1.5-4.1.el8.ors.x86_64.rpm
  * apbs-debugsource-1.5-4.1.el8.ors.x86_64.rpm
  * apbs-devel-1.5-4.1.el8.ors.x86_64.rpm
  * apbs-doc-1.5-4.1.el8.ors.x86_64.rpm
  * apbs-tools-1.5-4.1.el8.ors.x86_64.rpm
  * apbs-tools-debuginfo-1.5-4.1.el8.ors.x86_64.rpm
* mmtf-cpp : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/mmtf-cpp/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/mmtf-cpp/)
  * mmtf-cpp-1.0.0-5.1.el8.ors.src.rpm
  * mmtf-cpp-devel-1.0.0-5.1.el8.ors.x86_64.rpm
  * mmtf-cpp-doc-1.0.0-5.1.el8.ors.noarch.rpm
* python-pmw : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/python-pmw/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/python-pmw/)
  * python-pmw-2.0.0-17.1.el8.ors.src.rpm
  * python3-pmw-2.0.0-17.1.el8.ors.noarch.rpm
* maloc : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/maloc/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/maloc/)
  * maloc-1.5-22.el8.src.rpm
  * maloc-1.5-22.el8.x86_64.rpm
  * maloc-debuginfo-1.5-22.el8.x86_64.rpm
  * maloc-debugsource-1.5-22.el8.x86_64.rpm
  * maloc-devel-1.5-22.el8.x86_64.rpm
* chemical-mime-data : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/chemical-mime-data/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/chemical-mime-data/)
  * chemical-mime-data-0.1.94-29.el8.noarch.rpm
  * chemical-mime-data-0.1.94-29.el8.src.rpm
