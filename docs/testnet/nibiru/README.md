# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (26)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,1587dd54b6e1f373ccf61401980816fbd7f7e43a@35.232.147.245:26656,30abc253688f7e70a6dcae9f0850e41a0245db3a@129.226.148.203:26656,104a00413d0fc7ec208c810c50d49932da355bd5@129.226.159.141:26656,6fefa7ece2ff81d1c228c31eda72692d9299d8bc@38.242.248.145:26656,f28e811d5c509cad0d14a6757a1eea1441be3e13@65.108.9.164:22456,aac16ac16e941f944c3c911db963e23159c6d637@38.242.246.213:26656,4715d949ee0ed2be527a21a6a8d0985430103017@109.205.182.232:26656,d5cc6d9f81b5cf808981233a6f8029e0d775504a@165.232.148.181:32656,883e3477ad5360a63c9f9d66a7b731e99dfe2dfd@138.68.101.57:38656,971fa24215b57d81be85a68a0a85b0b64d122dfc@5.166.240.95:26656,4ff2d57f41c0162dcfed7ac55077ed36e8721c18@31.220.86.18:26656,785ffb99f8724319d44254cbb47b3428aaaa25a5@38.242.236.134:26656,07323474e3685dd9ab23c5d515f62ff929c8dab2@45.147.248.163:26656,25dc5ada7df01293cc7af2b44b24356e054228a2@217.79.255.69:26656,a3de1f505133b416a47f546b4d4ccbdc442a891b@84.46.251.68:26656,fc015be87e5c15953a6508403c99a6c8d9493622@194.34.232.35:39656,01277e798525ff4df01ce6301a769b6898f408ea@95.217.156.93:26656,efaee8ff19257f93a8bb632aeeec29068e9f39c1@95.214.53.37:26656,30a63eaa77f7f95d741d16c2564441c4422fdb25@185.219.142.120:26656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,63c350ff4e6cc8cd4eb93332b2014473c9db9d8f@83.229.83.167:26656,2d635a85087168f8ff3d17d1fa9c609195642775@206.189.134.31:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
