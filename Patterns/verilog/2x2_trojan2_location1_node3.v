// Verilog
// 2x2 vedic multiplier
// Ninputs 4
// Noutputs 4
// NtotalGates 8
// AND2 6
// XOR2 2

module 2x2_ved (a0,b0,a1,b1,q0,q1,q2,q3);

input a0,b0,a1,b1;

output q0,q1,q2,q3;

wire n1,n2,n3,n4,n5,n6;

and AND2_1 (q0, a0, b0);
and AND2_2 (n1, a1, b0);
and AND2_3 (n2, a0, b1);
and AND2_4 (n3, a1, b1);
and AND2_1 (n5, a1, b1);
xor XOR2_1 (n6, n3, n5);
xor XOR2_5 (q1, n1, n2);
and AND2_6 (n4, n1, n2);
xor XOR2_7 (q2, n6, n4);
and AND2_8 (q3, n6, n4);

endmodule