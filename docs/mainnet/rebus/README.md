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
peers="275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
