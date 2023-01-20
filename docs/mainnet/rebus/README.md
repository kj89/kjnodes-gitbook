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

**live-peers** (29)
```bash
peers="12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
