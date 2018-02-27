#!/bin/bash

result=$(flake8 r2c/r2c.py)

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr 0`

if [ -z "$result" ]; then
  echo -e "\n ${green} -> OK tu peux envoyer ça sur le Git ;)${reset} \n"
else
  echo $result
  echo -e "\n ${red} -> Tu ne pousseras RIEN tant que tu n'auras pas tout corrigé ;) ${reset} \n"
fi
