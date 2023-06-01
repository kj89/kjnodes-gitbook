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

**live-peers** (12)
```bash
peers="b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,aa882f345fd3febd66f0693d4525a537bdaa35ec@194.233.67.92:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,e08089921baf39382920a4028db9e5eebd82f3d7@142.132.199.236:21656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
