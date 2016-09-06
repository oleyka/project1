#!/usr/bin/env python

import os
import sys
import pandas as pd

from common.global_vars import *


def read_all(breed_id):
    global offa_save_path

    print >>sys.stderr, "Collecting data for breed", breed_id, ":",

    fdir = offa_save_path + "/" + breed_id
    if not os.path.exists(fdir) or not os.path.isdir(fdir):
        print >>sys.stderr, "wrong location \"" + fdir + "\""
        return

    flist = [d for d in os.listdir(fdir)
             if len(d) > 4 and (d[-4:] == ".csv" or d[-4:] == ".txt")]

    records_list = [pd.read_csv(fdir + "/" + f,
                                header=None,
                                skip_blank_lines=True,
                                names=[
                                    "OFA Number",
                                    "Registration Number",
                                    "Registry Code",
                                    "Closed/Open",
                                    "Breed Code",
                                    "Registered Name",
                                    "Sex",
                                    "Color",
                                    "Birthdate",
                                    "Age at Test (Months)",
                                    "Test Date",
                                    "Results",
                                    "Sire Registration",
                                    "Dam Registration"
                                ]) for f in flist]

    records = pd.concat(records_list)
    print >>sys.stderr, "Done."
    return records


def main():
    breed_id = os.environ["k9data_breed"] if "k9data_breed" in os.environ else "WO"

    records = read_all(breed_id)
    return

if __name__ == "__main__":
    main()
