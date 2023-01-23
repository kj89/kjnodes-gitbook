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
peers="a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
