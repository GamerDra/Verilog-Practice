module full_adder (
    input A, input B, input cin, 
    output sum, output cout
);
    wire w1, w2, w3;

    xor (w1, A, B);
    xor (sum, w1, cin);

    and (w2, A, B);
    and (w3, cin, w1);
    or (cout, w2, w3);
endmodule

module top_module (
    input [99:0] a, b,
    input cin,
    output [99:0] sum,
    output [99:0] cout
);
    wire [100:0] carry;  

    assign carry[0] = cin;  

    genvar i;
    generate
        for (i = 0; i < 100; i = i + 1) begin : fa_loop
            full_adder fa (
                .A(a[i]), 
                .B(b[i]), 
                .cin(carry[i]), 
                .sum(sum[i]), 
                .cout(carry[i + 1])
            );
        end
    endgenerate

    assign cout = carry[99:0];  
endmodule
