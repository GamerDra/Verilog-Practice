module swap_vector(
    input [7:0] in_1,
    input [7:0] in_2,
    output [7:0] out_1,
    output [7:0] out_2
);
    assign {out_1, out_2} = {in_2,  in_1};
endmodule