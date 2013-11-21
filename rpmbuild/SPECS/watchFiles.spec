Name:           watchFiles
Version:        1.0
Release:        0
Summary:        Watch directories and report changes
License:        GPLv3+
Source:         %{name}.tar.gz

%description
Watch directories and report changes. By default /bin, /sbin, /usr/bin and
/usr/sbin will be watched. The status of each directory will be saved in
/var/tmp and changes be reported in /var/log/syschecker. The status consists
of added and deleted files, changed ownership, permissions, size or content.

%prep
%setup -n %{name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
cp watchFiles $RPM_BUILD_ROOT/usr/bin
cp watchFiles.1 $RPM_BUILD_ROOT/usr/share/man/man1

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

%files
%{_mandir}/man1/watchFiles.1.gz
%{_bindir}/watchFiles

%changelog
* Tue Nov 21 2013 Lutz <dgf@iera.de> 1.0-0
- Initial version of the package
