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

**live-peers** (18)
```bash
peers="ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,f6070ab2af725d4f62bb81dbd30dc2047bc66d04@65.108.193.249:2270,193acd7bf7049b425d7b95c24e02250fce8ad45c@65.109.92.79:11656,3ef426538e3b8bfa274aa9a442583bbbda71942f@185.144.99.12:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656,71819ce1899c1f4f0f138f7a538958dd0d3d3ff8@5.9.78.252:27656,80ef97d24a7f7072bff45b1822f97982f483b047@74.208.94.42:26656,e4fa11cfb413d69d95dc90a0e12125b091b1d574@51.158.115.159:26656,7b2fb9cdedb18336e55f4e8613e841982e455ba6@31.7.196.40:26656,3cf4a639196a73028136cd590c4682a80d41c460@3.125.129.136:26656,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,8fa3db61eeecd770ec508c3065d4a80a9a59c2af@195.201.108.152:16656,584197886e2ddd65df7e42ca5ded30047b715d00@65.108.44.149:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,481f26198511686ab7f648bc71a925901d9961e3@52.194.8.37:26656,f95a43de563d4b08b278db2c8cffee6e8b8d6f14@38.242.247.80:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
