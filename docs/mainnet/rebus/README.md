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
* grpc: https://rebus.grpc.kjnodes.com:443

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
peers="30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
