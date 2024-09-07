module swap_register(
    input reg a;
    input reg b;

    output reg a_new, b_new;
);
reg temp;
assign reg a_new = b;
assign reg b_new = a;
// a = (a+b)/2;
// b = 2*(a-b/2);
// a = 2*(a-b/2);
endmodule

