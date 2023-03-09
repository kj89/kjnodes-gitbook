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

**live-peers** (40)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,67f122a00eb926ff49cf54b1032e57d7027a02b8@38.242.158.250:26656,e3c92ba5f1ebd8bec0ab9431eb183ed9864eca87@65.108.231.238:46656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,bf7aef75c35725f89f31c12197100a1dd91b3174@146.190.47.103:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,8cd81b9119e4aa45fe549dd12543de862457c989@38.242.155.47:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,dc1c37e340a191ac0eea7c561b4a3c8fba2ce80a@65.21.237.241:26656,5585de73ef537dcbbe8ae04392ccea3a112cc6e6@65.109.85.170:49656,e06519a36d7c780af9ad2be69616a98445112c7a@80.79.5.171:29656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,dced9544a6a8529980dee3ef5b40a251ef06b763@157.97.108.38:20656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,8ffa4dbef4c0b2a1dc1172760914e2df1468fb22@178.63.8.245:60756,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,bbdb9ebdcc2ea89eca1091da8e54da0045373817@65.108.42.97:26656,3bc69361b1f03a52d63c31cf5b87a058e7a9385a@77.40.50.164:26656,550d7467d6a442da11d9772b804252a8dfdca27e@91.107.243.149:26656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,3f6d9698d9a5d9fe17afa5968ea652fae478b32f@185.250.37.239:32656,4c50601b49951a90204e72371e9efb453092f824@194.61.28.72:26656,34271a6f82d755777a3db02be39e575bf4ebd415@65.109.30.197:28656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,b36a39d183383fa068f0db145b179bf8455a06f4@38.242.159.214:26656,e2d3ae20c34f9fadc56853218110da2d79c1a8a3@38.242.222.255:26656,8c120c2b9b1379ce513b0017422d537cb284e067@86.111.48.172:26656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,d8900913c64c2d7894d13ba35fe6c3e7c346015a@95.31.224.15:36656,b62eb3baed171ab5654292e5e35d56a1287693c9@45.32.66.24:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:33256,f137232fd25d5c3adc6d3f6cffa879beafe17768@89.250.150.241:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,0925c475208d8e338907383ab87a094ad03c478e@65.109.55.186:40656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
