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
peers="b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
