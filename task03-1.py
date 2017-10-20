config_file_path = "./running-config.cfg"
output_file = "./config-modified.cfg"
find_pattern = "172."
replace_pattern = "192."

def main():
    fin = open(config_file_path)
    fout = open(output_file,'w')
    for line in fin:
        line_modified = line.replace(find_pattern,replace_pattern)
        fout.write(line_modified)
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()