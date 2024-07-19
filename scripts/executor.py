import paramiko
import os
import sys

# Read SSH connection configuration from environment variables
hostname = os.getenv('SSH_IP', 'localhost')
port = int(os.getenv('SSH_PORT', 22))
username = os.getenv('SSH_USERNAME', 'user')
password = os.getenv('SSH_PASSWORD', 'password')

def execute_command(command):
    try:
        # Connect to the remote server
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)

        # Execute the command on the remote server
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode('utf-8').strip()
        errors = stderr.read().decode('utf-8').strip()

        # Print the output and errors
        if output:
            print(output)
        if errors:
            print(errors, file=sys.stderr)

        # Close the SSH connection
        ssh.close()

    except Exception as e:
        print(f"Error connecting to the server: {e}", file=sys.stderr)

def main():
    if os.getenv('GET_IPS', 'false').lower() == 'true':
        from get_ips import get_ips
        get_ips()

if __name__ == "__main__":
    main()
