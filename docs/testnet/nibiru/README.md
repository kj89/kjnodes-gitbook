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

**live-peers** (15)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,d622efcde775f33bd8c14fa5757ee9fa95d4149e@135.181.203.53:26656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,072113660767e89b71033ce214f8248d2fb88862@194.163.167.126:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,930b1eb3f0e57b97574ed44cb53b69fb65722786@144.76.30.36:15662,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
