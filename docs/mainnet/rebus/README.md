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

**live-peers** (29)
```bash
peers="07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,3a49b0d49e2dcc0fb28d97b77c4e101f20de5842@155.133.22.8:23256,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
