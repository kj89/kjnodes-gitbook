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
peers="15582b92e58c81fad0220954a118097e2a3b2951@65.109.106.172:29656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
