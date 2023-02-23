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

**live-peers** (30)
```bash
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
