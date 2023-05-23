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

**live-peers** (28)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,aa882f345fd3febd66f0693d4525a537bdaa35ec@194.233.67.92:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656,ce2dcfe5794bed1d4b32b8a43b32afc5d5e435f2@135.181.114.98:46656,a5b803f5a4bb37965ad13d8bd0e076ef23c5a97c@173.212.252.154:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,d622efcde775f33bd8c14fa5757ee9fa95d4149e@135.181.203.53:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
