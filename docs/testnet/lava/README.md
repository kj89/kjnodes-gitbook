# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)




## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: [https://lava-testnet.grpc.kjnodes.com](https://lava-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (38)
```bash
peers="80922095c0766aabdaf9e93e9c38c45321347ac0@85.239.237.85:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,f00678dae0448ca33974a359bb1986e52b7ac19f@43.153.32.148:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,0f9f0fb4b9371a65bdf1c883a2a7dc52d0023019@34.233.69.21:26656,8cd81b9119e4aa45fe549dd12543de862457c989@38.242.155.47:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,7fb838681ff9855a634c7823de605fb4a5d22eba@65.108.144.202:26656,2d8a3416369fdb1fb48b7b418521ec31679fe0c5@184.174.37.165:12656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,74a979f0df53ef6f2ba9ab77c0c9fc5ba9c2bdc5@213.239.215.59:29456,32bf51f70c0a05c33a20c5af73f7cd55c3eadecf@213.202.216.117:26656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,f8b7dbce90a7cd73f008ce65218caad40c0f56c6@167.86.115.153:32656,07c557b393b235a7b004a4a32831e54092dc24a0@91.107.147.250:26656,0735c5a841fe98ee0a74de7cef537c03b4c66a1b@45.89.54.153:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,4e652dd3eac01eaf229e67e250db9f4a7b0a6832@154.53.51.114:26656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,d7c350f9b16111f04a5fe391ec8ccbed5faee56e@86.48.1.218:26656,a0476bc75ad2ade9ce8a6b2cd41ef646d3a2e3ee@85.10.193.246:28656,c69864d1c6dd7132f2f65eafec6e6828938c5c8d@37.221.198.252:26666,266ff814503d94fbe1a9f6923d1638ab1ad56461@185.209.230.99:26656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,d1772004f29d81f4c7cbb62ea71d2f230643abfb@65.108.150.175:24003,e38146de8800082110878c0521fd3ee5f93b70d6@194.163.177.203:26656,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,bbdb9ebdcc2ea89eca1091da8e54da0045373817@65.108.42.97:26656,94e57de2ffaa856ca23c23b81dc17d21a71833c5@194.233.75.144:26656,ace0e997a728bd76877618628b484d1adbd9ddaf@193.57.138.229:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
