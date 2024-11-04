# coprocessor
contains code intended to be run on an FRC robot's coprocessor

``` bash
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install pynetworktables
pip install ntcore # don't actually need this

python main.py 192.168.88.135 # robot or simulator IP address
```