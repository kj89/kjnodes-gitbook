# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" alt=""><figcaption></figcaption></figure>

The Migaloo chain is a permissionless Cosmos SDK chain on which  projects are encouraged to build their applications. Migaloo chain  is the home of the White Whale dApp, Interchain Command Center.

**Chain ID**: migaloo-1 | **Latest Version Tag**: v2.0.5 | **Wasm**: ON

[Website](https://whitewhale.money) | [Discord](https://discord.gg/AyvcgD4jy3) | [Twitter](https://twitter.com/WhiteWhaleDefi)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/migaloo/migaloovaloper1jxtgnfw3tatfh90ju9j76dfrt3yea0zw2vnr8v)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/migaloo/migaloovaloper1jxtgnfw3tatfh90ju9j76dfrt3yea0zw2vnr8v) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/migaloo](https://explorer.kjnodes.com/migaloo)

## Public endpoints

* api: [https://migaloo.api.kjnodes.com](https://migaloo.api.kjnodes.com)
* rpc: [https://migaloo.rpc.kjnodes.com](https://migaloo.rpc.kjnodes.com)
* grpc: migaloo.grpc.kjnodes.com:14990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@migaloo.rpc.kjnodes.com:14956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@migaloo.rpc.kjnodes.com:14959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/migaloo/addrbook.json > $HOME/.migalood/config/addrbook.json
```

**live-peers** (10)
```bash
peers="aba0c3f98fb5bef1a0d991b8e2b8bba24f9908b6@65.108.111.236:55736,c616069071f0864b5b0e995f8d8961536b41ab62@15.204.141.36:26656,ccaccdf6bafcb57197d86a1420a289cd39fe0ae9@85.10.200.231:8095,e3fee82bd16509145c45b3dc0b8f4db25315078e@212.227.13.120:26656,9cb7ba30c7eb7e9b516b90e09ca0f53250927440@146.59.52.135:8095,8b82817f0ea0117cb039050853a5d49b9a4ebf23@178.128.238.183:26120,78f0f5aa89b7ed92a5728dd3f67f646d8dda5213@198.244.228.162:55736,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14956,5429bc670b77cd9c61481912ea194bea8aa6d0cd@51.81.155.189:20756,a3b16ffbf713e51aa04aabfb696a9646393be934@139.59.8.48:26120"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
