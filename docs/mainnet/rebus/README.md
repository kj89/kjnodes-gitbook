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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,46b5ab9fdbddf1acea9222b523ed0a34571b6bbc@154.53.60.246:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
