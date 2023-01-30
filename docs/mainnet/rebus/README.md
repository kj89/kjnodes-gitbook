# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: [https://rebus.grpc.kjnodes.com](https://rebus.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,0863966356f6532377aeba663415258d44ddbd13@88.99.164.158:40106,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,678ded952968137c8ded8aeada337662065f1507@159.203.162.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
