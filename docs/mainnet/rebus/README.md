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

**live-peers** (19)
```bash
peers="ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
