module my_dff(input clk, input d, output reg q);
    always @(posedge clk) begin
        q <= d;  
    end
endmodule

module top_module ( input clk, input d, output q );
    wire q1, q2;
    my_dff uut1(.clk(clk), .d(d), .q(q1));
    my_dff uut2(.clk(clk), .d(q1), .q(q2));
    my_dff uut3(.clk(clk), .d(q2), .q(q)); 
endmodule
