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
peers="256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
