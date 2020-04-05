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
- apbs [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/apbs/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/apbs/)
- chemical-mime-data [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/chemical-mime-data/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/chemical-mime-data/)
- maloc [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/maloc/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/maloc/)
- mmtf-cpp [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/mmtf-cpp/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/mmtf-cpp/)
- msgpack [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/msgpack/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/msgpack/)
- pymol [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/pymol/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/pymol/)
- python-pmw [![Copr build status](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/python-pmw/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/orrisroot/pymol/package/python-pmw/)
