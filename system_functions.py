import psutil


def cpu():

    cpu_temperature = psutil.sensors_temperatures()

    cpu_names = ['coretemp', 'k10temp', 'k8temp']
    sensor_labels = {
        'coretemp': ['Package id 0'],
        'k10temp': ['Tdie', 'Tctl'],
        'k8temp': ['Tctl']
    }


    for name in cpu_names:
        try:
            for temp in cpu_temperature[name]:
                if temp.label in sensor_labels[name]:
                    return temp.current

        except KeyError:
            pass

def gpu():
    gpu_temperature = psutil.sensors_temperatures()

    gpu_names = ['amdgpu', 'nvidia', 'nouveau', 'i1915', 'xe', 'radeon', 'lima', 'panfrost']

    try:
        for name in gpu_names:
            for temp in gpu_temperature[name]:
                return temp.current
    except KeyError:
        pass

def acpitz():

    acpitz_temperature = psutil.sensors_temperatures()
    
    return acpitz_temperature['acpitz'][0].current

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
