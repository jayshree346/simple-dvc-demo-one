create env
```bash
conda create -n wineq python=3.7 -y
```
activate wineq
```bash
conda activate wineq
```
created a requirements file
install the requirements

```bash
pip install -r requirements.txt
```
download the dataset from link below

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```
online updates for readme file

```bash
git add . && git commit -m "update readme file"
```
```bash
git remote add origin https://github.com/jayshree346/simple-dvc-demo-one.git 
git branch -M main 
git push origin main
```




