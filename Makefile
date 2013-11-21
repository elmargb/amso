all: install

install:
	cp watchFiles /usr/bin/watchFiles
	cp watchFiles.1 /usr/share/man/man1/

uninstall:
	rm /usr/bin/watchFiles
	rm /usr/share/man/man1/watchFiles.1
