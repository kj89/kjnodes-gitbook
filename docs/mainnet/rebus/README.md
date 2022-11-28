# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

Website: [https://www.rebuschain.com](https://www.rebuschain.com)

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
peers="a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,7196b111260698b8b6ba8ea64c3af0444fb365c8@195.201.63.87:41656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,15b1c913dc3d9dab7c912b27bb2a957abbfe8834@142.132.199.27:40106,d241f395a167fd7a9f155641760bffa8af6a50d2@167.235.98.202:27656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
