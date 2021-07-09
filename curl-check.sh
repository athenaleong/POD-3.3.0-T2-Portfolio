#!/bin/bash
#Test all endpoints and output result

domain="https://mlh-week2.duckdns.org/"
declare -a StringArray=("health" "athena" "patrick" "juancarlos")

for val in ${StringArray[@]}; 
do
    response=$(curl -s -o /dev/null -w "%{http_code}" ${domain}${val})
    echo "${domain}${val}"
    echo ${response}
done 

username=$RANDOM
password=$RANDOM

echo "${domain}register"
response=$(curl -X POST -s -d "username=${username}&password=${password}" ${domain}register)
echo ${response}

echo "${domain}login"
response=$(curl -X POST -s -d "username=${username}&password=${password}" ${domain}login)
echo ${response}
