module bcd_fadd (
    input [3:0] a,
    input [3:0] b,
    input cin,
    output cout,
    output [3:0] sum
);
    wire [4:0] sum_wire;
    wire carry_out_bcd;
    
    assign sum_wire = a + b + cin;
    assign carry_out_bcd = (sum_wire > 9) ? 1'b1 : 1'b0;
    assign sum = (sum_wire > 9) ? (sum_wire - 10) : sum_wire[3:0];
    assign cout = carry_out_bcd;

endmodule

module top_module ( 
    input [15:0] a, b,
    input cin,
    output cout,
    output [15:0] sum );
    wire t1, t2, t3;
    bcd_fadd b1(a[3:0], b[3:0], cin,t1, sum[3:0]);
    bcd_fadd b2(a[7:4], b[7:4],t1 ,t2, sum[7:4]);
    bcd_fadd b3(a[11:8], b[11:8], t2,t3, sum[11:8]);
    bcd_fadd b4(a[15:12], b[15:12],t3,cout, sum[15:12]);
    

endmodule
