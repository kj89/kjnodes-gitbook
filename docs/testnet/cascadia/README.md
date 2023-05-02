# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (28)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,d9201d865b1ce2709b0a5270a230d534e93ada2d@65.109.65.163:22056,59385d42afcf24bdc7cfadb6272b48cc08683e86@217.199.117.157:55656,de11c79dab6ea248fb72f9d93c2ff0eace14a5ac@94.250.201.130:26656,3afe6df94dc385efa85aef823e038c76147e4c99@95.217.35.111:26656,624b1a13e77bd9f3cde44f4ed6a32eff1a95611b@195.201.59.194:26156,173262935b9d8ac15013c3e34936c89de9973f2d@41.189.187.235:26656,84371a3cbc4d68ba96f05fbeb612bf4739a483e0@5.231.220.71:26656,2fb0a8dd1c16b363d779229ab009479e0e60b7c1@95.129.57.179:36656,8658672ab9c417545483aeb5748c2818b4f8b89d@65.109.94.10:26656,190d96828cdeba320b60f4704d2f35a404c97fda@65.109.92.230:15656,a9986cb9e9950320e3b378a5dadebd6465d09de0@65.21.205.241:18656,3fd24af1036b180e2afdddbd83a0bbca211f9327@141.164.40.180:26656,31da1f1c50721bece630aa789c2ccd2023f2e596@38.242.234.199:26656,32bcc51674dd83a316323a67918c1cee25163291@65.109.72.12:26656,fcac681e16636bc1185194e31d0ff9b27d7f1275@85.239.233.241:55656,3dba68e8593170a998fc336951e3a2535c2fd54c@135.181.163.178:18656,cf08358a4db35d91b0b857e674380828619fcd4c@194.233.81.122:26656,c9256e4f42a23bbdc9ea79805f497a1923a4beac@65.108.230.113:17096,c6e3921222655345d8296353994e917f13a1b4a1@65.109.92.79:40656,37f1c41be15a41e33a0a820d55db3ca439486602@148.251.90.138:18656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,75b6a162a55e6b8a4c775c061bf814baee208d3f@194.163.170.138:26656,df3cd1c84b2caa56f044ac19cf0267a44f2e87da@51.79.27.11:26656,040d0b6ffefba3283b5763e26c352c7b1b232c1f@65.109.90.171:34656,c308f0e31f21b4007b07780f29ce75ae5ed4aa9b@144.91.110.125:26656,e34cc8a12a5274272ff861b4fe3042e98697e500@46.17.250.108:60956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
