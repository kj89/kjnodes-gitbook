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
peers="d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
