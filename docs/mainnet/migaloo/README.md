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

**live-peers** (10)
```bash
peers="51ca404bbc73d07fc0d6529388c90f807c5acf0b@65.109.104.72:20756,fe04ff9a13d8f0b23463e832f75eb5c845bd375e@213.239.214.73:7095,dfe5f91f824880e19d47475546d9874e0f2cea8c@5.79.74.229:8095,56a59158450e6f819502812cf28febd65c1ac6be@206.189.26.213:26120,4236750928a4dcb742e50e30e500ebc9ee39f240@35.223.246.103:26656,0326c9ee117587b7ebe3b26b00820642a8cf48ff@65.108.238.102:20756,a0a450ead908bd65813322c1373802ef32c5736d@65.108.235.33:4000,e3fee82bd16509145c45b3dc0b8f4db25315078e@212.227.13.120:26656,2e71dbd7d4c079ba7894c5287291c17ba58a6504@141.95.47.78:26656,32eed8c4079201b143d92860c9146b1d9e126aa2@168.119.89.8:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
