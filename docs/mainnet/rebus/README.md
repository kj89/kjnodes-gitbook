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
peers="eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,678ded952968137c8ded8aeada337662065f1507@159.203.162.120:26656,0863966356f6532377aeba663415258d44ddbd13@88.99.164.158:40106,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
