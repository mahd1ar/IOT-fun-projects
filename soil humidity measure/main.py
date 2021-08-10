import matplotlib.pyplot as plt
import time
import serial
import re

y_axis_limit = 4
serial_port = "COM3"  # depending on you setup and operating system

plt.style.use('dark_background')

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')

ax.axis([0, y_axis_limit, 60, 70])
ax.grid(True, linewidth=0.5, color='#ff0000', linestyle='-')

ser = serial.Serial(serial_port, 9600, timeout=1)
ser.flush()
iterate = 0
x = list()
y = list()


def read_from_serial(i):
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        exported_string = re.findall("\d{2}\.\d{2}", line)

        if len(exported_string) > 0:
            if i > y_axis_limit:
                ax.axis([0, i, 60, 70])

            new_data = float(exported_string[0])
            x.append(i)
            y.append(new_data)
            return True

        return False

    return False


if __name__ == "__main__":

    while True:
        res = read_from_serial(iterate)

        if res:
            iterate += 1
            ax.plot(x, y, "o-", color="green")

        plt.pause(0.05)
