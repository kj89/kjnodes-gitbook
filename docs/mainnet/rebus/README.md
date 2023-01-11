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

**live-peers** (28)
```bash
peers="4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
