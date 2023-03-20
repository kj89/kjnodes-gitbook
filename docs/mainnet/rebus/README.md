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
peers="92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,bd5a6419c073d6cb97bddcfcfd2059bdec41e6a8@185.144.99.33:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
