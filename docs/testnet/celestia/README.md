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
peers="5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,f7916ed6f294f94740b98b5a7f21d368589fee56@202.61.194.254:60956,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,62f6abc162db99389f13a1cdf1abaeb6efb647a7@35.210.78.75:26656,bd958914e4baac42f1c28fbae24e920bb0072535@65.109.71.210:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,7b2fb9cdedb18336e55f4e8613e841982e455ba6@31.7.196.40:26656,da9f722bf8dcbbeacf62c323ef06fd723535a141@5.78.111.122:12056,c054b3a758977691e284b04240efecfb5a56986b@195.201.197.4:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
