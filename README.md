# GOES-Grafana-Monitoring
A Python-based Prometheus exporter for monitoring metrics from the GOES Receiver.

# Features
 • Pulls information from such as System Info, CPU Usage, CPU Temp, Memory Usage, Disk Usage, Service Status, CPU Temp, HRIT Packets/Sec (1HR), Gain       Multiplier (1HR), Frequency Offset, Omega (Samples/Symbol), Viterbi Error Corrections / Packet and eed-Solomon Errors / Second.

 # Requirements
 • Python 3.x
 
 • requests
 
 • prometheus_client
 
 • time
 
 • re

 # Installation
1. Clone the repository:
   ```
   git clone https://github.com/jhgrazier/
   ```

2. Change into the cloned directory

   ```
   cd xxx
   ```

3. Install required Python requirements

   ```
   pip install prometheus_client requests time re
   ```

4. Copy the xxx into /usr/bin
   
   ```
   ```

5. Install the service files into /etc/systemd/system
   
   ```   
   ```

# Configuration

1. Edit the netgear-exporter.py to adjust the password.

# Prometheus Configuration

1. Add the following job to your Prometheus configuration (adjust localhost to the correct IP if they are not running on the same machine):

   ```
   - job_name: 'goes-receiver'
     metrics_path: '/metrics'
     static_configs:
       - targets: ['192.168.32.5:9102']
   ```

# Final Configuration

1. Enable and Start the service
   ```
   ```

2. Validate the service started
   ```
   ```

# Verify Metrics 

1. Run this curl command from command line on your host where prometheus is installed.
   ```
   curl http://localhost:9102/metrics
   ```

2. You should see something like the following:
   ```
   ```

# Dashboard
