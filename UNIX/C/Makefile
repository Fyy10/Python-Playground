all: mtest

mtest: cosine.o, sine.o, add.o
	gcc cosine.o sine.o add.o -o mtest

cosine.o: cosine.c
	gcc -c cosine.c

cosine.c: cosine.h

cosine.h: mlibi.h

sine.o: sine.c
	gcc -c sine.c

sine.c: sine.h

sine.h: mlib.h

add.o: add.c
	gcc -c add.c

add.c: add.h

add.h: mlib.h

