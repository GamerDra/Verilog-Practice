import itertools

def generate_verilog_testbench(input_names, output_names, module_name):
    num_inputs = len(input_names)
    
    # (2^n combinations for n inputs)
    input_combinations = list(itertools.product([0, 1], repeat=num_inputs))
    

    testbench = []
    
    
    testbench.append(f"module {module_name}_tb;\n")
    
    
    for name in input_names:
        testbench.append(f"reg {name};")
    for name in output_names:
        testbench.append(f"wire {name};")
    
    testbench.append(f"\n// Instantiate the {module_name} module")
    testbench.append(f"{module_name} uut (")
    
    # Instantiate inputs and outputs in the module
    testbench.append(",\n".join([f".{name}({name})" for name in input_names + output_names]) + ");\n")
    
    # initial block to dump the waveforms
    testbench.append(f"""initial 
        begin
            $dumpfile("{module_name}.vcd");
            $dumpvars(0, {module_name});
        end
""")
    
    #  monitoring for all inputs and outputs
    monitor_signals = " | ".join([f"{name} = %b" for name in input_names + output_names])
    testbench.append(f'$monitor("Time = %0d | ' + monitor_signals + '", $time, ' + ", ".join(input_names + output_names) + ");\n")
    
    
    testbench.append("\ninitial begin")
    

    for comb in input_combinations:
        assignments = " ".join([f"{name} = {val};" for name, val in zip(input_names, comb)])
        testbench.append(f"\t{assignments} #10;")
    
    testbench.append("\n\t$finish;\nend\nendmodule")

    return "\n".join(testbench)


if __name__ == '__main__':
    input_names = ["a", "b", "c"]
    output_names = ["sum", "carry"]
    module_name = "my_module"

    testbench_code = generate_verilog_testbench(input_names, output_names, module_name)
    print(testbench_code)
