module dff (
    input clk,    // Clocks are used in sequential circuits
    input d,
    output reg q );//

    always @(posedge clk) begin
        q <= d;
    end

endmodule

module top_module (
    input clk,
    input [7:0] d,
    output [7:0] q
);

    genvar i;
    generate
        for (i = 0; i < 8; i = i + 1) begin: dff_instances
            dff dff_inst (
                .clk(clk),
                .d(d[i]),
                .q(q[i])
            );
        end
    endgenerate

endmodule

