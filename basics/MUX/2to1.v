// 2:1 mux using gates
module mux_2to1 (
    input  A, 
    input  B,
    input select,
    output out
);

  wire w1, w2, w3;
  and (w1, A,~select);
  and (w2,B,select);
  or (out, w1, w2);
endmodule   



