#!/bin/bash

for i in {1..257}; do
    # filename="$i"_*.jpg
    # if [ -e "$filename" ]; then
        # mv subfile$i/* ./
    rm -r $i.*
    # else
    #     echo "file$i does not exist"
    # fi
done

# start=1
# for i in $(seq $start $((start + $1 - 1))); do
#     if [ -d subfile$i ]; then
#         mv subfile$i/* ./
#         rm -r subfile$i
#     else
#         echo "Subdirectory subfile$i does not exist"
#     fi
# done

#!/bin/bash

# for i in $(seq 1 $1); do
#     if [ -d $i.* ]; then
#         mv $i.*/* ./
#         rm -r $i.*
#     else
#         echo "Subdirectory subfile $i does not exist"
#     fi
# done

# for i in $(seq 1 $1); do
#     if [ -d $2/$i.* ]; then
#         mv $2/$i.*/* ./
#         rm -r $2/$i.*
#     else
#         echo "Subdirectory subfile $i does not exist"
#     fi
# done