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

**live-peers** (13)
```bash
peers="f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,4dc627534292d408d9087b7d62e59a10fdf99e7f@65.109.60.19:46656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
