# 0x0B. SSH

## Description:

This module exploits a vulnerability in the OpenSSH server that allows for remote code execution as root via an authenticated user, and can be used to gain persistence on systems running this service by leveraging sudo privileges of any users with access to run commands through sshd (e.g., `root`).
