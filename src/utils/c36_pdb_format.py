from pathlib import Path
import sys

# Universal DNA rename map
common_map = {"OP1": "O1P", "OP2": "O2P"}

# Thymine-specific map
dt_map = {"C7": "C5M", "H71": "H5M1", "H72": "H5M2", "H73": "H5M3"}

def fix_pdb(infile, outfile):
    n_changes = 0
    out_lines = []

    for line in Path(infile).read_text().splitlines():
        if line.startswith(("ATOM","HETATM")):
            if len(line) < 80:
                line = line + " " * (80 - len(line))
            atom = line[12:16].strip()
            resn = line[17:20].strip()

            if resn in {"DA","DC","DG","DT"} and atom in common_map:
                new_atom = common_map[atom].rjust(4)
                line = line[:12] + new_atom + line[16:]
                n_changes += 1

            if resn == "DT" and atom in dt_map:
                new_atom = dt_map[atom].rjust(4)
                line = line[:12] + new_atom + line[16:]
                n_changes += 1

        # Don’t strip trailing spaces here; preserve exact column layout
        out_lines.append(line)

    Path(outfile).write_text("\n".join(out_lines) + "\n")
    print(f"Applied {n_changes} changes. Output written to {outfile}")

if __name__ == "__main__":
    if len(sys.argv) not in {2, 3}:
        print(__doc__)
        sys.exit(1)

    infile = Path(sys.argv[1])
    if len(sys.argv) == 3:
        outfile = Path(sys.argv[2])
    else:
        outfile = infile.with_name(f"{infile.stem}_c36.pdb")

    fix_pdb(infile, outfile)
