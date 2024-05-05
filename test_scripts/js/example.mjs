#!/usr/bin/env zx

const { NodeSSH } = require('node-ssh');

const ssh = new NodeSSH();

const sshConfig = {
  host: 'localhost',
  port: 2222,
  username: 'ubuntu',
  privateKeyPath: '../../ssh/id_rsa'
};

async function remoteConnect(sshConfig) {
  try { 
  await ssh.connect(sshConfig);
  }
  catch(err) {
   console.error(err);
   disconnect(ssh)
  }
}

async function disconnect(ssh) {
 ssh.dispose();
}

async function runCommand(command,ssh) {
  try {
    const out = await ssh.execCommand(command);
    if (out.code != 0) {
	  console.log(out.stderr);
    }
    console.log(command + " executed details:\n" + JSON.stringify(out) );
  } catch (err) {
    console.error('Error during execution:\n', err);
}
}

( async () => {
const connection = await remoteConnect(sshConfig);
await runCommand("sudo ls -lrt /etc/test", ssh);
await runCommand("sudo rm -rf /etc/test", ssh);
await runCommand("sudo touch /etc/test", ssh);
await runCommand("sudo ls -lrt /etc/test", ssh);
await disconnect(ssh);
})();
