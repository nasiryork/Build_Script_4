#!/usr/bin/bash

echo "============================================"
echo "                   API                      "
echo "--------------------------------------------"
echo "  | Food | Basketball | Anime | Travel |    "
echo "--------------------------------------------"
read -p "Which api would you like to test out: " api
echo "============================================"
sleep 1

python_path="C:\Users\Nasir York\AppData\Local\Programs\Python\Python39\python.exe"
food_api_path="C:\Users\Nasir York\Desktop\Kura Scripts\Python Scripts\Food_API.py"

case $api in
  Food | food)
      #$python3 $food_api_path
      $python_path $food_api_path
      ;;
  Basketball | basketball)
    echo "Basketball" ;;
  Anime | anime)
    echo "Anime" ;;
  Travel | travel)
    echo "Travel" ;;
  Quit | quit)
    ;;
  *)
    echo "============================================"
    echo "              INVALID INPUT!!!              "
    echo "============================================"
    exit
    ;;
esac
echo "Fin"