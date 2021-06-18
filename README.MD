# dfast and marker extraction

This is the dfast annotation pipeline designed for the slurm system in DSMZ.

### Prerequisites

0. dfast

1. biopython

### Run

1. First, run the dfast annotation:

```
./submit.sh [bin_folder]
```



2. run marker_extract.py

```
find [bin_folder] -iname "*_dfast" -exec python marker_extract.py {} \; > [YourOutput.fasta]
```