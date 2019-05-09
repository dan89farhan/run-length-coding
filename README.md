# run-length-coding

this is the python code for run length encoding and decoding.
I wrote this code to compress the data. Run length coding is very simple to implement and give much higher ratio compression.

Logic is very simple

To compress the message we must find the codeword.

there are two types of codewords:
# (1) Fixed-length codeword:
a fixed-length codeword consists of
a prefix and a fixed number of tail bits. Fixed-length code-
words are used to address runs with the length L < 4. The
prefix of the codeword is fixed to bit 0. Beginning with the
first bit of the run, a fixed number of sequential bits is
extracted from the original bit stream as the number of tail
bits. Hereinafter, the fixed number is denoted as L fix . The
length of each fixed-length codeword is fixed to L fix + 1.
The L fix is set in advance before performing compression
procedure.

# (2) Variable-length codeword:
a variable-length codeword consists of a prefix, a length symbol
and a tail bit. Variable length codewords are used to compress runs with the length
L >= 4.

# steps for running the project
1) Clone the repo.
2) open terminal.
3) run python3 runlengthcoding.py
4) if not running then install dependency
5) again run python3 runlengthcoding.py
