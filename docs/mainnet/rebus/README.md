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
peers="b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
