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
peers="a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
