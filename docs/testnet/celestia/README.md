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

**live-peers** (14)
```bash
peers="ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,7b2fb9cdedb18336e55f4e8613e841982e455ba6@31.7.196.40:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,c054b3a758977691e284b04240efecfb5a56986b@195.201.197.4:20656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,de36dc2bc32ecaacafb213d173f6218f93ebb306@144.76.105.14:26656,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656,80ef97d24a7f7072bff45b1822f97982f483b047@74.208.94.42:26656,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,0096a95343de3097594ebebc66542ed4a4167f2a@65.109.159.227:26656,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,af66f28f19f747bd2b5a18d91d143dc8e035f86a@47.147.226.228:52656,393dc0c641caf09dcbc192df440562af60d6958e@149.102.157.17:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
