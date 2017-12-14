from Process_File import process
process = process()

reiterate = "y"

while reiterate == "y":
    # open input file to be read from
    input_file_name = input("Enter the name of the file, including the extension, that you want to use as input: ")
    input_file = open(input_file_name, "r")
    # open the output file to be written to
    output_file_name = input("Enter the name of the file, including the extension, that you want to use as output: ")
    mode = input("Do you want to write to this file, or append to this file? [w] or [a]:")
    if mode == "a":
        output_file = open(output_file_name, "a")
    else:
        output_file = open(output_file_name, "w")

    process.process_file(input_file, output_file)

    input_file.close()
    output_file.close()

    reiterate = input("Do you want to process another file? If so, type 'y'. Otherwise, type anything else and hit enter.")

