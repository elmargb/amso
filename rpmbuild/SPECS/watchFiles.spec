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
mkdir -p $RPM_BUILD_ROOT/var/log
cp watchFiles $RPM_BUILD_ROOT/usr/bin
cp watchFiles.1 $RPM_BUILD_ROOT/usr/share/man/man1
cp syschecker $RPM_BUILD_ROOT/var/log

%clean
rm -rf $RPM_BUILD_ROOT/../../tmp/%{name}
rm -rf $RPM_BUILD_ROOT/../../BUILD/%{name}
rm -rf $RPM_BUILD_ROOT

%files
%{_mandir}/man1/watchFiles.1.gz
%{_bindir}/watchFiles
%attr(666, root, root) /var/log/syschecker

%changelog
* Tue Nov 21 2013 Lutz <dgf@iera.de> 1.0-0
- Initial version of the package
