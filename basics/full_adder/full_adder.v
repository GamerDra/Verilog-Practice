// Making full_adder using gates

module fullAdder (
    input A, input B,input cin, output sum, output cout
    
);
  wire w1, w2, w3;
  xor (w1, A,B);
  xor (sum, w1,cin);
  
  and (w2, A,B);
  and (w3, cin, w1);
  or (cout, w3, w2);
endmodule



