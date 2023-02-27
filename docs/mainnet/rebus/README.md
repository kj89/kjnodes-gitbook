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
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
