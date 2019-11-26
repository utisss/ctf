#!/bin/sh

# Expect 1st command to be initial file, expect 2nd command to be number of compressions to occur

prev=-1;
curr=-1;
file_prefix='result';
prev_file=$1;

for index in $(seq 1 $2); do 
    curr_file="${file_prefix}${index}";
    curr=$((RANDOM % 3));

    # Prevent same compressing from happening twice in a row
    while [ $prev == $curr  ]
    do
        curr=$((RANDOM % 3));
    done
     
    # execute curr-th command of compressions
    if [ $curr == 0 ]; then
        eval $"gzip -c $prev_file > $curr_file";
    elif [ $curr == 1 ]; then
        eval $"bzip2 -c $prev_file > $curr_file";
    elif [ $curr == 2 ]; then
        eval $"base64 $prev_file > $curr_file";
    elif [ $curr == 3 ]; then
        eval $"tar -cvf $curr_file $prev_file";
    fi

    # delete previous file
    eval $"rm $prev_file"

    prev_file=$curr_file
    echo $curr;
    echo $prev;
    prev=$curr;
done
