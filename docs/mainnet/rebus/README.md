# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: rebus.grpc.kjnodes.com:21090

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
peers="92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
