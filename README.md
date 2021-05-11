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
  * apbs-3.0.0-7.1.el8.ors.x86_64.rpm
  * apbs-libs-3.0.0-7.1.el8.ors.x86_64.rpm
  * apbs-tools-3.0.0-7.1.el8.ors.x86_64.rpm
  * apbs-doc-3.0.0-7.1.el8.ors.noarch.rpm
  * apbs-devel-3.0.0-7.1.el8.ors.x86_64.rpm
  * apbs-debuginfo-3.0.0-7.1.el8.ors.x86_64.rpm
  * apbs-libs-debuginfo-3.0.0-7.1.el8.ors.x86_64.rpm
  * apbs-tools-debuginfo-3.0.0-7.1.el8.ors.x86_64.rpm
  * apbs-debugsource-3.0.0-7.1.el8.ors.x86_64.rpm
  * apbs-3.0.0-7.1.el8.ors.src.rpm
* python-pmw : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/python-pmw/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/python-pmw/)
  * python3-pmw-2.0.0-20.el8.noarch.rpm
  * python-pmw-2.0.0-20.el8.src.rpm
* maloc : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/maloc/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/maloc/)
  * maloc-1.5-22.el8.x86_64.rpm
  * maloc-devel-1.5-22.el8.x86_64.rpm
  * maloc-debuginfo-1.5-22.el8.x86_64.rpm
  * maloc-debugsource-1.5-22.el8.x86_64.rpm
  * maloc-1.5-22.el8.src.rpm
* chemical-mime-data : [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/chemical-mime-data/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/chemical-mime-data/)
  * chemical-mime-data-0.1.94-29.el8.noarch.rpm
  * chemical-mime-data-0.1.94-29.el8.src.rpm
