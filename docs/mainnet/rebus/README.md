# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

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

**live-peers** (30)
```bash
peers="10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
