import sys
from read_log import parse_log
from write_input import write_input
import os
import glob 

def main():
    if len(sys.argv) < 4:
        print("Usage: python convert.py input.log xyz|gjf level_of_theory")
        print("The output file name will be input[_optimized]_out.xyz|gjf")
        exit()

    finput = sys.argv[1]
    fformat = sys.argv[2]
    level_of_theory = sys.argv[3]
    
    if fformat not in ["xyz", "gjf"]:
        print("The output file format has to be either xyz or gjf")
        exit()

    if "all" in finput:
        log_files = glob.glob("*.log")  # Expand the pattern to a list of files
        if not log_files:
            print("No .log files matched the pattern.")
            sys.exit(1)
    else:
        log_files = [finput]  # Treat as a single file
        basename =  os.path.splitext(os.path.basename(finput))[0]
    # print(fformat)


    for log_file in log_files:
        if os.path.isfile(log_file):  # Ensure it's a valid file
            status, geometry, energy, charge, multiplicity = parse_log(log_file)
        if status == "failed":
            print(f"Warning! Job failed")

        # Generate output file name
        output_file = f"{log_file.replace('.log', '')}_new.{fformat}"

        # Write the new input file
        write_input(output_file, fformat, geometry, level_of_theory, charge = charge, multiplicity = multiplicity)

        print(f"Conversion successful! File written: {output_file}")
        if energy is not None:
            print(f"Energy of the last frame: {energy}")

if __name__ == "__main__":
    main()
