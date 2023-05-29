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
peers="62f6abc162db99389f13a1cdf1abaeb6efb647a7@35.210.78.75:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,193acd7bf7049b425d7b95c24e02250fce8ad45c@65.109.92.79:11656,c054b3a758977691e284b04240efecfb5a56986b@195.201.197.4:20656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@46.4.53.94:30582,7135928a1a9e6cc13d139a67b4ef94c53f470e15@154.12.252.237:26656,64a3c4a25abefdd2087da0d7cd1abafe8a354953@209.97.138.19:26656,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
