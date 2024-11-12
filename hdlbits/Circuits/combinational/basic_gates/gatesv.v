module top_module( 
    input [3:0] in,
    output  reg [2:0] out_both,
    output reg [3:1]  out_any,
    output reg [3:0]  out_different );
    
	always @(*) begin
        out_both[2] = in[3] & in[2];
        out_both[1] = in[2] & in[1];
        out_both[0] = in[1] & in[0];
        out_any = {in[3]|in[2], in[2]|in[1], in[1]|in[0]};
        out_different = {in[0]^in[3],in[3]^in[2], in[2]^in[1], in[1]^in[0]};
    end

endmodule
