
def cpu():

    path = "/sys/class/hwmon/hwmon2/temp1_input"
    with open(path, "r") as cpu_temp:
        content = cpu_temp.read()
        return int(content) / 1000

def gpu():

    path = "/sys/class/hwmon/hwmon1/temp1_input"
    with open(path, "r") as gpu_temp:
        content = gpu_temp.read()
        return int(content) / 1000

def motherboard():

    path = "/sys/class/hwmon/hwmon0/temp1_input"
    with open(path, "r") as mboard_temp:
        content = mboard_temp.read()
        return int(content) / 1000

def uptime():

    path = "/proc/uptime"
    with open(path, "r") as uptime:
        content = uptime.read()
        cut = content.split(" ")[0]
        preparator = cut.index(".")
        convertor = cut[:preparator]
        internum = f"{int(convertor) / 3600}"
        calc = internum[2] + internum[3]
        minutes = str((int(calc) * 60))

        return str(internum[0]) + "h:" + minutes[:2]




