inside `ssh` directory you need to place ssh keys, it will be used to build docker image and later for scripts to connect to that docker. 
```bash
ssh-keygen -t rsa -b 4096 -f ./ssh/id_rsa
```


Dependencies for needed are inside each directory in test_script
