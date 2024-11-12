module top_module( 
    input [254:0] in,
    output reg [7:0] out);
    integer i = 0;
    
    always @(*) begin
        out = 0;
        for (i = 0; i < 255; i = i + 1) begin
            out = (in[i]==1)?(out+1):out;
    end
    end

endmodule
