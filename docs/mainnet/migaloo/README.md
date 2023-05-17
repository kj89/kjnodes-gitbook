# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/migaloo.png" alt=""><figcaption></figcaption></figure>

The Migaloo chain is a permissionless Cosmos SDK chain on which  projects are encouraged to build their applications. Migaloo chain  is the home of the White Whale dApp, Interchain Command Center.

**Chain ID**: migaloo-1 | **Latest Version Tag**: v2.0.2 | **Wasm**: ON

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

**live-peers** (9)
```bash
peers="a0a450ead908bd65813322c1373802ef32c5736d@65.108.235.33:4000,3b3428d679faa1bd498b3554ca798de3a0d802c6@162.19.89.8:20756,9780ea85f4d0f4cb5ebca14992ce11ebe1982d35@188.172.229.26:26656,80be85c4980deccaa2fbd710029f0eb660dadf9a@51.81.16.186:26656,e39876398a43c0f9b93b5a82d8e38fa57c0373b5@65.109.89.19:20756,6870906f86e474d88d077c7c55af36debe49da04@178.162.165.194:7095,ccaccdf6bafcb57197d86a1420a289cd39fe0ae9@85.10.200.231:8095,51ca404bbc73d07fc0d6529388c90f807c5acf0b@65.109.104.72:20756,9cb7ba30c7eb7e9b516b90e09ca0f53250927440@146.59.52.135:8095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
