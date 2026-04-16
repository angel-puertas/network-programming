Questions for Reflection
1. What is the difference between socket.AF_INET and socket.AF_INET6?
socket.AF_INET is for IPv4 addresses while socket.AF_INET6 is for IPv6 addresses.

2. How would you add IPv6 support in Python?
I would create the socket with AF_INET6 instead of AF_INET.

3. How could a TCP application handle timeout situations with poor connections?
A TCP app can use timeouts so it does not wait forever.

Explanations for command outpus:

find_service_name.png: shows the name of the services running on the ports we selected.
local_machine_info.png: shows the computer name and local IP address
network_activity.png: finds the hostname of an IP address and shows open network ports on the computer.
remote_machine_info.png: shows the domain address for a given IP address