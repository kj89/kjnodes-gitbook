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
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,b8613a7717b0ebaf2100c360cf13c92c4de33100@195.201.63.87:41666,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
