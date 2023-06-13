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

**live-peers** (15)
```bash
peers="ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,c08cc20656b20b9590bfb28980100900631e3709@162.19.58.103:26656,0096a95343de3097594ebebc66542ed4a4167f2a@65.109.159.227:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,0196b56324c6fd3dd31110d3cb06dc169a1e1310@194.62.97.31:26656,80ef97d24a7f7072bff45b1822f97982f483b047@74.208.94.42:26656,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,5fa6853eb52bc3a5ff1fe56b988515d16644819a@65.21.232.33:2000,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,2d2c1bcbe6bb2ba77586933119160d29f961fffc@65.108.225.70:24956,10c84789386c2ee3aacd8e09f04b78fac14fb3d7@209.126.86.119:26656,3e3d0887865ca6feaf7e99a50dbfb41e591a9781@141.94.138.48:26688,f95a43de563d4b08b278db2c8cffee6e8b8d6f14@38.242.247.80:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
