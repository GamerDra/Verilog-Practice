module top_module( 
    input [399:0] a, b,
    input cin,
    output cout,
    output [399:0] sum );
    wire [100:0] carry;
    assign carry[0] = cin;
    genvar i;
    generate
        for (i = 0; i < 100; i = i + 1) begin : bcd_loop
            bcd_fadd bcd (
                a[i*4+3:i*4],
                b[i*4+3:i*4],
                carry[i],
                carry[i+1],
                sum[i*4+3:i*4],
            );
        end
    endgenerate
    assign cout = carry[99:0];
endmodule

