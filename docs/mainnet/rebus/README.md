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

**live-peers** (30)
```bash
peers="f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
