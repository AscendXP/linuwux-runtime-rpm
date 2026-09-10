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

> [!IMPORTANT]
> This project is experimental and under active development.

## Installation

LinUwUx Runtime is distributed as an RPM package across distinct repositories for **openSUSE** and **Fedora**.

### openSUSE

Add the OBS repository and install via `zypper`:

```sh
sudo zypper addrepo https://download.opensuse.org/repositories/home:ascendxpss/openSUSE_Tumbleweed/home:ascendxpss.repo

sudo zypper refresh

sudo zypper install linuwux-runtime
```

### Fedora

Enable the COPR repository and install via `dnf`:

```sh
sudo dnf copr enable ascendxps/AscendXP

sudo dnf install linuwux-runtime
```

The Fedora package is available from the [AscendXP COPR repository](https://copr.fedorainfracloud.org/coprs/ascendxps/AscendXP/).

The package installs the runtime library to:

```text
/usr/lib64/liblinuwux_runtime.so
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

## Debugging

Enable runtime logging with:

```sh
LINUWUX_DEBUG=1 linuwux COMMAND [ARG...]
```

The `LINUWUX_DEBUG` environment variable enables runtime diagnostic logging.

## FAQ

### How does the Hypervisor (HV) bypass work? What are the requirements?

**LinUwUx Runtime is a required part of the setup, but it is not the complete solution.**

This repository develops and distributes the standalone LinUwUx runtime required by the setup. The HV bypass itself, its configuration, additional requirements, and the overall setup are outside the scope of this project.

For information about the complete setup, requirements, compatibility, or troubleshooting, refer to the dedicated discussion and documentation for the wider LinUwUx project.

### Which Proton versions are supported?

The runtime primarily targets community Proton builds.

The main supported and tested environments are:

* Proton-CachyOS
* Proton-GE

Compatibility with other Wine or Proton builds may vary.

Valve's official Proton builds are currently outside the supported target and should not be assumed to work with the runtime.

### Does it require a custom Proton build?

No.

One of the main purposes of the runtime architecture is to provide LinUwUx behavior without requiring the LinUwUx modifications to be compiled directly into Wine or Proton.

A compatible Wine or Proton environment is still required to run Windows software.

### Does it patch or replace Wine or Proton?

No.

The runtime is loaded into the Linux-side process environment through the `linuwux` launcher.

It does not replace Wine or Proton binaries and does not require a patched Wine or Proton source tree.

### Is this the same as LinUwUx.patch?

No, although it implements the same LinUwUx protocol and is a rework of the behavior introduced by `LinUwUx.patch`.

The original patch implements LinUwUx through modifications to Wine and Proton. LinUwUx Runtime instead restructures the relevant behavior into a standalone shared library.

### Why use a standalone runtime?

Keeping LinUwUx behavior outside Wine and Proton reduces its coupling to a particular Wine or Proton source tree.

The implementation is divided into focused components with separate responsibilities, including:

* CPUID interception and protocol handling
* syscall redirection
* Syscall User Dispatch integration
* KUSER_SHARED_DATA handling
* faketime handling
* Wine prefix registry handling
* signal handling
* `prctl` interposition
* time-function interposition

### Which architectures are supported?

Currently, x86-64 Linux is supported.

Some runtime mechanisms are architecture-specific, including the `prctl` interposer entry point, CPUID handling, and CPU-context manipulation.

## Current implementation

The runtime currently implements core mechanisms required by the LinUwUx protocol, including:

* CPUID interception and LinUwUx command handling
* CPU vendor spoofing
* `TargetSysHandler` registration
* syscall redirection
* Syscall User Dispatch integration
* LinUwUx syscall trampoline ABI handling
* XMM4 syscall-number forwarding
* XMM5 one-shot syscall bypass handling
* KUSER_SHARED_DATA setup and patching
* faketime handling and shared faketime state
* Wine prefix `HwProfileGuid` handling
* Proton-related environment setup
* signal-handler interposition
* `prctl` interposition
* `clock_gettime` and `gettimeofday` interposition

The current implementation targets x86-64 Linux.

## Tests

Focused runtime tests are currently provided for:

* faketime CPUID behavior
* repeated faketime state updates
* syscall trampoline resume semantics
* XMM4 syscall-number forwarding
* XMM5 one-shot bypass semantics

Some test binaries must be executed from a filesystem that permits execution.

## Credits

This project is a standalone runtime rework inspired by the original LinUwUx work.

Credits to:

- **brcly** — LinUwUx Runtime and original runtime implementation
- **LinUwUx** — original LinUwUx bypass work
- **DenuvOwO** — hypervisor bypass
- **Kurt Himebauch** — legacy Reflex / multi-protocol compatibility

For reference, the original LinUwUx Runtime repository is:

https://github.com/brcly/linuwux-runtime
