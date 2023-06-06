# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" alt=""><figcaption></figcaption></figure>

The Migaloo chain is a permissionless Cosmos SDK chain on which  projects are encouraged to build their applications. Migaloo chain  is the home of the White Whale dApp, Interchain Command Center.

**Chain ID**: migaloo-1 | **Latest Version Tag**: v2.0.3 | **Wasm**: ON

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
peers="e39876398a43c0f9b93b5a82d8e38fa57c0373b5@65.109.89.19:20756,0326c9ee117587b7ebe3b26b00820642a8cf48ff@65.108.238.102:20756,2e71dbd7d4c079ba7894c5287291c17ba58a6504@141.95.47.78:26656,3b3428d679faa1bd498b3554ca798de3a0d802c6@162.19.89.8:20756,8b82817f0ea0117cb039050853a5d49b9a4ebf23@178.128.238.183:26120,70d1818f50d983bfebf4c8546b221687b76cd4b0@51.81.107.95:20756,4236750928a4dcb742e50e30e500ebc9ee39f240@35.223.246.103:26656,7603409373d43dfa078bcdc8dd380e4b7105f7cb@178.128.42.132:26120,7e2bf7bdcc3b40a1dae4c9befb1ef1cb47d03c6d@65.108.10.37:26656,2bd1bfb7a8d73e573b3a27cd01835b67d48f1f04@51.159.214.226:42103"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
