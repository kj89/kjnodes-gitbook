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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,c08cc20656b20b9590bfb28980100900631e3709@162.19.58.103:26656,3e3d0887865ca6feaf7e99a50dbfb41e591a9781@141.94.138.48:26688,ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,e85b086d236a2c9a4d285e6d44126bb6fc6a1555@131.153.158.209:26656,193acd7bf7049b425d7b95c24e02250fce8ad45c@65.109.92.79:11656,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,02b93545950853d692d7ea63eac879e6dd4bf390@82.223.122.139:26656,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,fedea9723696360d429a23792225594779cc7cd7@65.108.231.124:11656,606f6520eb2be48acdd5039173dac0ad65bce4f5@35.210.34.138:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
