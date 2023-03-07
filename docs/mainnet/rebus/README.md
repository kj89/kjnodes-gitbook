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

**live-peers** (19)
```bash
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
