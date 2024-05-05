#!/bin/bash
set -exuo pipefail
ssh -i ../../ssh/id_rsa ubuntu@localhost -p 2222 < example_1.sh
