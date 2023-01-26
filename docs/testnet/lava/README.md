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

**live-peers** (26)
```bash
peers="e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,a5c1d2e86c2dc0eecb009dc71c92d6b5e193db6b@35.210.166.150:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,968548d113d42652720314e31d9822b905b0539c@5.78.45.11:38656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,4b82a658919cb7cc18e7aa5b9d49a75ef138c64e@44.196.143.228:26656,547ed576c99ca6decd5fd54a73f0e53f581d6628@194.163.187.175:36656,27a9aebdcc1bd6a8eb8cbffdd689e565dca14bc2@5.189.149.159:27656,95a490b4cde4c5311f7d58c3e47ee41fa039ddf4@144.76.27.79:60756,7ec0007e3c24012db9d5596745db5cb7c8321b50@95.216.7.169:60956,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,525696e557db51c4d5f5bca1d7152753c7426c2e@34.192.150.110:26656,5585de73ef537dcbbe8ae04392ccea3a112cc6e6@65.109.85.170:49656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,904ec45d55abe397e486579338225bd9b60e0d87@145.224.100.235:26656,c5c98017339ce6d4d5d2a4fd0fb1aaeb966ef0f7@65.108.124.57:36656,d60e577b6dbdac7a7cd620f71a6bff71f9f82c2e@146.19.24.242:26656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,6c988ad39fef48abd5504fda547d561fb8a60c3a@130.185.119.243:33656,821c9347c927db52138dcd4bb54478fdf17f273e@81.0.218.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
