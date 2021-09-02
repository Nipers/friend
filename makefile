all : c d
d : d.cpp
	/usr/bin/g++ -g /mnt/d/Fan/d.cpp -o /mnt/d/Fan/d
c : c.cpp
	/usr/bin/g++ -g /mnt/d/Fan/c.cpp -o /mnt/d/Fan/c

reset :
	rm -f splines/*
	rm -f c d
