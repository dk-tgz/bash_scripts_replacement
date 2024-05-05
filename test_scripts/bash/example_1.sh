#!/bin/bash
set -exuo pipefail
sudo touch /etc/test
ls -lrt /etc/test
sudo rm -rf /etc/test
ls -lrt /etc/test


