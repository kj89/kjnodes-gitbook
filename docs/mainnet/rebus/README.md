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
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
