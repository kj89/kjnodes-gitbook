# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

Website: [https://www.rebuschain.com](https://www.rebuschain.com)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (29)
```
peers="a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,f83df63886e56713bf3adb5c6836b1a7b07ec024@65.108.235.18:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,408206e3aab058d1dc09697566e3dadfaa3760ea@135.181.5.47:20106,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,186209f02d238b48dcc7997cca3e6c6855aa91aa@20.112.73.169:26656,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,0a3eb0b5a76b2b881ae260e4546e3fbbfbbfba4b@65.108.206.56:32656,3fc3b7e3073cc0d59fef9390cad15601d7109dd0@65.108.193.11:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
