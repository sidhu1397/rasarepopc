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
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import scipy.cluster.hierarchy as shc\n",
    "\n",
    "plt.figure(figsize=(10, 7))\n",
    "plt.title(\"Customer Dendograms\")\n",
    "dend = shc.dendrogram(shc.linkage(train, method='ward'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3,\n",
       "       4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 1,\n",
       "       4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
       "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 0, 2, 0, 2,\n",
       "       1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2,\n",
       "       0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2,\n",
       "       0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2,\n",
       "       0, 2], dtype=int64)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.cluster import AgglomerativeClustering\n",
    "\n",
    "cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')\n",
    "cluster.fit_predict(train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'(slice(None, None, None), 0)' is an invalid key",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-2ec3e40556a0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfigure\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfigsize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m7\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mscatter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtrain\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtrain\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcluster\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlabels_\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcmap\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'rainbow'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   2925\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnlevels\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2926\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_getitem_multilevel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2927\u001b[1;33m             \u001b[0mindexer\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2928\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mis_integer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2929\u001b[0m                 \u001b[0mindexer\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[0mindexer\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pandas\\core\\indexes\\base.py\u001b[0m in \u001b[0;36mget_loc\u001b[1;34m(self, key, method, tolerance)\u001b[0m\n\u001b[0;32m   2655\u001b[0m                                  'backfill or nearest lookups')\n\u001b[0;32m   2656\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2657\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2658\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2659\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_maybe_cast_indexer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: '(slice(None, None, None), 0)' is an invalid key"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 720x504 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 7))\n",
    "plt.scatter(train[:,0], train[:,1], c=cluster.labels_, cmap='rainbow')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from skleran.metrics import sm"
   ]
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
