readonly RM_BACKUP="/tmp/rm_backup"
  
backup_rm() {
        local tmp_file_or_dir
        local counter

        mkdir -p "${RM_BACKUP}"

        for file_or_dir in "$@"
        do
                file_or_dir="${file_or_dir%/}"
                if [ ! -e "${file_or_dir}" ]
                then
                        >&2 echo "rm: ${file_or_dir}: No such file or directory"
                        continue
                fi
                counter=0
                tmp_file_or_dir="${file_or_dir##*/}"

                while [ -e "${RM_BACKUP}/${tmp_file_or_dir}" ]
                do
                        tmp_file_or_dir="${file_or_dir##*/}_${counter}"
                        counter="$(expr "${counter}" + 1)"
                done

                mv "${file_or_dir}" "${RM_BACKUP}/${tmp_file_or_dir}"
        done
}

alias rm="backup_rm"
