module mux2to1(input a,b ,sel, output f);
    assign f = (~sel&a)| (sel&b);
endmodule
module top_module (
    input c,
    input d,
    output [3:0] mux_in
); 
    mux2to1 c_or_d (c,1'b1,d,mux_in[0]);
    mux2to1 c_and_d (1'b0,c,d, mux_in[3]);
    assign mux_in[2] = ~d;
    assign mux_in[1] = 1'b0;
endmodule
