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

##############################################################
# start docker
# The recommended docker driver is overlay
# The default storage directory for docker on the vm is /var/lib/docker
# which is on the root partition. Since the storage on this partition is limited
# we can move to /dev/sda1 or other storage has bigger space, let's say ${PATH}
# Groupadd docker
DOCKER_STORAGE_DIR="${PATH}/docker"
sudo mkdir -m777 -p ${DOCKER_STORAGE_DIR}
echo "EXTRA_DOCKER_STORAGE_OPTIONS='-g ${DOCKER_STORAGE_DIR}'" | sudo tee -a /etc/sysconfig/docker-storage-setup
sudo /usr/bin/systemctl start docker.service
sudo /usr/bin/systemctl status docker.service

##############################################################
