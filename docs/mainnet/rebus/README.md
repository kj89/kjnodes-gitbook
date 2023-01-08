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

**live-peers** (27)
```bash
peers="30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
