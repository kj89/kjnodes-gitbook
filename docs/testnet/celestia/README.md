# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.13.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: celestia-testnet.grpc.kjnodes.com:12090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:12056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:12059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (12)
```bash
peers="de36dc2bc32ecaacafb213d173f6218f93ebb306@144.76.105.14:26656,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656,23c69377c73644e125d29cb01d1f61e897fc0ae4@65.109.104.70:21066,3cf4a639196a73028136cd590c4682a80d41c460@3.125.129.136:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,193acd7bf7049b425d7b95c24e02250fce8ad45c@65.109.92.79:11656,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
