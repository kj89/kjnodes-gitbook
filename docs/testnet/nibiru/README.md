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

**live-peers** (16)
```bash
peers="bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,930b1eb3f0e57b97574ed44cb53b69fb65722786@144.76.30.36:15662,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,e08089921baf39382920a4028db9e5eebd82f3d7@142.132.199.236:21656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
