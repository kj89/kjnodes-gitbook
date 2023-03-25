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
peers="e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,ff7621be29e39e9fdf07f2501e1a217201ca29ee@213.239.207.175:39656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
