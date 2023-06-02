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
peers="c08cc20656b20b9590bfb28980100900631e3709@162.19.58.103:26656,0096a95343de3097594ebebc66542ed4a4167f2a@65.109.159.227:26656,7135928a1a9e6cc13d139a67b4ef94c53f470e15@154.12.252.237:26656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,02b93545950853d692d7ea63eac879e6dd4bf390@82.223.122.139:26656,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656,7b2fb9cdedb18336e55f4e8613e841982e455ba6@31.7.196.40:26656,193acd7bf7049b425d7b95c24e02250fce8ad45c@65.109.92.79:11656,bd958914e4baac42f1c28fbae24e920bb0072535@65.109.71.210:26656,f7916ed6f294f94740b98b5a7f21d368589fee56@202.61.194.254:60956,02241bb63c01fb52033029f7155c3db5d7846c1f@168.119.64.26:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
