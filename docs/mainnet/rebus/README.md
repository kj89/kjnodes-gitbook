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
peers="07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,703714c82c94fc1c74b6ee0d1fc3417b932be5f3@134.65.192.98:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,678ded952968137c8ded8aeada337662065f1507@159.203.162.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
