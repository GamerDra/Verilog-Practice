### Vector Declaration and Part-Select
- Vectors are arrays of bits, often used to represent buses or multi-bit values. For example, `reg [7:0] data` declares an 8-bit vector.
- **Packed vectors** are defined before the variable name, while **unpacked arrays** (such as memory) come after the name. Example: `reg [7:0] mem [255:0];` represents 256 8-bit registers.
- You can access specific portions of a vector using **part-select** syntax, such as `a[3:0]` to get the lower 4 bits. Verilog also allows selecting a portion using ranges like `a[7:4]`.
  
### Combining and Reversing Vectors
- **Concatenation operator** `{}` is used to join smaller vectors into larger ones. For example, `{4'ha, 4'd10}` results in an 8-bit vector `8'b10101010`.
- **Reversing a vector** can be done by assigning parts in reverse order, such as `{out[0], out[1], ..., out[7]} = in;`.

### Bitwise and Logical Operators
- **Bitwise operators** (`&`, `|`, `^`) perform operations on each bit in a vector. For instance, `a | b` computes the bitwise OR of vectors `a` and `b`.
- **Logical operators** (`&&`, `||`) treat entire vectors as Boolean values, where any non-zero vector is `true`.

### HDLBits Exercises:
1. **Splitting a 16-bit input**: Split a 16-bit input signal into two 8-bit outputs (`out_hi` and `out_lo`).
2. **Reversing a 32-bit vector**: Reorder the bytes in a 32-bit vector, useful for converting between little-endian and big-endian formats.
3. **Vector Concatenation**: Join 5 input vectors and append `2'b11` to create four 8-bit output vectors.

