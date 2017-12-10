# caja-git

Caja extension to add important information about the current git directory.
This project is based on [nautilus-git by Bilal Elmoussaoui](https://github.com/bil-elmoussaoui/nautilus-git).

## Requirements:

### Running dependencies

- `python2`
- `git`
- `caja-python` or `python2-caja` >= 1.17.0



### Building dependencies

- `meson`
- `ninja`
- `intltool`
- `gtk+-3.0`
- `gobject-introspection`:
  - Debian/Ubuntu : `libgirepository1.0-dev`
  - Fedora : `gobject-introspection-devel`
  - Archlinux :  `gobject-introspection`

### Manual installation

1- Install requirements

2- Clone the repository

```bash
git clone https://github.com/darkshram/caja-git
```

3- Build it!

```bash
cd caja-git
mkdir build
cd build
meson .. --prefix /usr -Dfile_manager=caja
sudo ninja install
```


4- Restart Caja

```bash
caja -q
```

## How to uninstall

1- Download the uninstall script.

```bash
cd /tmp && wget -O uninstall.sh https://raw.githubusercontent.com/darkshram/caja-git/master/uninstall.sh
```

2- Make the file executable

```bash
chmod +x ./uninstall.sh
```

3- Run it!

```bash
sudo ./uninstall.sh /usr
```

PS : Replace `/usr` with whatever installation prefix you have chosen before.

## Credits

- Code was originally written by Bilal Elmoussaoui.
- The `caja-git-symbolic` icon was designed by gitg design team.

## Screenshots


![Caja main window](screenshots/screenshot1.png?raw=true "Caja main window")

![Compare commits](screenshots/screenshot2.png?raw=true "Compare commits")

![Changes detected](screenshots/screenshot3.png?raw=true "Changes detected")

![New files detected](screenshots/screenshot4.png?raw=true "New files detected")

![Caja Git tab in properties window](screenshots/screenshot5.png?raw=true "Caja Git tab in properties window")

![Compare commits](screenshots/screenshot6.png?raw=true "Compare commits")

