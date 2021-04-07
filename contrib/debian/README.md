
Debian
====================
This directory contains files used to package bitbridgecoind/bitbridgecoin-qt
for Debian-based Linux systems. If you compile bitbridgecoind/bitbridgecoin-qt yourself, there are some useful files here.

## bitbridgecoin: URI support ##


bitbridgecoin-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install bitbridgecoin-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your bitbridgecoin-qt binary to `/usr/bin`
and the `../../share/pixmaps/bitbridgecoin128.png` to `/usr/share/pixmaps`

bitbridgecoin-qt.protocol (KDE)

