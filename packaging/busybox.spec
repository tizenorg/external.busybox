Summary: Single binary providing simplified versions of system commands
Name: busybox
Version: 1.17.1
Release: 10
License: GPLv2
Group: Base/Tools
Source: http://www.busybox.net/downloads/%{name}-%{version}.tar.gz
Source1: busybox-dahlia.config
Source2: bin.links
Source3: sbin.links
Source4: usrbin.links
Source5: usrsbin.links
Source1001: packaging/busybox.manifest 

Patch0: 06ls.patch
Patch1: doc-man-name.patch
Patch2: shell-ash-export-HOME.patch
Patch3: applets-fallback.patch
Patch4: version.patch
Patch5: init-console.patch
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
Patch32: debian-changes-1:1.17.1-10

# SLP
Patch33: udhcpc-fast-request.patch

URL: http://www.busybox.net




%define debug_package %{nil}  

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

%package symlinks-loginutils
Group: tools
Summary: BusyBox symlinks to provide 'su'
Requires: %{name} = %{version}-%{release}

%description symlinks-loginutils
BusyBox symlinks for utilities corresponding to 'su' package.

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


%build
cp %{SOURCE1001} .
# create dynamic busybox - the executable is busybox
make defconfig
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

%files
%manifest busybox.manifest
%defattr(-,root,root,-)
%doc LICENSE 
/bin/mktemp
/bin/busybox
/bin/ash
/bin/cat
/bin/chgrp
/bin/chmod
/bin/chown
/bin/cp
/bin/date
/bin/dd
/bin/df
/bin/dnsdomainname
/bin/echo
/bin/egrep
/bin/false
/bin/fgrep
/bin/grep
/bin/gunzip
/bin/gzip
/bin/hostname
/bin/ln
/bin/ls
/bin/mkdir
/bin/mknod
/bin/more
/bin/mv
/bin/pwd
/bin/readlink
/bin/rm
/bin/rmdir
%exclude /bin/sed
/bin/sleep
/bin/stty
/bin/sync
/bin/tar
/bin/touch
/bin/true
/bin/uname
/bin/uncompress
/bin/zcat
%exclude /sbin/blkid
%exclude /sbin/blockdev
%exclude /sbin/fdisk
/sbin/fsck.minix
/sbin/getty
%exclude /sbin/hwclock
%exclude /sbin/losetup
/sbin/mkfs.minix
%exclude /sbin/mkswap
%exclude /sbin/pivot_root
%exclude /sbin/swapoff
%exclude /sbin/swapon
%exclude /sbin/switch_root
/usr/bin/[
/usr/bin/basename
%exclude /usr/bin/chrt
/usr/bin/cksum
/usr/bin/cmp
/usr/bin/comm
/usr/bin/cut
/usr/bin/diff
/usr/bin/dirname
/usr/bin/du
/usr/bin/env
/usr/bin/expand
/usr/bin/expr
/usr/bin/fdformat
%exclude /usr/bin/find
%exclude /usr/bin/flock
/usr/bin/fold
%exclude /usr/bin/getopt
/usr/bin/head
/usr/bin/hostid
/usr/bin/id
/usr/bin/install
%exclude /usr/bin/ionice
%exclude /usr/bin/ipcrm
%exclude /usr/bin/ipcs
/usr/bin/less
%exclude /usr/bin/linux32
%exclude /usr/bin/linux64
%exclude /usr/bin/logger
/usr/bin/logname
/usr/bin/md5sum
/usr/bin/mkfifo
/usr/bin/nice
/usr/bin/nohup
/usr/bin/od
/usr/bin/printenv
/usr/bin/printf
%exclude /usr/bin/renice
%exclude /usr/bin/rev
/usr/bin/rtcwake
%exclude /usr/bin/script
/usr/bin/scriptreplay
/usr/bin/seq
%exclude /usr/bin/setarch
%exclude /usr/bin/setsid
/usr/bin/sha1sum
/usr/bin/sha256sum
/usr/bin/sha512sum
/usr/bin/sort
/usr/bin/split
/usr/bin/stat
/usr/bin/sum
/usr/bin/tac
/usr/bin/tail
%exclude /usr/bin/taskset
/usr/bin/tee
/usr/bin/test
/usr/bin/timeout
/usr/bin/tr
/usr/bin/tty
/usr/bin/unexpand
/usr/bin/uniq
/usr/bin/wall
/usr/bin/wc
/usr/bin/who
/usr/bin/whoami
/usr/bin/vi
%exclude /usr/bin/xargs
/usr/bin/yes
/usr/sbin/chroot
/usr/sbin/rdev
%exclude /usr/sbin/readprofile

%files docs
%manifest busybox.manifest
%doc LICENSE docs/busybox.net/*.html

%files symlinks-adduser
%manifest busybox.manifest
/usr/sbin/addgroup
/usr/sbin/adduser
/usr/sbin/delgroup
/usr/sbin/deluser

%files symlinks-adjtimex
%manifest busybox.manifest
/usr/bin/adjtimex

%files symlinks-binutils
%manifest busybox.manifest
/usr/bin/ar
/usr/bin/strings

%files symlinks-bridge-utils
%manifest busybox.manifest
/usr/bin/brctl

%files symlinks-bsdmainutils
%manifest busybox.manifest
/usr/bin/cal
/usr/bin/hd
/usr/bin/hexdump

%files symlinks-busybox
%manifest busybox.manifest
/usr/bin/[[
/usr/bin/catv
/usr/sbin/crond
/usr/sbin/dhcprelay
/usr/sbin/dnsd
/bin/dumpkmap
/usr/bin/ether-wake
/usr/sbin/fakeidentd
/sbin/fbsplash
/bin/fsync
/usr/bin/ftpget
/usr/bin/ftpput
/usr/sbin/httpd
/sbin/ifenslave
/sbin/inotifyd
/bin/ipaddr
/bin/iplink
/bin/iproute
/bin/iprule
/usr/bin/length
/usr/bin/loadfont
/sbin/loadkmap
/sbin/logread
/sbin/makedevs
/sbin/mdev
/usr/bin/microcom
/usr/bin/nmeter
/usr/bin/pscan
/sbin/raidautorun
/usr/bin/readahead
/sbin/setconsole
/usr/sbin/tftpd
/usr/bin/ttysize
/bin/usleep
/usr/bin/volname

%files symlinks-bzip2
%manifest busybox.manifest
/bin/bunzip2
/bin/bzcat
/bin/bzip2

%files symlinks-console-tools
%manifest busybox.manifest
/usr/bin/chvt
/usr/bin/deallocvt
/bin/fgconsole
/usr/bin/kbd_mode
/usr/bin/openvt
/usr/bin/setkeycodes
/usr/bin/setlogcons
/usr/bin/showkey

%files symlinks-cpio
%manifest busybox.manifest
/bin/cpio

%files symlinks-cron
%manifest busybox.manifest
/usr/bin/crontab

%files symlinks-daemontools
%manifest busybox.manifest
/usr/bin/envdir
/usr/bin/envuidgid
/usr/bin/setuidgid
/usr/bin/softlimit

%files symlinks-dc
%manifest busybox.manifest
/usr/bin/dc

%files symlinks-dnsutils
%manifest busybox.manifest
/usr/bin/nslookup

%files symlinks-dosfstools
%manifest busybox.manifest
/sbin/mkdosfs
/sbin/mkfs.vfat

%files symlinks-ed
%manifest busybox.manifest
/bin/ed

%files symlinks-eject
%manifest busybox.manifest
/usr/bin/eject

%files symlinks-fbset
%manifest busybox.manifest
/bin/fbset

%files symlinks-fdflush
%manifest busybox.manifest
/bin/fdflush

%files symlinks-hdparm
%manifest busybox.manifest
/sbin/hdparm

%files symlinks-ifupdown
%manifest busybox.manifest
/sbin/ifdown
/sbin/ifup

%files symlinks-initscripts
%manifest busybox.manifest
/bin/mountpoint

%files symlinks-ipcalc
%manifest busybox.manifest
/usr/bin/ipcalc

%files symlinks-iproute
%manifest busybox.manifest
/bin/ip
/sbin/ip

%files symlinks-ipsvd
%manifest busybox.manifest
/usr/bin/tcpsvd
/usr/bin/udpsvd

%files symlinks-iputils-arping
%manifest busybox.manifest
/usr/bin/arping

%files symlinks-iputils-ping
%manifest busybox.manifest
/bin/ping
/bin/ping6

%files symlinks-klogd
%manifest busybox.manifest
/sbin/klogd

%files symlinks-loadlin
%manifest busybox.manifest
/usr/bin/freeramdisk

%files symlinks-lrzsz
%manifest busybox.manifest
/usr/bin/rx

%files symlinks-lzma
%manifest busybox.manifest
/usr/bin/lzcat
/usr/bin/lzma
/usr/bin/unlzma

%files symlinks-lzop
%manifest busybox.manifest
/usr/bin/lzop
/usr/bin/lzopcat
/usr/bin/unlzop

%files symlinks-module-init-tools
%manifest busybox.manifest
/sbin/depmod
/sbin/insmod
/sbin/lsmod
/sbin/modinfo
/sbin/modprobe
/sbin/rmmod

%files symlinks-mtd-utils
%manifest busybox.manifest
/usr/sbin/flash_eraseall
/usr/sbin/flash_lock
/usr/sbin/flash_unlock
/usr/sbin/flashcp
/usr/sbin/ubiattach
/usr/sbin/ubidetach

%files symlinks-net-tools
%manifest busybox.manifest
/usr/sbin/arp
/sbin/ifconfig
/sbin/iptunnel
/sbin/nameif
/bin/netstat
/sbin/route
/sbin/slattach

%files symlinks-openbsd-inetd
%manifest busybox.manifest
/usr/sbin/inetd

%files symlinks-passwd
%manifest busybox.manifest
/usr/sbin/chpasswd
/usr/bin/passwd

%files symlinks-patch
%manifest busybox.manifest
/usr/bin/patch

%files symlinks-ppp
%manifest busybox.manifest
/usr/sbin/chat

%files symlinks-procps
%manifest busybox.manifest
/usr/bin/free
/bin/kill
/usr/bin/pgrep
/usr/bin/pkill
/bin/ps
/sbin/sysctl
/usr/bin/top
/usr/bin/uptime
/usr/bin/watch

%files symlinks-psmisc
%manifest busybox.manifest
/bin/fuser
/usr/bin/killall

%files symlinks-rdate
%manifest busybox.manifest
/usr/sbin/rdate

%files symlinks-realpath
%manifest busybox.manifest
/usr/bin/realpath

#%files symlinks-rpm
#/usr/bin/rpm
#/usr/bin/rpm2cpio

%files symlinks-runit
%manifest busybox.manifest
/usr/bin/chpst
/usr/bin/runsv
/usr/bin/runsvdir
/usr/bin/sv
/usr/bin/svlogd

%files symlinks-sharutils
%manifest busybox.manifest
/usr/bin/uudecode
/usr/bin/uuencode

%files symlinks-ssmtp
%manifest busybox.manifest
/usr/sbin/sendmail

%files symlinks-sysklogd
%manifest busybox.manifest
/sbin/syslogd

%files symlinks-telnetd
%manifest busybox.manifest
/usr/sbin/telnetd

%files symlinks-tftp
%manifest busybox.manifest
/usr/bin/tftp

%files symlinks-time
%manifest busybox.manifest
/usr/bin/time

%files symlinks-tofrodos
%manifest busybox.manifest
/usr/bin/dos2unix
/usr/bin/unix2dos

%files symlinks-udhcpc
%manifest busybox.manifest
/usr/bin/udhcpc

%files symlinks-udhcpd
%manifest busybox.manifest
/usr/bin/dumpleases
/usr/sbin/udhcpd

%files symlinks-unzip
%manifest busybox.manifest
/usr/bin/unzip

%files symlinks-vlan
%manifest busybox.manifest
/sbin/vconfig

%files symlinks-vlock
%manifest busybox.manifest
/usr/bin/vlock

%files symlinks-watchdog
%manifest busybox.manifest
/usr/sbin/watchdog

%files symlinks-wget
%manifest busybox.manifest
/usr/bin/wget

%files symlinks-xterm
%manifest busybox.manifest
/usr/bin/resize

%files symlinks-zcip
%manifest busybox.manifest
/usr/bin/zcip

%files symlinks-loginutils
%manifest busybox.manifest
/bin/su
/bin/sulogin

