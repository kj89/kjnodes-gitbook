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
peers="12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,46b5ab9fdbddf1acea9222b523ed0a34571b6bbc@154.53.60.246:26656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
