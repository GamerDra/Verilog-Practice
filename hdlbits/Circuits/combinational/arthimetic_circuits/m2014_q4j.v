module fadd( 
    input a, b, cin,
    output cout, sum );
    assign cout = (a&b) | (cin&(a^b));
    assign sum = (a^b^cin); 

endmodule

module top_module (
    input [3:0] x,
    input [3:0] y, 
    output [4:0] sum);
    wire [2:0] cout;
    fadd f1(x[0],y[0], 0, cout[0], sum[0]);
    fadd f2(x[1],y[1], cout[0], cout[1], sum[1]);
    fadd f3(x[2],y[2], cout[1], cout[2], sum[2]);
    fadd f4(x[3],y[3], cout[2], sum[4], sum[3]);
  

endmodule
