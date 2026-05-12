sudo dnf update -y

sudo dnf install -y \
https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda mokutil kmodtool openssl

sudo kmodgenca -a

sudo mokutil --import /etc/pki/akmods/certs/public_key.der

sudo grubby --update-kernel=ALL --args="nvidia-drm.modeset=1"

# after
#sudo akmods --force
#sudo dracut --force
#sudo reboot

