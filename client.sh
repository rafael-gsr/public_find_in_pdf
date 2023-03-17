#! /bin/bash

clear
initial_path="$PWD"

red="\e[0;91m"
blue="\e[0;94m"
expand_bg="\e[K"
blue_bg="\e[0;104m${expand_bg}"
red_bg="\e[0;101m${expand_bg}"
green_bg="\e[0;102m${expand_bg}"
green="\e[0;92m"
white="\e[0;97m"
bold="\e[1m"
uline="\e[4m"
reset="\e[0m"

# echo -e "$blue_bg  $reset"
# echo -e "$white °°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°"
# echo ""
# echo -e " $blue Cd folder? (y/n) "
# echo ""
# echo -e "$white °°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°"
# echo -e "$blue_bg  $reset"
# read cd_folder


# if [ $cd_folder == y ]
#     then
#         cd $HOME/Desktop/FIND_IN_PDF_APP
# fi

# clear


echo -e "$blue_bg  $reset"
echo -e "$white °°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°"
echo ""
echo -e "$blue WHAT DO YOU WANT TO DO? $reset"
echo ""
echo -e "$red 1 -$green RODAR APP"
echo -e "$red 2 -$green INSTALAR"
echo -e "$red 3 -$green DECRIPTAR"
echo -e "$red 4 -$green DESINSTALAR"
echo -e "$red 5 -$green FECHAR CLIENT" 
echo -e "$red 6 -$green ENCRIPTAR $reset"
echo ""
echo -e "$white °°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°..°°"
echo -e "$blue_bg       $reset"

read whatYouWant

case $whatYouWant in
	1) echo -e  "$blue Rodando o App ... $reset"
		cd $HOME/Desktop/FIND_IN_PDF_APP/
        python ./pdf_reader.py 
        ;;
        
	4) echo -e  "$blue Desinstalando ... $reset"
		
        echo -e "$blue Isso apagará $red TODOS $blue os arquivos em FIND_IN_PDF_APP/ $reset"
        echo -e "$blue Você tem certeza disso? (y/n) $reset"
        
        read areYouShure
        if [ $areYouShure == "y" ]
            then 
                rm -rf $HOME/Desktop/FIND_IN_PDF_APP/
            else
                echo -e "$red  Ok, até mais $reset"
        fi 
        
        ;;
	
    3) echo -e  "$blue Decriptando ... $reset"
	    cd $HOME/Desktop/FIND_IN_PDF_APP/
        python decrypt.py 
        ;;

    2) echo -e  "$blue Instalando ... $reset"
        sudo pacman -S python-pip wget
        pip install PyPDF2 datetime cryptography

        clear

        cd $HOME/Desktop

        if [ -d FIND_IN_PDF_APP ]
            then
                cd $HOME/Desktop/FIND_IN_PDF_APP
            else
                cd $HOME/Desktop
                mkdir FIND_IN_PDF_APP
                cd FIND_IN_PDF_APP
        fi 

        echo "GVlEy6rnvdVYxes7hCqJKgC8HZcJpCUgLPXHkntq4Qw=" > key.txt
        echo "" > palavras_a_procurar.txt

        wget "https://raw.githubusercontent.com/nefelyn/public_find_in_pdf/main/encrypt.py.encrypted"
        wget "https://raw.githubusercontent.com/nefelyn/public_find_in_pdf/main/pdf_reader.py.encrypted"
        cp -f "$initial_path/decrypt.py" "$PWD"

        python decrypt.py
        ;;

	5) echo -e  "$blue Fechando o script ... $reset"
        exit 
        ;;

    6) echo -e "$blue Encriptando ... $reset"
        cd $HOME/Desktop/FIND_IN_PDF_APP/
        python encrypt.py 
        ;;

	*)echo -e  "$reset Essa não é uma oppção $reset";;
esac

