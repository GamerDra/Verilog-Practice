`timescale 1ns/1ns
`include "full_adder.v"


module full_adder_tb;

    reg A, B, cin;
    wire sum, cout;    

fullAdder uut(.A(A), .B(B), .cin(cin), .sum(sum), .cout(cout));


initial 
    begin
        $dumpfile("full_adder.vcd");
        $dumpvars(0, full_adder_tb);
    end

initial begin
    $display("Start of simulation");
    
   $monitor("Time = %0d | A = %b | B = %b | cin = %b | Sum = %b | Carry = %b", $time, A, B, cin, sum, cout);
        
        // Test cases
        A = 0; B = 0; cin = 0; #10; 
        A = 0; B = 1; cin = 0; #10; 
        A = 1; B = 0; cin = 0; #10; 
        A = 1; B = 1; cin = 0; #10;
        A = 0; B = 0; cin = 1; #10;
        A = 0; B = 1; cin = 1; #10;
        A = 1; B = 0; cin = 1; #10;
        A = 1; B = 1; cin = 1; #10;
        
    $finish;
end

endmodule   