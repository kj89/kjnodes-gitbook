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

**live-peers** (10)
```bash
peers="15582b92e58c81fad0220954a118097e2a3b2951@65.109.106.172:29656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,dc1aac15f2d1071ecc9573e2b71a063eb125067e@51.91.30.160:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
