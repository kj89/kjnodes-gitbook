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
peers="b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,15582b92e58c81fad0220954a118097e2a3b2951@65.109.106.172:29656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,6712c72792a0753a4e8d9fae298f50b92892194c@23.175.49.98:10656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
