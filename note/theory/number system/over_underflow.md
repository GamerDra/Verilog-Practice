The key difference between **overflow** and **underflow** lies in the direction of the arithmetic operation exceeding the representable range in a given bit-width system.

---

### **Overflow**
- **What Happens?**  
  The result of an operation is **too large** to fit within the maximum representable value for the given number of bits.
- **Range Exceeded:** The result goes **above the maximum value**.
- **Signs of Overflow:**  
  - Adding two positive numbers results in a **negative number**.
  - Subtracting a negative number from a positive number results in a **negative number**.

#### Example of Overflow in a 4-bit System:
- Range: \(-8 \, \text{to} \, +7\).
- Add \(+7 + +1\):
  - Binary: \(0111 + 0001 = 1000\) (\(-8\) in 4-bit 2's complement).
  - Expected result is \(8\), but it overflows and wraps around to \(-8\).

---

### **Underflow**
- **What Happens?**  
  The result of an operation is **too small** to fit within the minimum representable value for the given number of bits.
- **Range Exceeded:** The result goes **below the minimum value**.
- **Signs of Underflow:**  
  - Adding two negative numbers results in a **positive number**.
  - Subtracting a positive number from a negative number results in a **positive number**.

#### Example of Underflow in a 4-bit System:
- Range: \(-8 \, \text{to} \, +7\).
- Subtract \(-8 - 1\):
  - Binary: \(1000 + 1111 = 0111\) (\(+7\) in 4-bit 2's complement).
  - Expected result is \(-9\), but it underflows and wraps around to \(+7\).

---

### **Comparison Table**

| **Aspect**          | **Overflow**                         | **Underflow**                        |
|----------------------|---------------------------------------|---------------------------------------|
| **Cause**            | Result exceeds the **maximum value** | Result goes below the **minimum value** |
| **Range Violated**   | Above \(+2^{N-1} - 1\)               | Below \(-2^{N-1}\)                   |
| **Typical Cases**    | Adding two large positive numbers    | Subtracting a positive number from the smallest negative number |
| **Result Behavior**  | Wraps around to the **minimum value** | Wraps around to the **maximum value** |
| **Signs Involved**   | Positive inputs → Negative result    | Negative inputs → Positive result    |

---

### **Visualization of 4-bit Range**
The 4-bit 2's complement range is cyclic:

```
 -8 → 1000       +7 → 0111
  ↓                ↑
 Wrap-around     Wrap-around
```

- **Overflow**: Going above \(+7\) (0111) wraps to \(-8\) (1000).
- **Underflow**: Going below \(-8\) (1000) wraps to \(+7\) (0111).

---

### **Summary**
- **Overflow**: Happens when numbers go **too high** for the range.
- **Underflow**: Happens when numbers go **too low** for the range.
