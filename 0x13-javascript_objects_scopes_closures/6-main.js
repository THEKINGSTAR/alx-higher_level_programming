#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');


const s2 = new Square(3);
s2.charPrint('O');

s2.charPrint('D');

/*
guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$
*/
