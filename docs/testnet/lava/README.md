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

**live-peers** (30)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,fd72e2c2418ea30da3771d6a66893cb4c7ac4263@5.189.137.33:26656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,4c86262ed00a1d42c6654967589ca57143f950d4@68.183.82.151:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,2ce2e6a1ba83c46183f8ee543ce8bd80be9544fb@34.206.52.68:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,97a7c2941a5875ce518f4775b841ff3b888c82d4@65.108.129.104:21656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,897d44b1cb6633539cf51261f6629a9d5664eb9b@159.69.72.247:11656,f31c4dc121f37db1e0e24b49584bbbe4bbbba6c4@162.55.39.16:36656,7fb838681ff9855a634c7823de605fb4a5d22eba@65.108.144.202:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0efa60456219f5b7847ee21439aa8662c0a8e1b6@65.21.195.40:26056,79a3b530b271b1f9b5e10617fcca9041c9f8f548@65.108.45.200:26858,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,563bf40de5ff5d2aa2dc8c4bab350c67bfcb4284@109.123.253.103:26656,4238277ef21b9a8cda2c20a9b4570d180353dffe@24.199.118.95:26656,632bfd3276ab33ed74cbb048a1de28183b927e9c@80.85.141.179:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
