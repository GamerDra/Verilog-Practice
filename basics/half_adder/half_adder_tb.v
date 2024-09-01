`timescale 1ns/1ns
`include "half_adder.v"


module half_adder_tb;

    reg A, B;
    wire sum, c;    

halfAdder uut(.A(A), .B(B), .sum(sum), .carry(c));


initial 
    begin
        $dumpfile("half_adder_tb.vcd");
        $dumpvars(0, half_adder_tb);
    end

initial begin
    $display("Start of simulation");
    
    $monitor("Time = %0d | A = %b | B = %b | Sum = %b | Carry = %b", $time, A, B, sum, c);
    
    
    A = 0; B = 0; #10;  // Test case 1: A = 0, B = 0
    A = 0; B = 1; #10;  // Test case 2: A = 0, B = 1
    A = 1; B = 0; #10;  // Test case 3: A = 1, B = 0
    A = 1; B = 1; #10;  // Test case 4: A = 1, B = 1
    
    
    $stop;
end

endmodule   