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

**live-peers** (31)
```bash
peers="e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,7bb000363922f1da93c0f25b2544e453b523a82a@65.108.246.178:26656,e774ca76b7765c49e21daff712fbbc93815771ab@5.9.70.180:15662,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,31fa18ff28fd7f80d279a951849e4ef56003b039@128.140.85.113:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,ba49814ebe24e4d1ba41f4fc774997bd5d7d8e47@65.108.126.46:35656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,3b5c0147311c294de8e635c853af5a0de72d43f1@65.21.131.215:26566,7f8bd4eaf6b9b213fd7b89ceefc517bcaa517d24@5.9.147.22:22656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
