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
peers="4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
