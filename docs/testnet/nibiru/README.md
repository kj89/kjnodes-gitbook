# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (14)
```bash
peers="0945129df734538663010c1349f1b4f29da48687@89.117.48.176:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,d622efcde775f33bd8c14fa5757ee9fa95d4149e@135.181.203.53:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,2269d5937ec2b5213ad4ee824ca1ccc328971dc8@185.219.142.179:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
