module dff (
    input clk,  
    input reset,
    input d,
    output reg q );//

    always @(posedge clk) begin
        if (reset)
            q<=0;
        else
        	q <= d;
    end

endmodule

module top_module (
    input clk,
    input reset,            // Synchronous reset
    input [7:0] d,
    output [7:0] q
);
    genvar i;
    generate
        for (i = 0; i < 8; i = i + 1) begin: dff_instances
            dff dff_inst (
                .clk(clk),
                .reset(reset),
                .d(d[i]),
                .q(q[i])
            );
        end
    endgenerate

endmodule
