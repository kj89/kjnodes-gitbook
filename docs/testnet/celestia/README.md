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

**live-peers** (13)
```bash
peers="5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,1f11577400a5caadedc01261e0f4902983445fb1@46.4.53.94:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656,ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,c054b3a758977691e284b04240efecfb5a56986b@195.201.197.4:20656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,ad9f58823af591c23254347ade010166d5d6334b@135.181.216.54:2150,6df4a6d0db5a771b84055646fe3814c655dd3428@95.216.163.64:26656,f7916ed6f294f94740b98b5a7f21d368589fee56@202.61.194.254:60956,0096a95343de3097594ebebc66542ed4a4167f2a@65.109.159.227:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
