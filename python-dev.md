# Python dev 

## Create Python virtual environment
Do this after first checkout.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## First time package installation
```
pip install numpy
pip freeze | grep numpy >> requirements.txt
pip install matplotlib
pip freeze | grep matplotlib >> requirements.txt
pip install pandas
pip freeze | grep pandas >> requirements.txt
```
## Upgrade package
Conservative upgrade:
```
pip install <packagename> --upgrade
```
Upgrading with "eager" gives the same package version as we would have ended up with if we installed the new version from start.
```
pip install <packagename> --upgrade --upgrade-strategy eager
```
## Reinstalling everything
```
rm -rf venv
```
then setup a new venv from scratch.
