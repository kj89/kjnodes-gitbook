# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)

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
peers="18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,678ded952968137c8ded8aeada337662065f1507@159.203.162.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
