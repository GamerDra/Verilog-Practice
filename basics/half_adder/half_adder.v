module halfAdder (
    input A, input B, output sum, output carry
    
);
  wire w1, w2, w3, w4;
  xor (sum, A,B);
  and (carry, A,B);
endmodule


