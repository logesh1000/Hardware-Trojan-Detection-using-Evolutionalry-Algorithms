// Verilog
// 4 bit ripple carry adder
// Ninputs 9
// Noutputs 5
// NtotalGates 24
// AND2 12
// XOR2 8
// AND3 4

module 4bit_ripple (a0,a1,a2,a3,b0,b1,b2,b3,C0,Cout,s0,s1,s2,s3);

input a3,a2,a1,a0,b3,b2,b1,b0,C0;

output Cout,s0,s1,s2,s3;

wire C1,C2,C3,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16;

and AND2_1 (n1, a0, b0);
and AND2_2 (n2, a0, C0);
and AND2_3 (n3, b0, C0);
xor XOR2_4 (n4, a0, b0);
xor XOR2_5 (s0, n4, C0);
or OR3_6 (C1, n1, n2, n3);
and AND2_7 (n5, a1, b1);
and AND2_8 (n6, a1, C1);
and AND2_9 (n7, b1, C1);
xor XOR2_10 (n8, a1, b1);
xor XOR2_11 (s1, n8, C1);
or OR3_12 (C2, n5, n6, n7);
and AND2_13 (n9, a2, b2);
and AND2_14 (n10, a2, C2);
and AND2_15 (n11, b2, C2);
xor XOR2_16 (n12, a2, b2);
xor XOR2_17 (s2, n12, C2);
or OR3_18 (C3, n9, n10, n11);
and AND2_19 (n13, a3, b3);
and AND2_20 (n14, a3, C3);
and AND2_21 (n15, b3, C3);
xor XOR2_22 (n16, a3, b3);
xor XOR2_23 (s3, n16, C3);
or OR3_24 (Cout, n13, n14, n15);

endmodule