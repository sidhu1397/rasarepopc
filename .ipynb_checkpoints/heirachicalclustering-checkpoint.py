{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "%matplotlib inline\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     CustomerID   Genre  Age  Annual Income (k$)  Spending Score (1-100)\n",
      "0             1    Male   19                  15                      39\n",
      "1             2    Male   21                  15                      81\n",
      "2             3  Female   20                  16                       6\n",
      "3             4  Female   23                  16                      77\n",
      "4             5  Female   31                  17                      40\n",
      "5             6  Female   22                  17                      76\n",
      "6             7  Female   35                  18                       6\n",
      "7             8  Female   23                  18                      94\n",
      "8             9    Male   64                  19                       3\n",
      "9            10  Female   30                  19                      72\n",
      "10           11    Male   67                  19                      14\n",
      "11           12  Female   35                  19                      99\n",
      "12           13  Female   58                  20                      15\n",
      "13           14  Female   24                  20                      77\n",
      "14           15    Male   37                  20                      13\n",
      "15           16    Male   22                  20                      79\n",
      "16           17  Female   35                  21                      35\n",
      "17           18    Male   20                  21                      66\n",
      "18           19    Male   52                  23                      29\n",
      "19           20  Female   35                  23                      98\n",
      "20           21    Male   35                  24                      35\n",
      "21           22    Male   25                  24                      73\n",
      "22           23  Female   46                  25                       5\n",
      "23           24    Male   31                  25                      73\n",
      "24           25  Female   54                  28                      14\n",
      "25           26    Male   29                  28                      82\n",
      "26           27  Female   45                  28                      32\n",
      "27           28    Male   35                  28                      61\n",
      "28           29  Female   40                  29                      31\n",
      "29           30  Female   23                  29                      87\n",
      "..          ...     ...  ...                 ...                     ...\n",
      "170         171    Male   40                  87                      13\n",
      "171         172    Male   28                  87                      75\n",
      "172         173    Male   36                  87                      10\n",
      "173         174    Male   36                  87                      92\n",
      "174         175  Female   52                  88                      13\n",
      "175         176  Female   30                  88                      86\n",
      "176         177    Male   58                  88                      15\n",
      "177         178    Male   27                  88                      69\n",
      "178         179    Male   59                  93                      14\n",
      "179         180    Male   35                  93                      90\n",
      "180         181  Female   37                  97                      32\n",
      "181         182  Female   32                  97                      86\n",
      "182         183    Male   46                  98                      15\n",
      "183         184  Female   29                  98                      88\n",
      "184         185  Female   41                  99                      39\n",
      "185         186    Male   30                  99                      97\n",
      "186         187  Female   54                 101                      24\n",
      "187         188    Male   28                 101                      68\n",
      "188         189  Female   41                 103                      17\n",
      "189         190  Female   36                 103                      85\n",
      "190         191  Female   34                 103                      23\n",
      "191         192  Female   32                 103                      69\n",
      "192         193    Male   33                 113                       8\n",
      "193         194  Female   38                 113                      91\n",
      "194         195  Female   47                 120                      16\n",
      "195         196  Female   35                 120                      79\n",
      "196         197  Female   45                 126                      28\n",
      "197         198    Male   32                 126                      74\n",
      "198         199    Male   32                 137                      18\n",
      "199         200    Male   30                 137                      83\n",
      "\n",
      "[200 rows x 5 columns]\n"
     ]
    }
   ],
   "source": [
    "data=pd.read_csv(\"C:\\\\Users\\\\Admin\\\\Desktop\\\\Titanic Data Set\\\\hierarchical-clustering-with-python-and-scikit-learn-shopping-data.csv\")\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Annual Income (k$)  Spending Score (1-100)\n",
      "0                    15                      39\n",
      "1                    15                      81\n",
      "2                    16                       6\n",
      "3                    16                      77\n",
      "4                    17                      40\n",
      "5                    17                      76\n",
      "6                    18                       6\n",
      "7                    18                      94\n",
      "8                    19                       3\n",
      "9                    19                      72\n",
      "10                   19                      14\n",
      "11                   19                      99\n",
      "12                   20                      15\n",
      "13                   20                      77\n",
      "14                   20                      13\n",
      "15                   20                      79\n",
      "16                   21                      35\n",
      "17                   21                      66\n",
      "18                   23                      29\n",
      "19                   23                      98\n",
      "20                   24                      35\n",
      "21                   24                      73\n",
      "22                   25                       5\n",
      "23                   25                      73\n",
      "24                   28                      14\n",
      "25                   28                      82\n",
      "26                   28                      32\n",
      "27                   28                      61\n",
      "28                   29                      31\n",
      "29                   29                      87\n",
      "..                  ...                     ...\n",
      "170                  87                      13\n",
      "171                  87                      75\n",
      "172                  87                      10\n",
      "173                  87                      92\n",
      "174                  88                      13\n",
      "175                  88                      86\n",
      "176                  88                      15\n",
      "177                  88                      69\n",
      "178                  93                      14\n",
      "179                  93                      90\n",
      "180                  97                      32\n",
      "181                  97                      86\n",
      "182                  98                      15\n",
      "183                  98                      88\n",
      "184                  99                      39\n",
      "185                  99                      97\n",
      "186                 101                      24\n",
      "187                 101                      68\n",
      "188                 103                      17\n",
      "189                 103                      85\n",
      "190                 103                      23\n",
      "191                 103                      69\n",
      "192                 113                       8\n",
      "193                 113                      91\n",
      "194                 120                      16\n",
      "195                 120                      79\n",
      "196                 126                      28\n",
      "197                 126                      74\n",
      "198                 137                      18\n",
      "199                 137                      83\n",
      "\n",
      "[200 rows x 2 columns]\n"
     ]
    }
   ],
   "source": [
    "train=data.drop(['CustomerID','Genre','Age'],axis=1)\n",
    "print(train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}