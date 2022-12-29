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

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (30)
```
peers="1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@134.65.192.98:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,46b5ab9fdbddf1acea9222b523ed0a34571b6bbc@154.53.60.246:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b574e11e103058a121cc03d1c4d9867ba3daed34@135.181.139.113:31656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
