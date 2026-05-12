nmtui

sudo dnf update -y

sudo dnf install https://rpmfusion.org(rpm -E %fedora).noarch.rpm https://rpmfusion.org(rpm -E %fedora).noarch.rpm -y

sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda mokutil kmodtool openssl -y

sudo kmodgenca

sudo mokutil --import /etc/pki/akmods/certs/public_key.der

sudo grubby --update-kernel=ALL --args="nvidia-drm.modeset=1"

sudo reboot

