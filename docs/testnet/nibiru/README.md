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

**live-peers** (30)
```bash
peers="5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,97c4976b580a5ef4c3b82e239c50c81b8ab8189d@49.12.123.87:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,436cb422506a1b3fc9c4e1e5920625e49babe161@185.219.142.214:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,0cc5236b8a37e89af65c8504982ae0eb5b01e004@178.20.47.61:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,0bec869738691df5d0c1f40348c95cd256382f26@89.116.31.114:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,b87fb99a9a4b6d2651b4015ff7f055a82ea6acdd@116.202.17.68:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,1d31af8dcbc5a3333eb6583f97ed6b2387d70e72@34.30.60.89:26656,7c85671fd863077f7f74d85341beeb53408fae3c@109.123.248.101:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,b02f28e0675743b077186b363386f10845c9e122@194.233.74.249:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
