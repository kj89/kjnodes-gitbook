# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
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

**live-peers** (20)
```bash
peers="92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
