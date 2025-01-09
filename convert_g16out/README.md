log_to_gjf is a Python module designed to convert `.log` files into `.gjf` files. It allows you to process one or multiple `.log` files in the current directory with a specified method and basis set.

An easier way is to use the convert file function within GaussView but sometimes it just won't work.

# Usage

## Command-Line Usage
You can run the module directly using after specifying the $PATHONPATH:
`python -m log_to_gjf <log_files> <methods>`

## Examples
1. convet a single file:\
`python convert.py example.log "B3LYP/6-31G"`

2. process all *.log files in the current directory:
`python convert.py all "B3LYP/6-31G"`

## Error Handling
- If the output file is incomplete or contains errors, warnings will be displayed.
- If the "all" keyword is used but no .log files are found in the current directory, the script will notify you.
