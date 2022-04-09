// Verilog
// c17
// Ninputs 5

module c17 (N1,N2,N3,N6,N7,N22,N23);

input N1,N2,N3,N6,N7;

output N22,N23;

wire N10,N11,N16,N19,N24,N25;

nand NAND2_1 (N10, N1, N3);

nand NAND2_2 (N11, N3, N6);

nand NAND2_3 (N16, N2, N11);

and AND2_1 (N24, N2, N11);

xor XOR2_1 (N25, N16, N24);

nand NAND2_4 (N19, N11, N7);

nand NAND2_5 (N22, N10, N25);

nand NAND2_6 (N23, N25, N19);

endmodule
