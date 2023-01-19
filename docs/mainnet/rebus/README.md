# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
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
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
