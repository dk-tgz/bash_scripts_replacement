#!/bin/bash
set -ex
podman rm -f dkos || : 
podman run -d --name dkos -p 2222:22 dk/ubuntu
