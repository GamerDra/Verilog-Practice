module add16 (
    input [15:0] a,
    input [15:0] b,
    input cin,
    output [15:0] sum,
    output cout
);
    assign {cout, sum} = a + b + cin;  // 16-bit addition with carry-in and carry-out
endmodule

module top_module(
    input [31:0] a,
    input [31:0] b,
    input sub,
    output [31:0] sum
);
    wire cout1, cout2;
    wire [31:0] bin;
    assign bin = b ^ {32{sub}};
    
    add16 uut1 (a[15:0], bin[15:0], sub, sum[15:0], cout1);
    add16 uut2 (a[31:16], bin[31:16], cout1, sum[31:16], cout2);
    

endmodule


