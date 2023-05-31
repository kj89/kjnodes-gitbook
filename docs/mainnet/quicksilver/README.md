# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.13 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,96b7605dbf13dbf0df2c3ac4f076397a9f351c6b@88.98.195.228:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11156,79b214369c8f52c2d33cf79fc1897677b24cf8cb@94.130.240.229:2000,05241d21ff9e7c699bbdb4faa73da1860b6d8cd7@128.199.85.168:26656,a87f48e433160970318d181bb69c378f4564cd2d@107.155.67.202:26736,1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.196:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
