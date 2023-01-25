# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.4 | **Wasm**: OFF

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

**live-peers** (32)
```bash
peers="8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,71fb615c968e6ea9458d065d71d47dd1bb10d11e@185.205.246.203:36656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,bbf1fd8b2b993dd354453f90749bd08d108b5de3@194.61.28.30:16656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,f441a05060e55323b3d6757e353eba149fd728d8@51.89.149.182:26656,d2a59307e055565a7e3fc1e420f0615365ef3e11@143.198.149.130:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,e06519a36d7c780af9ad2be69616a98445112c7a@80.79.5.171:29656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26656,8636a0d9276ee1b99c772e51904ea010862bc772@135.181.133.37:27656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,57fabec15de09f93aea5a2a29e937c9035b95487@185.219.142.32:15656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,c4152a1cbe6daefafaf7fcd12a0e2785a3a15c1a@154.53.42.72:26656,dc1c37e340a191ac0eea7c561b4a3c8fba2ce80a@65.21.237.241:26656,474e2436e097c28472a1fe269e1825762fa340d6@38.242.128.19:26656,d927303d07abf24b72f3eb8ae495ac02372e3908@91.195.101.78:26656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,33298ebaaa99faad4f5c9880f555340f26ff66ff@161.97.160.19:26656,bcc19c4f7c3007aea90e24f2fe3a80cef985fee3@89.106.206.190:26656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,dcb7e2621a326d58184c3ad5a6e6b82b5ca0eda2@65.108.255.124:46656,d8900913c64c2d7894d13ba35fe6c3e7c346015a@95.31.224.15:36656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
