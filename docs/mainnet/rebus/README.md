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
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,57f475bb44fc6f121790d523ce06fb4e0ad9ab69@141.95.65.73:17256,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,3a49b0d49e2dcc0fb28d97b77c4e101f20de5842@155.133.22.8:23256,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,0863966356f6532377aeba663415258d44ddbd13@88.99.164.158:40106,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
