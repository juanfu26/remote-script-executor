from executor import execute_command

# Command to get the IPs of the network interfaces
command = "ip -o -4 addr list | awk '{print $4}'"

def get_ips():
    execute_command(command)
