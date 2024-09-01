`timescale 1ns/1ns
`include "2to1.v"


module mux2_1;

    reg A, B, select;
    wire out;    

mux_2to1 uut(.A(A), .B(B), .select(select), .out(out));


initial 
    begin
        $dumpfile("2 to 1.vcd");
        $dumpvars(0, mux2_1);
    end

initial begin
    $display("Start of simulation");
    
   $monitor("Time = %0d | A = %b | B = %b | select = %b | out = %b ", $time, A, B, select, out);
        
        // Test cases
        A = 0; B = 0; select = 0; #10; 
        A = 0; B = 1; select = 0; #10; 
        A = 1; B = 0; select = 0; #10; 
        A = 1; B = 1; select = 0; #10;
        A = 0; B = 0; select = 1; #10;
        A = 0; B = 1; select = 1; #10;
        A = 1; B = 0; select = 1; #10;
        A = 1; B = 1; select = 1; #10;
        
    $finish;
end

endmodule   