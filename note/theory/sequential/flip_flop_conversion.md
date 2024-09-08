

| From \ To  | **D Flip-Flop**          | **T Flip-Flop**          | **JK Flip-Flop**                | **SR Flip-Flop**              |
|------------|--------------------------|--------------------------|---------------------------------|-------------------------------|
| **D**      | -                        | D = T⊕Q_n              | JQ_n' + K'Q_n                    | S+R'Qn                |
| **T**      | D⊕Qn              | -                        |  JQ_n' + KQ_n              | SQn' + RQn|
| **JK**     | J = D, K=D'     | J=K=T               | -                               | S = J, R = K                  |
| **SR**     | S = D, R=D'                   | S=Qn'T R= QnT         | S= JQn' R =QnK R                    | -                             |

### Key Points:
- **\( Q_n \)** represents the current output of the flip-flop before the next clock pulse.
- **\( Q_n' \)** represents the complement (or negation) of the current state \( Q_n \).
- **D Flip-Flop**: Directly stores the value of **D** at the next clock pulse.
- **T Flip-Flop**: Toggles the output if **T = 1**, otherwise holds the current value.
- **JK Flip-Flop**: Acts as a toggle when both **J** and **K** are 1, otherwise, it can set, reset, or hold based on inputs.
- **SR Flip-Flop**: Sets when **S = 1** and resets when **R = 1**.

This updated table includes the effect of the current state \( Q_n \), which is crucial for understanding how the next state depends on the flip-flop inputs and the current state.