# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
