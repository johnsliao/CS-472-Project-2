# CS-472-Project-2
CS 472 - Computer Architecture (Taken SUMMER 2015)

Cache simulation written in Python

1) OVERVIEW

You are to design and implement a software simulation of a cache memory subsystem.  You can use any language.   Note that any real cache is invisible to software.  This will be a simulation of the way that a real cache works.  Your "cache" will be a software structure/class  that will contain information similar (but on a smaller and more simplified scale) to what would be in a real cache.  Your "main memory" will be a 2K array.  You can make it an array of integers or shorts (16-bits), but because it is simulating a byte-addressable memory, you won't be putting any value larger than 0xFF (255 decimal or 11111111 binary) in it.  

You will provide for these two areas by defining an array for main memory and a structure/class/record (or array of these) for the cache.  
