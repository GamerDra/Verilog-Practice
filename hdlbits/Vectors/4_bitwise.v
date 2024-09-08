module top_module( 
    input [2:0] a,
    input [2:0] b,
    output [2:0] out_or_bitwise,
    output out_or_logical,
    output [5:0] out_not
);
    assign out_or_bitwise = a|b;
    assign out_or_logical = a||b;
    assign out_not = {~b,~a};
    // first i tried ~a, ~b but that didnot work because it says in the question \
    // Place the inverse of b in the upper half of out_not (i.e., bits [5:3]), and the inverse of a in the lower half
    

endmodule
