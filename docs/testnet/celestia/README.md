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
peers="f05e6a065b772dda4c7c0cbed40894a8c43416c7@57.128.86.3:26656,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656,7b2fb9cdedb18336e55f4e8613e841982e455ba6@31.7.196.40:26656,80ef97d24a7f7072bff45b1822f97982f483b047@74.208.94.42:26656,f6070ab2af725d4f62bb81dbd30dc2047bc66d04@65.108.193.249:2270,73e2aa2de6080734152b54020464fb9ba752a7dd@194.36.145.127:26656,c97019ef9ee43e93ad9019514b612e6b8363c3fd@138.201.63.38:26686,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,f7916ed6f294f94740b98b5a7f21d368589fee56@202.61.194.254:60956,92e7087b3dec79fb2b8105e5a61935d28927d511@45.83.104.218:2000,10297d22a2f1f66bfb9f2c8f7d7152660bfffd92@65.109.32.148:26116,ae95e8d93a0822a763823551c163d15d4cdce944@116.202.227.117:20656,0096a95343de3097594ebebc66542ed4a4167f2a@65.109.159.227:26656,fedea9723696360d429a23792225594779cc7cd7@65.108.231.124:11656,481f26198511686ab7f648bc71a925901d9961e3@52.194.8.37:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
