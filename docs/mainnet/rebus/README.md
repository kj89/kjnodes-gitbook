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
peers="1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,c177f05fc7c0379e26eff108048c0bfd96949b2c@141.95.65.73:17256,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,46b5ab9fdbddf1acea9222b523ed0a34571b6bbc@154.53.60.246:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
