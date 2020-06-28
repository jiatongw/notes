#! /bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

function gitVersion {
  git describe --tags --always --dirty --abbrev=7
}

function sha256 {
  local cmd

  if command -v sha256sum &> /dev/null; then
    cmd=(sha256sum)
  elif command -v shasum &> /dev/null; then
    cmd=(shasum -a 256)
  else
    echo "ERROR: could not find shasum or sha256sum."
    return 1
  fi

  "${cmd[@]}" "$@"
}
