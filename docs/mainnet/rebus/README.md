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
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@134.65.192.98:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
