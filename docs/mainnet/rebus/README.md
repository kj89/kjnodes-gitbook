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
peers="3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30547,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,aa2feb704c0089b1a0f23011a9e7cd2c27a06134@65.21.200.6:29656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
