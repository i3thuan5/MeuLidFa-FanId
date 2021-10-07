# MeuLidFa-FanId
苗栗話翻譯

## 遽遽做
### 安裝
- 安裝[Ubuntu Linux 20.04 LTS作業系統](https://ubuntu.com/download/desktop?version=20.04&architecture=amd64)
- Nvidia cuda driver
- 安裝[docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)
- 安裝[docker-compose](https://docs.docker.com/compose/install/)
- 設定docker權限`sudo usermod -aG docker $USER`
- 安裝[dobi](https://github.com/dnephin/dobi)

### 下載專案
```
git clone git@github.com:i3thuan5/MeuLidFa-FanId.git
```

#### 若係無權，愛用ssh key代替密碼
https://github.com/settings/keys

1. 產生ssh key
2. rsa_id.pub傳去github

### 訓練
`time dobi qionpu`

### 定服務
```
docker-compose up --build
```

### 試翻譯
```bash
curl -i -X POST -H "Content-Type: application/json"  \
    -d '[
        {"src": "我 打 籃 球 時 手 扭 傷 ， 醫 生 說 要 打 石 膏 。 ", "id": 1},
        {"src": "黃 槿 樹 的 葉 子 ， 一 片 差 不 多 手 掌 一 般 大 。 ", "id": 1}
    ]' \
    "http://localhost:5000/translate"
```
#### 結果
```bash
HTTP/1.1 200 OK
Content-Length: 620
Content-Type: application/json
Date: Fri, 10 Sep 2021 08:30:26 GMT
Server: waitress

[[{"n_best":1,"pred_score":-5.343369007110596,"src":"\u6211 \u6253 \u7c43 \u7403 \u6642 \u624b \u626d \u50b7 \uff0c \u91ab \u751f \u8aaa \u8981 \u6253 \u77f3 \u818f \u3002 ","tgt":"\ud840\ude8e \u6309 \u7c43 \u7403 \u6642 \u624b \uff0c \u5148 \u751f \u8b1b \u611b \u6253 \u77f3 \u81a0 \u3002 "},{"n_best":1,"pred_score":-10.280594825744629,"src":"\u9ec3 \u69ff \u6a39 \u7684 \u8449 \u5b50 \uff0c \u4e00 \u7247 \u5dee \u4e0d \u591a \u624b \u638c \u4e00 \u822c \u5927 \u3002 ","tgt":"\u9ec3 \u790e \u6a39 \u4ed4 \uff0c \u4e00 \u3f13 \u4ed4 \uff0c \u4e00 \u3f13 \u4ed4 \u8f03 \u6bcb \u591a \u624b \u5df4 \u4ed4 \u3002 "}]]
```
係UTF-16，到[Unicode Converter](https://www.branah.com/unicode-converter)做得看著
```bash
[[{"n_best":1,"pred_score":-5.343369007110596,"src":"我 打 籃 球 時 手 扭 傷 ， 醫 生 說 要 打 石 膏 。 ","tgt":"𠊎 按 籃 球 時 手 ， 先 生 講 愛 打 石 膠 。 "},{"n_best":1,"pred_score":-10.280594825744629,"src":"黃 槿 樹 的 葉 子 ， 一 片 差 不 多 手 掌 一 般 大 。 ","tgt":"黃 礎 樹 仔 ， 一 㼓 仔 ， 一 㼓 仔 較 毋 多 手 巴 仔 。 "}]]
```

## 訓練
`dobi.yaml`:
```yaml
alias=qionpu: # 全部
  tasks: [hazoi-ngiliau, don-ngiliau, zunpi-ngiliau, hiunlien, ]
```
有
1. `job=hazoi-ngiliau: # 下載語料`
2. `job=don-ngiliau: # 斷詞斷字語料`
3. `job=zunpi-ngiliau: # 準備語料`
4. `job=hiunlien: # 訓練`

### 1. `job=hazoi-ngiliau: # 下載語料`
`time dobi hazoi-ngiliau`
#### 結果
```bash
1-ngienbun-ngiliau/
├── fa.txt
└── meu.txt
```

### 2. `job=don-ngiliau: # 斷詞斷字語料`
`time dobi don-ngiliau`
#### 結果
```bash
2-doncii-ngiliau/
├── fa.train
├── fa.valid
├── meu.train
└── meu.valid
```

### 3. `job=zunpi-ngiliau: # 準備語料`
`time dobi zunpi-ngiliau`
#### 結果
```bash
3-opennmt-data/
├── meufa.vocab.src
└── meufa.vocab.tgt
```

### 4. `job=hiunlien: # 訓練`
`time dobi hiunlien`

#### 結果
```bash
4-opennmt-model/
├── fameu_step_1000.pt
├── fameu_step_10000.pt
├── fameu_step_10500.pt
├── fameu_step_11000.pt
...
```
