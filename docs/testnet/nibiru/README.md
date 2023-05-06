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

**live-peers** (18)
```bash
peers="efaee8ff19257f93a8bb632aeeec29068e9f39c1@95.214.53.37:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,436cb422506a1b3fc9c4e1e5920625e49babe161@185.219.142.214:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
