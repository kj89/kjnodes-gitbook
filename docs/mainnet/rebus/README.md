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
peers="10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
