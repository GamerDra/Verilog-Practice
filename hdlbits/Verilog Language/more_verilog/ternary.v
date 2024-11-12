module top_module (
    input [7:0] a, b, c, d,
    output reg [7:0] min);
    reg [7:0] w1, w2, w3;
    always @(*) begin
        w1 = a<b?a:b;
        w2 = c<d?c:d;
        min = w1<w2?w1:w2;
    end
    
    
    // assign min = (a<b)?((a<c)?((a<d)?a:d):c<d?c:d):b<c?((b<d)?b:d):c<d?c:d;

endmodule
