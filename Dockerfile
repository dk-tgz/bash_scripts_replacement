FROM ubuntu:rolling
RUN apt update && apt install  openssh-server sudo -y
RUN  echo 'ubuntu:ubuntu' | chpasswd
RUN mkdir -vp /home/ubuntu/.ssh && chown ubuntu:ubuntu /home/ubuntu/.ssh 
COPY ./ssh/id_rsa.pub /home/ubuntu/.ssh/authorized_keys
RUN chmod 500 /home/ubuntu/.ssh/authorized_keys  && chown ubuntu:ubuntu -R /home/ubuntu/.ssh
RUN sed -i 's/^PasswordAuthentication.*$/PasswordAuthentication yes/g' /etc/ssh/sshd_config
RUN echo 'ubuntu ALL=(ALL) NOPASSWD: ALL' | tee -a /etc/sudoers
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]

