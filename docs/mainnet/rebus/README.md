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
peers="5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@94.23.207.45:30547,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,46b5ab9fdbddf1acea9222b523ed0a34571b6bbc@154.53.60.246:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
