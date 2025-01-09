import re

def parse_log(log_file):
    """
    Parses a Gaussian log file to extract job status, last geometry frame, and energy.

    Args:
        log_file (str): Path to the Gaussian log file.

    Returns:
        tuple: (status, geometry, energy), where:
            - status (str): 'success', 'failed', or 'incomplete'.
            - geometry (list): List of strings containing atomic coordinates of the last frame.
            - energy (float): Energy of the last frame, or None if not found.
    """
    status = "incomplete"
    geometry_block = []
    last_energy = None

    # Regex patterns
    energy_pattern = re.compile(r"SCF Done:\s+.*?=\s+([-+]?\d+\.\d+)")
    termination_pattern = re.compile(r"Normal termination")
    
    with open(log_file, "r") as file:
        print("reading log file ", log_file, "...")
        for line in file:
            # Check for termination status
            if termination_pattern.search(line):
                status = "success"

            # Match energy lines
            energy_match = energy_pattern.search(line)
            if energy_match:
                last_energy = float(energy_match.group(1))

    # If no termination and no energy, mark as failed
    if status == "incomplete" and last_energy is None:
        status = "failed"
    
    print("reading geometry......")
    geometry, charge, multiplicity = get_geometry(log_file)
    # print(geometry[:10])
    return status, geometry, last_energy, charge, multiplicity

def get_geometry(filename):
    coords = []
    with open(filename) as f:
        charge = None
        for line in f:
            # if line starts with "Charge = " then get the charge
            if "Charge = " in line and charge is None:
                charge = line.split()[2]
                multiplicity = line.split()[5]
                # print("charge = ", charge)
                # print("multiplicity = ", multiplicity)
            if " Standard orientation:" in line:
                coords = []
                for _ in range(4):  # Changed from 5 to 4 to include first atom
                    next(f)
                for line in f:
                    if "----" in line:
                        break
                    parts = line.split()
                    coords.append([parts[1], float(parts[3]), float(parts[4]), float(parts[5])])
    return coords, charge, multiplicity