# Kluczowe dla działania Nvidii
env = LIBVA_DRIVER_NAME,nvidia
env = XDG_SESSION_TYPE,wayland
env = __GLX_VENDOR_LIBRARY_NAME,nvidia

# Rozwiązuje problem z migotaniem (flickering) i lagami
env = GBM_BACKEND,nvidia-drm

# Naprawia błędy w aplikacjach Electron (np. VS Code, Discord)
env = ELECTRON_OZONE_PLATFORM_HINT,auto
