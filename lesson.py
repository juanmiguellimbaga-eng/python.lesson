from netmiko import ConnectHandler

router_device = {
    'device_type': "cisco_ios_telnet",
    'ip': "192.168.10.101",
    'port': 32770,
    'username': "admin",
    'password': "eve",
    'secret': "eve",
}


try:
    print("Connecting to the router...")

    net_connect = ConnectHandler(**router_device)

    net_connect.enable()

    commands_to_run = [
        "show version",
        "show ip interface brief",
        "show running-config",
    ]

    for cmd in commands_to_run:
        print(f"\n--- Output of '{cmd}' ---")
        output = net_connect.send_command(cmd)
        print(output)

        net_connect.disconnect()
        print("\nDisconnected sucessfully.")
except Exception as e:
    print(f"An error occurred: {e}")
