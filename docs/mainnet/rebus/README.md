# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

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
peers="10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
