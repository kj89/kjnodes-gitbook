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
peers="36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
