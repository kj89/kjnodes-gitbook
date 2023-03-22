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
peers="87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
