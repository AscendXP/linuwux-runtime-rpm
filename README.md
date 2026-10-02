# LinUwUx Runtime for openSUSE/Fedora

Standalone Linux runtime for Wine & Proton.

<p align="center">
  <a href="#installation">Installation</a>
  ·
  <a href="#usage">Usage</a>
  ·
  <a href="#faq">FAQ</a>
</p>

---

## About

**LinUwUx Runtime** is a standalone runtime rework of the functionality provided by `LinUwUx.patch`.

Instead of applying LinUwUx modifications directly to Wine and Proton, this project provides the required behavior through a preloadable Linux shared library.

The goal is to decouple the LinUwUx runtime behavior from a particular Wine or Proton source tree and make it possible to use and develop the implementation independently.

## Installation

LinUwUx Runtime is distributed as an RPM package across distinct repositories for **openSUSE** and **Fedora**.

### openSUSE

Add the OBS repository and install via `zypper`:

```sh
sudo zypper addrepo https://download.opensuse.org/repositories/home:ascendxpss/openSUSE_Tumbleweed/home:ascendxpss.repo
sudo zypper refresh
sudo zypper install linuwux-runtime
sudo usermod -aG wheel "$USER" # Integrate Polkit with AscendXP's cpuid-fault-emulation project and linuwux-runtime
```

### Fedora

Enable the COPR repository and install via `dnf`:

```sh
sudo dnf copr enable ascendxps/AscendXP
sudo dnf install linuwux-runtime
sudo usermod -aG wheel "$USER" # Integrate Polkit with AscendXP's cpuid-fault-emulation project and linuwux-runtime
```

The Fedora package is available from the [AscendXP COPR repository](https://copr.fedorainfracloud.org/coprs/ascendxps/AscendXP/).

The package installs the runtime library to:

```text
/usr/lib64/LinUwUx.so
```

After installation, use the `linuwux` launcher to start Wine, Proton, Steam, Heroic, Lutris, or other supported applications.

## Usage

### Steam

Select Proton-CachyOS or Proton-GE as the game's compatibility tool.

Open **Properties → General → Launch Options** and add:

```text
linuwux %command%
```

For runtime logging:

```text
LINUWUX_DEBUG=1 linuwux %command%
```

### Faugus Launcher

Select Proton-CachyOS or Proton-GE as the game's runner.

1. Right-click the game.
2. Select **Edit**.
3. Find **Game Arguments**.
4. Add:

```text
linuwux
```

For runtime logging:

```text
LINUWUX_DEBUG=1 linuwux
```

### Heroic Games Launcher

Select Proton-GE or another compatible community Proton build.

1. Open the game's **Settings**.
2. Select **Advanced**.
3. Find **Game Arguments**.
4. Add:

```text
linuwux
```

For runtime logging, add:

```text
Name:  LINUWUX_DEBUG
Value: 1
```

Do not put the full library path in **Game Arguments**. The `linuwux` launcher handles loading the runtime.

### Lutris

Open the game's configuration and go to:

**System options → Environment variables**

Use:

```text
Key:   LINUWUX
Value: 1
```

For runtime logging:

```text
Key:   LINUWUX_DEBUG
Value: 1
```

Alternatively, if Lutris allows command wrapping for the selected runner, use:

```text
linuwux
```

### Command line

The runtime can be started through the `linuwux` launcher:

```sh
linuwux COMMAND [ARG...]
```

For example:

```sh
linuwux wine program.exe
```

For runtime logging:

```sh
LINUWUX_DEBUG=1 linuwux COMMAND [ARG...]
```
## Credits

This project is a standalone runtime rework inspired by the original LinUwUx work.

Credits to:

- **brcly** — LinUwUx Runtime and original runtime implementation
- **LinUwUx** — original LinUwUx bypass work
- **DenuvOwO** — hypervisor bypass
- **Kurt Himebauch** — legacy Reflex / multi-protocol compatibility

For reference, the original LinUwUx Runtime repository is:

https://github.com/brcly/linuwux-runtime
