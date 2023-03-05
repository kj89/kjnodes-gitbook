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
peers="e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,678ded952968137c8ded8aeada337662065f1507@159.203.162.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
