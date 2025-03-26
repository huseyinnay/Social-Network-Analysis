# 👥 Social Network Analysis of LinkedIn Connections

Bu projede, 6.000'den fazla kişinin LinkedIn bağlantıları analiz edilmiştir. Python kullanılarak geliştirilen bu çalışma, bireyler arasındaki ilişkileri anlamak ve bu ilişkilerin sosyal yapı üzerindeki etkilerini incelemek amacıyla gerçekleştirilmiştir.

## 🧠 Kullanılan Yöntemler ve Hesaplamalar

- **Betweenness Centrality**
- **Closeness Centrality**
- **Eigenvector Centrality**
- **Ağın En Yüksek Dereceli (Bağlantılı) Düğümü**
- **Network Density (Ağ Yoğunluğu)**
- **Average Clustering Coefficient (Ortalama Kümeleme Katsayısı)**
- **Average Shortest Path Length (Ortalama En Kısa Yol Uzunluğu)**
- **Topluluk Algılama Algoritmaları:**
  - Louvain Algorithm
  - Girvan-Newman Algorithm

## 🔍 Elde Edilen Bulgular

- Ağ üzerindeki etkili bireyler ve "anahtar kişiler" belirlendi.
- Topluluk yapıları çıkarıldı ve bireylerin hangi gruplarda yer aldığı incelendi.
- Profesyonel etkileşimler ve bağlantı yoğunluğu görselleştirildi.
- Ağın genel yapısı ve etkileşim kalıpları analiz edildi.

## 📊 Kullanılan Kütüphaneler

- [NetworkX](https://networkx.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

## 🌐 English Summary

Conducted social network analysis of over **6,000 LinkedIn users** using Python libraries like NetworkX, Pandas, and Matplotlib.  
Calculated key centrality metrics including **betweenness**, **closeness**, and **eigenvector centrality**.  
Measured global network properties such as **density**, **clustering coefficient**, and **average shortest path length**.  
Applied **Louvain** and **Girvan-Newman** algorithms for community detection and uncovered **interaction patterns** and **influence dynamics** within the network.

## 📁 Nasıl Çalıştırılır?

```bash
pip install -r requirements.txt
python main.py
