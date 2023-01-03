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
peers="30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
