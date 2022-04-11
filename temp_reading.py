import os
import time


def main():
    """
    Program to demonstrate how to obtain the current value of the CPU temperature.
    """
    log_file = get_log_file()
    print('Temperature logging started.')
    while(True):
        curr_temperature = get_cpu_temp()
        log_file.write (str(time.time()) + '  ' + str(curr_temperature) + '\n')
        time.sleep(60)

    
def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature.
    :returns: Current value of the CPU temperature if successful, zero value otherwise.
    :rtype: float
    """
    # Initialize the result.
    result = 0.0
    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        # Test if the string is an integer as expected.
        if line.isdigit():
            # Convert the string with the CPU temperature to a float in degrees Celsius.
            result = float(line) / 1000
    # Give the result back to the caller.
    return result


def get_log_file():
    #Notify whether there is an existing log or not
    if (os.path.isfile('temp_recording.log')):
        print('Temperature logging will continue in the previous file.')
    else:
        print('No former file found. A new temperature log has been created.')
    
    log_file = open('temp_log.log', 'a')
    return log_file


if __name__ == "__main__":
    main()
