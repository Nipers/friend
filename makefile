all : c d
d : d.cpp
	g++ d.cpp -o d
c : c.cpp
	g++ c.cpp -o c

reset :
	rm -f splines/*
	rm -f c d
