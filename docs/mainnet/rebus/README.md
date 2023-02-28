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

**live-peers** (18)
```bash
peers="e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,ad116a3f497ebb37ac14226c22a1483237a224ac@65.108.229.102:23656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
