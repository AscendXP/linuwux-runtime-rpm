Name:           linuwux-runtime
Version:        0.1.1
Release:        0
Summary:        Standalone Linux preload runtime library for Wine and Proton
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/brcly/linuwux-runtime
Source0:        https://github.com/brcly/linuwux-runtime/archive/refs/heads/main.zip
Source1:        linuwux
ExclusiveArch:  x86_64
BuildRequires:  unzip

%description
A preloadable runtime library (liblinuwux_runtime.so) providing CPUID spoofing,
syscall redirection, and time interposition for Wine and Proton environments.

%prep
%setup -q -n linuwux-runtime-main
%build

%install
install -d -m 0755 %{buildroot}%{_libdir}
install -m 0755 liblinuwux.so %{buildroot}%{_libdir}/liblinuwux_runtime.so
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/linuwux

%post
if [ -n "$SUDO_USER" ]; then
    USER_HOME=$(getent passwd "$SUDO_USER" | cut -d: -f6)
    if [ -d "$USER_HOME" ]; then
        mkdir -p "$USER_HOME/.local/lib"
        cp --reflink=auto -f %{_libdir}/liblinuwux_runtime.so "$USER_HOME/.local/lib/liblinuwux_runtime.so"
        chown -h "$SUDO_USER:" "$USER_HOME/.local/lib/liblinuwux_runtime.so"
        chown -R "$SUDO_USER:$USER_GROUP" "$USER_HOME/.local/lib"
        chmod 0755 "$USER_HOME/.local/lib"
        chmod 0755 "$USER_HOME/.local/lib/liblinuwux_runtime.so"
    fi
fi

%postun
if [ -n "$SUDO_USER" ]; then
    USER_HOME=$(getent passwd "$SUDO_USER" | cut -d: -f6)
    TARGET_LINK="$USER_HOME/.local/lib/liblinuwux_runtime.so"
    if [ -f "$TARGET_LINK" ] || [ -L "$TARGET_LINK" ]; then
        rm -f "$TARGET_LINK"
    fi
    rmdir --ignore-fail-on-non-empty "$USER_HOME/.local/lib" 2>/dev/null || true
fi

%files
%{_libdir}/liblinuwux_runtime.so
%{_bindir}/linuwux
