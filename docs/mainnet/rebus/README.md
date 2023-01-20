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
peers="b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
