{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "min = 1\n",
    "max = 100\n",
    "count = 0\n",
    "target = random.randint(min,max)\n",
    "print(\"==============猜數字遊戲==================\\n\")\n",
    "\n",
    "while(True):\n",
    "    try:\n",
    "        keyin = int(input(f\"猜數字範圍:{min}~{max}:\"))\n",
    "    except:\n",
    "        print(\"輸入格式錯誤\")\n",
    "        count += 1\n",
    "        print(f\"您已經猜了{count}次\")\n",
    "    else:\n",
    "        count += 1\n",
    "        if(keyin >= min and keyin <= max):\n",
    "            if keyin == target:\n",
    "                print(f\"賓果!猜對了, 答案是:\",target)\n",
    "                print(f\"您總共猜了{count}次\")\n",
    "                break\n",
    "            elif keyin > target:\n",
    "                print(\"再小一點\")\n",
    "                max = keyin - 1                \n",
    "            elif keyin < target:\n",
    "                print(\"再大一點\")\n",
    "                min = keyin + 1\n",
    "\n",
    "            print(f\"您已經猜了{count}次\")\n",
    "        else:\n",
    "            print(\"輸入錯誤,超出範圍\")\n",
    "            print(f\"您已經猜了{count}次\")\n",
    "\n",
    "print(\"遊戲結束\")"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
