#!/bin/bash

NAME=$(basename $PWD)
if [ ! -f "${NAME}.spec" ]; then
  echo Error: spec file not found: ${NAME}.spec
  exit 1
fi

rpkg --module-name "rpms/${NAME}" $*

