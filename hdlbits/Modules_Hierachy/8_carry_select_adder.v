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
    output [31:0] sum
);
    wire cout1, cout2;
    wire [15:0] temp_sum1, temp_sum2;
    add16 uut1 (a[15:0], b[15:0], 0, sum[15:0], cout1);
    add16 uut2 (a[31:16], b[31:16], 0, temp_sum1[15:0], cout2);
    add16 uut3 (a[31:16], b[31:16], 1, temp_sum2[15:0], cout2);
    
    assign sum[31:16] = cout1 ? temp_sum2: temp_sum1;

endmodule
