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

**live-peers** (30)
```bash
peers="1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
