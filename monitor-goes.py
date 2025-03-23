import statsd
import os
import psutil
import subprocess
import time

c = statsd.StatsClient('localhost', 8125, prefix='goes_receiver')

def get_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            return int(f.read()) / 1000.0
    except FileNotFoundError:
        return None

def is_service_running(service):
    try:
        subprocess.check_output(['systemctl', 'is-active', '--quiet', service])
        return 1
    except subprocess.CalledProcessError:
        return 0

while True:
    c.incr('heartbeat')
    c.gauge('cpu_percent', psutil.cpu_percent(interval=1))
    c.gauge('memory_percent', psutil.virtual_memory().percent)
    c.gauge('disk_percent', psutil.disk_usage('/').percent)
    c.gauge('uptime_seconds', time.time() - psutil.boot_time())
    c.gauge('status_goesrecv', is_service_running('goesrecv'))
    c.gauge('status_goesproc', is_service_running('goesproc'))

    temp = get_temp()
    if temp is not None:
        c.gauge('cpu_temp_celsius', temp)

    time.sleep(30)
    
