# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
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

**live-peers** (19)
```bash
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
