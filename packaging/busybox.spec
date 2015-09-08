#sbs-git:slp/pkgs/b/busybox busybox 1.17.1 2af797aea95edf3accab73b53dd8075b78e75ddd
Summary: Single binary providing simplified versions of system commands
Name: busybox
Version: 1.17.1
Release: 28
License: GPLv2
Group: System/Shells
Source: http://www.busybox.net/downloads/%{name}-%{version}.tar.gz
Source1: busybox-dahlia.config
Source2: bin.links
Source3: sbin.links
Source4: usrbin.links
Source5: usrsbin.links
Source101: tizen.config
Source201: klogd.service
Source202: syslogd.service
Source1001: %{name}.manifest
Source1002: syslogd.manifest

Patch0: 06ls.patch
Patch1: doc-man-name.patch
Patch2: shell-ash-export-HOME.patch
Patch3: applets-fallback.patch
Patch4: version.patch
Patch5: init-console.patch
#Patch6: 05thumb.dpatch
#Patch7: 06ls.patch
Patch8: busybox-zero-ifr.ifr_hwaddr.sa_data.patch
Patch9: top-display-rss.patch
Patch10: strip.patch
Patch11: make_gen_build_files_skip_quilt.patch

# The following patches have been merged upstream and will be in version 1.18
Patch12: readlink-use-xmalloc_realpath.patch
Patch13: mark-Linux-specific-configuration-options.patch
Patch14: init-loginutils-termios-portability-fixes.patch
Patch15: init-halt-portability-improvements.patch
Patch16: init-make-the-initial-TERM-value-configurable.patch
Patch17: libbb.h-add-device-names-for-Hurd-and-FreeBSD.patch
Patch18: mkdir-fix-p-on-FreeBSD.patch
Patch19: libbb-conditionalize-AF_-usage-in-error-reporting.patch
Patch20: tcpsvd-udpsvd-conditionalize-usage-of-SO_ORIGINAL_DS.patch
Patch21: less-remove-misguided-dependency-on-PLATFORM_LINUX.patch
Patch22: bootchartd-mounting-tmpfs-is-Linux-specific.patch
Patch23: vlock-disable-linux-console-calls-on-other-systems.patch
Patch24: cttyhack-serial-console-detection-is-Linux-specific.patch
Patch25: klogd-make-it-work-on-non-linux-systems.patch
Patch26: stty-sort-out-preprocessor-conditionals.patch
Patch27: update-scripts-kconfig-_shipped.patch
Patch28: blockdev.patch

# The following patches will likely be merged soon
Patch29: u-mount-FreeBSD-support.patch
Patch30: swaponoff-FreeBSD-support.patch

# not sent upstream
Patch31: init-console-CRTSCTS.patch
Patch32: debian-changes-1.17.1-10

# SLP
Patch33: udhcpc-fast-request.patch
Patch34: smack-busybox-1.17.1.patch
Patch35: smack-conflict-with-selinux.patch
Patch36: make_unicode_printable.patch

# The following patches have been merged upstream and will be in version 1.20
Patch37: busybox-1.20.2-fix-resource-h-failure.patch

Patch100: busybox-1.17.1-make.patch
Patch101: sysinfo-multiple-define-error-fix.patch

Patch999: syslogd-disable-systemd-sa.patch

URL: http://www.busybox.net

BuildRequires: pkgconfig(libsystemd-daemon)

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

%package docs
Group: Documentation
Summary: Busybox Documentation

%description docs
Busybox documentation and user guides

%package symlinks-busybox
Group: tools
Summary: BusyBox specific symlinks
Requires: %{name} = %{version}-%{release}

%description symlinks-busybox
 BusyBox symlinks for utilities without counterparts in Debian.
 These are in separate package because they aren't essentials
 (e.g. needed for system package upgrades).

%package symlinks-adduser
Group: tools
Summary: BusyBox symlinks to provide 'adduser'
Requires: %{name} = %{version}-%{release}

%description symlinks-adduser
BusyBox symlinks for utilities corresponding to 'adduser' package.

%package symlinks-adjtimex
Group: tools
Summary: BusyBox symlinks to provide 'adjtimex'
Requires: %{name} = %{version}-%{release}

%description symlinks-adjtimex
BusyBox symlinks for utilities corresponding to 'adjtimex' package.

%package symlinks-binutils
Group: tools
Summary: BusyBox symlinks to provide 'binutils'
Requires: %{name} = %{version}-%{release}

%description symlinks-binutils
BusyBox symlinks for utilities corresponding to 'binutils' package.

%package symlinks-bridge-utils
Group: tools
Summary: BusyBox symlinks to provide 'bridge-utils'

%description symlinks-bridge-utils
BusyBox symlinks for utilities corresponding to 'bridge-utils' package.

%package symlinks-bsdmainutils
Group: tools
Summary: BusyBox symlinks to provide 'bsdmainutils'
Requires: %{name} = %{version}-%{release}

%description symlinks-bsdmainutils
BusyBox symlinks for utilities corresponding to 'bsdmainutils' package.

%package symlinks-bzip2
Group: tools
Summary: BusyBox symlinks to provide 'bzip2'
Requires: %{name} = %{version}-%{release}

%description symlinks-bzip2
BusyBox symlinks for utilities corresponding to 'bzip2' package.

%package symlinks-console-tools
Group: tools
Summary: BusyBox symlinks to provide 'console-tools'
Requires: %{name} = %{version}-%{release}

%description symlinks-console-tools
BusyBox symlinks for utilities corresponding to 'console-tools' package.

%package symlinks-cpio
Group: tools
Summary: BusyBox symlinks to provide 'cpio'
Requires: %{name} = %{version}-%{release}

%description symlinks-cpio
BusyBox symlinks for utilities corresponding to 'cpio' package.

%package symlinks-cron
Group: tools
Summary: BusyBox symlinks to provide 'cron'
Requires: %{name} = %{version}-%{release}

%description symlinks-cron
BusyBox symlinks for utilities corresponding to 'cron' package.

%package symlinks-daemontools
Group: tools
Summary: BusyBox symlinks to provide 'daemontools'
Requires: %{name} = %{version}-%{release}

%description symlinks-daemontools
BusyBox symlinks for utilities corresponding to 'daemontools' package.

%package symlinks-dc
Group: tools
Summary: BusyBox symlinks to provide 'dc'
Requires: %{name} = %{version}-%{release}

%description symlinks-dc
BusyBox symlinks for utilities corresponding to 'dc' package.

%package symlinks-dnsutils
Group: tools
Summary: BusyBox symlinks to provide 'dnsutils'
Requires: %{name} = %{version}-%{release}

%description symlinks-dnsutils
BusyBox symlinks for utilities corresponding to 'dnsutils' package.

%package symlinks-dosfstools
Group: tools
Summary: BusyBox symlinks to provide 'dosfstools'
Requires: %{name} = %{version}-%{release}

%description symlinks-dosfstools
BusyBox symlinks for utilities corresponding to 'dosfstools' package.

%package symlinks-ed
Group: tools
Summary: BusyBox symlinks to provide 'ed'
Requires: %{name} = %{version}-%{release}

%description symlinks-ed
BusyBox symlinks for utilities corresponding to 'ed' package.

%package symlinks-eject
Group: tools
Summary: BusyBox symlinks to provide 'eject'
Requires: %{name} = %{version}-%{release}

%description symlinks-eject
BusyBox symlinks for utilities corresponding to 'eject' package.

%package symlinks-fbset
Group: tools
Summary: BusyBox symlinks to provide 'fbset'
Requires: %{name} = %{version}-%{release}

%description symlinks-fbset
BusyBox symlinks for utilities corresponding to 'fbset' package.

%package symlinks-fdflush
Group: tools
Summary: BusyBox symlinks to provide 'fdflush'
Requires: %{name} = %{version}-%{release}

%description symlinks-fdflush
BusyBox symlinks for utilities corresponding to 'fdflush' package.

%package symlinks-hdparm
Group: tools
Summary: BusyBox symlinks to provide 'hdparm'
Requires: %{name} = %{version}-%{release}

%description symlinks-hdparm
BusyBox symlinks for utilities corresponding to 'hdparm' package.

%package symlinks-ifupdown
Group: tools
Summary: BusyBox symlinks to provide 'ifupdown'
Requires: %{name} = %{version}-%{release}

%description symlinks-ifupdown
BusyBox symlinks for utilities corresponding to 'ifupdown' package.

%package symlinks-initscripts
Group: tools
Summary: BusyBox symlinks to provide 'initscripts'
Requires: %{name} = %{version}-%{release}

%description symlinks-initscripts
BusyBox symlinks for utilities corresponding to 'initscripts' package.

%package symlinks-ipcalc
Group: tools
Summary: BusyBox symlinks to provide 'ipcalc'
Requires: %{name} = %{version}-%{release}

%description symlinks-ipcalc
BusyBox symlinks for utilities corresponding to 'ipcalc' package.

%package symlinks-iproute
Group: tools
Summary: BusyBox symlinks to provide 'iproute'
Requires: %{name} = %{version}-%{release}

%description symlinks-iproute
BusyBox symlinks for utilities corresponding to 'iproute' package.

%package symlinks-ipsvd
Group: tools
Summary: BusyBox symlinks to provide 'ipsvd'
Requires: %{name} = %{version}-%{release}

%description symlinks-ipsvd
BusyBox symlinks for utilities corresponding to 'ipsvd' package.

%package symlinks-iputils-arping
Group: tools
Summary: BusyBox symlinks to provide 'iputils-arping'
Requires: %{name} = %{version}-%{release}

%description symlinks-iputils-arping
BusyBox symlinks for utilities corresponding to 'iputils-arping' package.

%package symlinks-iputils-ping
Group: tools
Summary: BusyBox symlinks to provide 'iputils-ping'
Requires: %{name} = %{version}-%{release}

%description symlinks-iputils-ping
BusyBox symlinks for utilities corresponding to 'iputils-ping' package.

%package symlinks-klogd
Group: tools
Summary: BusyBox symlinks to provide 'klogd'
Requires: %{name} = %{version}-%{release}

%description symlinks-klogd
BusyBox symlinks for utilities corresponding to 'klogd' package.

%package symlinks-loadlin
Group: tools
Summary: BusyBox symlinks to provide 'loadlin'
Requires: %{name} = %{version}-%{release}

%description symlinks-loadlin
BusyBox symlinks for utilities corresponding to 'loadlin' package.

%package symlinks-lrzsz
Group: tools
Summary: BusyBox symlinks to provide 'lrzsz'
Requires: %{name} = %{version}-%{release}

%description symlinks-lrzsz
BusyBox symlinks for utilities corresponding to 'lrzsz' package.

%package symlinks-lzma
Group: tools
Summary: BusyBox symlinks to provide 'lzma'
Requires: %{name} = %{version}-%{release}

%description symlinks-lzma
BusyBox symlinks for utilities corresponding to 'lzma' package.

%package symlinks-lzop
Group: tools
Summary: BusyBox symlinks to provide 'lzop'
Requires: %{name} = %{version}-%{release}

%description symlinks-lzop
BusyBox symlinks for utilities corresponding to 'lzop' package.

%package symlinks-module-init-tools
Group: tools
Summary: BusyBox symlinks to provide 'module-init-tools'
Requires: %{name} = %{version}-%{release}

%description symlinks-module-init-tools
BusyBox symlinks for utilities corresponding to 'module-init-tools' package.

%package symlinks-mtd-utils
Group: tools
Summary: BusyBox symlinks to provide 'mtd-utils'
Requires: %{name} = %{version}-%{release}

%description symlinks-mtd-utils
BusyBox symlinks for utilities corresponding to 'mtd-utils' package.

%package symlinks-net-tools
Group: tools
Summary: BusyBox symlinks to provide 'net-tools'
Requires: %{name} = %{version}-%{release}

%description symlinks-net-tools
BusyBox symlinks for utilities corresponding to 'net-tools' package.

%package symlinks-openbsd-inetd
Group: tools
Summary: BusyBox symlinks to provide 'openbsd-inetd'
Requires: %{name} = %{version}-%{release}

%description symlinks-openbsd-inetd
BusyBox symlinks for utilities corresponding to 'openbsd-inetd' package.

%package symlinks-passwd
Group: tools
Summary: BusyBox symlinks to provide 'passwd'
Requires: %{name} = %{version}-%{release}

%description symlinks-passwd
BusyBox symlinks for utilities corresponding to 'passwd' package.

%package symlinks-patch
Group: tools
Summary: BusyBox symlinks to provide 'patch'
Requires: %{name} = %{version}-%{release}

%description symlinks-patch
BusyBox symlinks for utilities corresponding to 'patch' package.

%package symlinks-ppp
Group: tools
Summary: BusyBox symlinks to provide 'ppp'
Requires: %{name} = %{version}-%{release}

%description symlinks-ppp
BusyBox symlinks for utilities corresponding to 'ppp' package.

%package symlinks-procps
Group: tools
Summary: BusyBox symlinks to provide 'procps'
Requires: %{name} = %{version}-%{release}

%description symlinks-procps
BusyBox symlinks for utilities corresponding to 'procps' package.

%package symlinks-psmisc
Group: tools
Summary: BusyBox symlinks to provide 'psmisc'
Requires: %{name} = %{version}-%{release}

%description symlinks-psmisc
BusyBox symlinks for utilities corresponding to 'psmisc' package.

%package symlinks-rdate
Group: tools
Summary: BusyBox symlinks to provide 'rdate'
Requires: %{name} = %{version}-%{release}

%description symlinks-rdate
BusyBox symlinks for utilities corresponding to 'rdate' package.

%package symlinks-realpath
Group: tools
Summary: BusyBox symlinks to provide 'realpath'
Requires: %{name} = %{version}-%{release}

%description symlinks-realpath
BusyBox symlinks for utilities corresponding to 'realpath' package.

%package symlinks-runit
Group: tools
Summary: BusyBox symlinks to provide 'runit'
Requires: %{name} = %{version}-%{release}

%description symlinks-runit
BusyBox symlinks for utilities corresponding to 'runit' package.

%package symlinks-sharutils
Group: tools
Summary: BusyBox symlinks to provide 'sharutils'
Requires: %{name} = %{version}-%{release}

%description symlinks-sharutils
BusyBox symlinks for utilities corresponding to 'sharutils' package.

%package symlinks-ssmtp
Group: tools
Summary: BusyBox symlinks to provide 'ssmtp'
Requires: %{name} = %{version}-%{release}

%description symlinks-ssmtp
BusyBox symlinks for utilities corresponding to 'ssmtp' package.

%package symlinks-sysklogd
Group: tools
Summary: BusyBox symlinks to provide 'sysklogd'
Requires: %{name} = %{version}-%{release}

%description symlinks-sysklogd
BusyBox symlinks for utilities corresponding to 'sysklogd' package.

%package symlinks-telnetd
Group: tools
Summary: BusyBox symlinks to provide 'telnetd'
Requires: %{name} = %{version}-%{release}

%description symlinks-telnetd
BusyBox symlinks for utilities corresponding to 'telnetd' package.

%package symlinks-tftp
Group: tools
Summary: BusyBox symlinks to provide 'tftp'
Requires: %{name} = %{version}-%{release}

%description symlinks-tftp
BusyBox symlinks for utilities corresponding to 'tftp' package.

%package symlinks-time
Group: tools
Summary: BusyBox symlinks to provide 'time'
Requires: %{name} = %{version}-%{release}

%description symlinks-time
BusyBox symlinks for utilities corresponding to 'time' package.

%package symlinks-tofrodos
Group: tools
Summary: BusyBox symlinks to provide 'tofrodos'
Requires: %{name} = %{version}-%{release}

%description symlinks-tofrodos
BusyBox symlinks for utilities corresponding to 'tofrodos' package.

%package symlinks-udhcpc
Group: tools
Summary: BusyBox symlinks to provide 'udhcpc'
Requires: %{name} = %{version}-%{release}

%description symlinks-udhcpc
BusyBox symlinks for utilities corresponding to 'udhcpc' package.

%package symlinks-udhcpd
Group: tools
Summary: BusyBox symlinks to provide 'udhcpd'
Requires: %{name} = %{version}-%{release}

%description symlinks-udhcpd
BusyBox symlinks for utilities corresponding to 'udhcpd' package.

%package symlinks-unzip
Group: tools
Summary: BusyBox symlinks to provide 'unzip'
Requires: %{name} = %{version}-%{release}

%description symlinks-unzip
BusyBox symlinks for utilities corresponding to 'unzip' package.

%package symlinks-vlan
Group: tools
Summary: BusyBox symlinks to provide 'vlan'
Requires: %{name} = %{version}-%{release}

%description symlinks-vlan
BusyBox symlinks for utilities corresponding to 'vlan' package.

%package symlinks-vlock
Group: tools
Summary: BusyBox symlinks to provide 'vlock'
Requires: %{name} = %{version}-%{release}

%description symlinks-vlock
BusyBox symlinks for utilities corresponding to 'vlock' package.

%package symlinks-watchdog
Group: tools
Summary: BusyBox symlinks to provide 'watchdog'
Requires: %{name} = %{version}-%{release}

%description symlinks-watchdog
BusyBox symlinks for utilities corresponding to 'watchdog' package.

%package symlinks-wget
Group: tools
Summary: BusyBox symlinks to provide 'wget'
Requires: %{name} = %{version}-%{release}

%description symlinks-wget
BusyBox symlinks for utilities corresponding to 'wget' package.

%package symlinks-xterm
Group: tools
Summary: BusyBox symlinks to provide 'xterm'
Requires: %{name} = %{version}-%{release}

%description symlinks-xterm
BusyBox symlinks for utilities corresponding to 'xterm' package.

%package symlinks-zcip
Group: tools
Summary: BusyBox symlinks to provide 'zcip'
Requires: %{name} = %{version}-%{release}

%description symlinks-zcip
BusyBox symlinks for utilities corresponding to 'zcip' package.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
#%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch36 -p1
%patch37 -p1

%patch100 -p1
%patch101 -p1

%patch999 -p1

%build
cp %{SOURCE1001} .
cp %{SOURCE1002} .
# create dynamic busybox - the executable is busybox
cp %{SOURCE101} .config
make oldconfig
make CC="gcc $RPM_OPT_FLAGS"
cp busybox busybox-dynamic

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
install -m 755 busybox-dynamic $RPM_BUILD_ROOT/bin/busybox

# debian/busybox.links
pushd %{buildroot}
mkdir -p usr/bin usr/sbin sbin
cd bin
for f in `cat %SOURCE2` ; do ln -s busybox $f ; done
cd ../sbin
for f in `cat %SOURCE3` ; do ln -s ../bin/busybox $f ; done
cd ../usr/bin
for f in `cat %SOURCE4` ; do ln -s ../../bin/busybox $f ; done
cd ../../usr/sbin
for f in `cat %SOURCE5` ; do ln -s ../../bin/busybox $f ; done
popd

# install systemd service files for syslogd and klogd
mkdir -p %{buildroot}%{_libdir}/systemd/system
mkdir -p %{buildroot}%{_libdir}/systemd/system/basic.target.wants
install -m 644 %SOURCE201 %{buildroot}%{_libdir}/systemd/system/klogd.service
ln -s ../klogd.service %{buildroot}%{_libdir}/systemd/system/basic.target.wants/klogd.service
install -m 644 %SOURCE202 %{buildroot}%{_libdir}/systemd/system/syslogd.service
ln -s ../syslogd.service %{buildroot}%{_libdir}/systemd/system/basic.target.wants/syslogd.service

rm -rf $RPM_BUILD_ROOT/sbin/syslogd
cp -f $RPM_BUILD_ROOT/bin/busybox $RPM_BUILD_ROOT/sbin/syslogd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
for keyword in LICENSE COPYING COPYRIGHT;
do
	for file in `find %{_builddir} -name $keyword`;
	do
		cat $file >> $RPM_BUILD_ROOT%{_datadir}/license/%{name};
		echo "";
	done;
done

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%doc LICENSE
%{_datadir}/license/%{name}
%exclude /bin/mktemp
/bin/busybox
%exclude /bin/ash
%exclude /bin/cat
%exclude /bin/chgrp
%exclude /bin/chmod
%exclude /bin/chown
%exclude /bin/cp
%exclude /bin/date
%exclude /bin/dd
%exclude /bin/df
%exclude /bin/dmesg
%exclude /bin/dnsdomainname
%exclude /bin/echo
%exclude /bin/egrep
%exclude /bin/false
%exclude /bin/fgrep
%exclude /bin/grep
%exclude /bin/gunzip
%exclude /bin/gzip
%exclude /bin/hostname
%exclude /bin/ln
%exclude /bin/ls
%exclude /bin/mkdir
%exclude /bin/mknod
%exclude /bin/more
%exclude /bin/mount
%exclude /bin/mv
%exclude /bin/pwd
%exclude /bin/readlink
%exclude /bin/rm
%exclude /bin/rmdir
%exclude /bin/sed
#/bin/sh
%exclude /bin/sleep
%exclude /bin/stty
%exclude /bin/sync
%exclude /bin/tar
%exclude /bin/touch
%exclude /bin/true
%exclude /bin/umount
%exclude /bin/uname
%exclude /bin/uncompress
%exclude /bin/zcat
%exclude /sbin/blkid
%exclude /sbin/blockdev
%exclude /sbin/fdisk
%exclude /sbin/fsck.minix
%exclude /sbin/getty
%exclude /sbin/hwclock
%exclude /sbin/losetup
%exclude /sbin/mkfs.minix
%exclude /sbin/mkswap
%exclude /sbin/pivot_root
%exclude /sbin/swapoff
%exclude /sbin/swapon
%exclude /sbin/switch_root
%exclude /usr/bin/[
%exclude /usr/bin/basename
%exclude /usr/bin/chrt
%exclude /usr/bin/cksum
%exclude /usr/bin/cmp
%exclude /usr/bin/comm
%exclude /usr/bin/cut
%exclude /usr/bin/diff
%exclude /usr/bin/dirname
%exclude /usr/bin/du
%exclude /usr/bin/env
%exclude /usr/bin/expand
%exclude /usr/bin/expr
%exclude /usr/bin/fdformat
%exclude /usr/bin/find
%exclude /usr/bin/flock
%exclude /usr/bin/fold
%exclude /usr/bin/getopt
%exclude /usr/bin/head
%exclude /usr/bin/hostid
%exclude /usr/bin/id
%exclude /usr/bin/install
%exclude /usr/bin/ionice
%exclude /usr/bin/ipcrm
%exclude /usr/bin/ipcs
%exclude /usr/bin/less
%exclude /usr/bin/linux32
%exclude /usr/bin/linux64
%exclude /usr/bin/logger
%exclude /usr/bin/logname
%exclude /usr/bin/md5sum
%exclude /usr/bin/mkfifo
%exclude /usr/bin/nice
%exclude /usr/bin/nohup
%exclude /usr/bin/od
%exclude /usr/bin/printenv
%exclude /usr/bin/printf
%exclude /usr/bin/renice
%exclude /usr/bin/rev
%exclude /usr/bin/rtcwake
%exclude /usr/bin/script
%exclude /usr/bin/scriptreplay
%exclude /usr/bin/seq
%exclude /usr/bin/setarch
%exclude /usr/bin/setsid
%exclude /usr/bin/sha1sum
%exclude /usr/bin/sha256sum
%exclude /usr/bin/sha512sum
%exclude /usr/bin/sort
%exclude /usr/bin/split
%exclude /usr/bin/stat
%exclude /usr/bin/sum
%exclude /usr/bin/tac
%exclude /usr/bin/tail
%exclude /usr/bin/taskset
%exclude /usr/bin/tee
%exclude /usr/bin/test
%exclude /usr/bin/timeout
%exclude /usr/bin/tr
%exclude /usr/bin/tty
%exclude /usr/bin/unexpand
%exclude /usr/bin/uniq
%exclude /usr/bin/wall
%exclude /usr/bin/wc
%exclude /usr/bin/who
%exclude /usr/bin/whoami
/usr/bin/vi
%exclude /usr/bin/xargs
%exclude /usr/bin/yes
%exclude /usr/sbin/chroot
%exclude /usr/sbin/rdev
%exclude /usr/sbin/readprofile

%files docs
%doc LICENSE docs/busybox.net/*.html

%files symlinks-adduser
%exclude /usr/sbin/addgroup
%exclude /usr/sbin/adduser
%exclude /usr/sbin/delgroup
%exclude /usr/sbin/deluser

%files symlinks-adjtimex
%exclude /usr/bin/adjtimex

%files symlinks-binutils
%exclude /usr/bin/ar
%exclude /usr/bin/strings

%files symlinks-bridge-utils
%exclude /usr/bin/brctl

%files symlinks-bsdmainutils
%exclude /usr/bin/cal
%exclude /usr/bin/hd
%exclude /usr/bin/hexdump

%files symlinks-busybox
%manifest %{name}.manifest
%exclude /usr/bin/[[
%exclude /usr/bin/catv
%exclude /usr/sbin/crond
%exclude /usr/sbin/dhcprelay
%exclude /usr/sbin/dnsd
%exclude /bin/dumpkmap
%exclude /usr/bin/ether-wake
%exclude /usr/sbin/fakeidentd
%exclude /sbin/fbsplash
%exclude /bin/fsync
%exclude /usr/bin/ftpget
%exclude /usr/bin/ftpput
%exclude /usr/sbin/httpd
%exclude /sbin/ifenslave
%exclude /sbin/inotifyd
%exclude /bin/ipaddr
%exclude /bin/iplink
%exclude /bin/iproute
%exclude /bin/iprule
%exclude /usr/bin/length
%exclude /usr/bin/loadfont
%exclude /sbin/loadkmap
%exclude /sbin/logread
%exclude /sbin/makedevs
%exclude /sbin/mdev
%exclude /usr/bin/microcom
%exclude /usr/bin/nmeter
%exclude /usr/bin/pscan
%exclude /sbin/raidautorun
%exclude /usr/bin/readahead
%exclude /sbin/setconsole
%exclude /usr/sbin/tftpd
%exclude /usr/bin/ttysize
%exclude /bin/usleep
%exclude /usr/bin/volname

%files symlinks-bzip2
%exclude /bin/bunzip2
%exclude /bin/bzcat
%exclude /bin/bzip2

%files symlinks-console-tools
%exclude /usr/bin/chvt
%exclude /usr/bin/deallocvt
%exclude /bin/fgconsole
%exclude /usr/bin/kbd_mode
%exclude /usr/bin/openvt
%exclude /usr/bin/setkeycodes
%exclude /usr/bin/setlogcons
%exclude /usr/bin/showkey

%files symlinks-cpio
%exclude /bin/cpio

%files symlinks-cron
%exclude /usr/bin/crontab

%files symlinks-daemontools
%exclude /usr/bin/envdir
%exclude /usr/bin/envuidgid
%exclude /usr/bin/setuidgid
%exclude /usr/bin/softlimit

%files symlinks-dc
%exclude /usr/bin/dc

%files symlinks-dnsutils
%manifest %{name}.manifest
%exclude /usr/bin/nslookup

%files symlinks-dosfstools
%exclude /sbin/mkdosfs
%exclude /sbin/mkfs.vfat

%files symlinks-ed
%exclude /bin/ed

%files symlinks-eject
%exclude /usr/bin/eject

%files symlinks-fbset
%exclude /bin/fbset

%files symlinks-fdflush
%exclude /bin/fdflush

%files symlinks-hdparm
%exclude /sbin/hdparm

%files symlinks-ifupdown
%manifest %{name}.manifest
%exclude /sbin/ifdown
%exclude /sbin/ifup

%files symlinks-initscripts
%exclude /bin/mountpoint

%files symlinks-ipcalc
%exclude /usr/bin/ipcalc

%files symlinks-iproute
%exclude /bin/ip
%exclude /sbin/ip

%files symlinks-ipsvd
%exclude /usr/bin/tcpsvd
%exclude /usr/bin/udpsvd

%files symlinks-iputils-arping
%exclude /usr/bin/arping

%files symlinks-iputils-ping
%manifest %{name}.manifest
%exclude /bin/ping
%exclude /bin/ping6

%files symlinks-klogd
%manifest %{name}.manifest
%exclude /sbin/klogd
%exclude %{_libdir}/systemd/system/klogd.service
%exclude %{_libdir}/systemd/system/basic.target.wants/klogd.service

%files symlinks-loadlin
%exclude /usr/bin/freeramdisk

%files symlinks-lrzsz
%exclude /usr/bin/rx

%files symlinks-lzma
%exclude /usr/bin/lzcat
%exclude /usr/bin/lzma
%exclude /usr/bin/unlzma

%files symlinks-lzop
%exclude /usr/bin/lzop
%exclude /usr/bin/lzopcat
%exclude /usr/bin/unlzop

%files symlinks-module-init-tools
%exclude /sbin/depmod
%exclude /sbin/insmod
%exclude /sbin/lsmod
%exclude /sbin/modinfo
%exclude /sbin/modprobe
%exclude /sbin/rmmod

%files symlinks-mtd-utils
%exclude /usr/sbin/flash_eraseall
%exclude /usr/sbin/flash_lock
%exclude /usr/sbin/flash_unlock
%exclude /usr/sbin/flashcp
%exclude /usr/sbin/ubiattach
%exclude /usr/sbin/ubidetach

%files symlinks-net-tools
%exclude /usr/sbin/arp
%exclude /sbin/ifconfig
%exclude /sbin/iptunnel
%exclude /sbin/nameif
%exclude /bin/netstat
%exclude /sbin/route
%exclude /sbin/slattach

%files symlinks-openbsd-inetd
%exclude /usr/sbin/inetd

%files symlinks-passwd
%exclude /usr/sbin/chpasswd
%exclude /usr/bin/passwd

%files symlinks-patch
%exclude /usr/bin/patch

%files symlinks-ppp
%exclude /usr/sbin/chat

%files symlinks-procps
%exclude /usr/bin/free
%exclude /bin/kill
%exclude /usr/bin/pgrep
%exclude /usr/bin/pkill
%exclude /bin/ps
%exclude /sbin/sysctl
%exclude /usr/bin/top
%exclude /usr/bin/uptime
%exclude /usr/bin/watch

%files symlinks-psmisc
%exclude /bin/fuser
%exclude /usr/bin/killall

%files symlinks-rdate
%exclude /usr/sbin/rdate

%files symlinks-realpath
%exclude /usr/bin/realpath

#%files symlinks-rpm
#/usr/bin/rpm
#/usr/bin/rpm2cpio

%files symlinks-runit
%exclude /usr/bin/chpst
%exclude /usr/bin/runsv
%exclude /usr/bin/runsvdir
%exclude /usr/bin/sv
%exclude /usr/bin/svlogd

%files symlinks-sharutils
%exclude /usr/bin/uudecode
%exclude /usr/bin/uuencode

%files symlinks-ssmtp
%exclude /usr/sbin/sendmail

%files symlinks-sysklogd
%exclude /sbin/syslogd
%exclude %{_libdir}/systemd/system/syslogd.service
%exclude %{_libdir}/systemd/system/basic.target.wants/syslogd.service

%files symlinks-telnetd
%exclude /usr/sbin/telnetd

%files symlinks-tftp
%exclude /usr/bin/tftp

%files symlinks-time
%exclude /usr/bin/time

%files symlinks-tofrodos
%exclude /usr/bin/dos2unix
%exclude /usr/bin/unix2dos

%files symlinks-udhcpc
%exclude /usr/bin/udhcpc

%files symlinks-udhcpd
%exclude /usr/bin/dumpleases
%exclude /usr/sbin/udhcpd

%files symlinks-unzip
%exclude /usr/bin/unzip

%files symlinks-vlan
%exclude /sbin/vconfig

%files symlinks-vlock
%exclude /usr/bin/vlock

%files symlinks-watchdog
%exclude /usr/sbin/watchdog

%files symlinks-wget
%exclude /usr/bin/wget

%files symlinks-xterm
%exclude /usr/bin/resize

%files symlinks-zcip
%exclude /usr/bin/zcip
