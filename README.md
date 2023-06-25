# QIIME2-IQR-generator
The QIIME2-IQR-generator is a tool based on the QIIME2 kit used to calculate the interquartile range (IQR) of taxonomy relative abundance. Users only need to enter the genus-level name and the corresponding experimental abundance, and the tool will generate the IQR figure.

- Parameters

``` python
path = './'
#The folder path

fileName = 'level-6.csv'  
#NGS composition result in level-6 (.csv) after classifier analysis.
```

- input()

``` python
Bacteria (Genus)?
#Blautia

ObserveValue (%)? 
#12

```
- Input file - level-6.csv

![Input file](https://user-images.githubusercontent.com/81002817/179383739-ac797212-2376-4688-b992-cdb32e53ede1.png "Input file")

- Output figures

![image](https://github.com/ba2c7yoyo/NTGS/assets/81002817/59b907a1-046d-44f9-91f3-4e8cde459cee)

