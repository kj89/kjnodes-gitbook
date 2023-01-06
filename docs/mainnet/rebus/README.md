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

**live-peers** (29)
```
peers="5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@134.65.192.98:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
