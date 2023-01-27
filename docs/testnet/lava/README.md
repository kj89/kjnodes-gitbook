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

**live-peers** (33)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,9fde827327a35dadcde19cbca9f9255c2f5c4cb6@65.109.106.6:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,855ce67c043ed3f466b1cda61525193f6e239c93@144.217.201.173:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,897d44b1cb6633539cf51261f6629a9d5664eb9b@159.69.72.247:11656,0e9062ed560ce78eba346f1d73ae3ca9eeea5985@142.132.248.253:24656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,7ec0007e3c24012db9d5596745db5cb7c8321b50@95.216.7.169:60956,f9f49cc8ffbdee85fb8a9551f644f5554a610ebe@91.107.137.90:26656,7fb838681ff9855a634c7823de605fb4a5d22eba@65.108.144.202:26656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,a5c1d2e86c2dc0eecb009dc71c92d6b5e193db6b@35.210.166.150:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,e77d76e89ae593411ca6a6f1f13bc98d3bdb2024@161.97.142.90:26656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,d2ded0eb8f9a1bcb61af92c8d6a1cf1cbc747847@194.163.180.203:26656,910c0e9e8299d642208ef4c4199ae9ea44d6ffe1@164.68.99.218:26656,7c6b756adbd4a7a7a9fbd2f538627077641cf114@65.109.69.240:27657,29363a9673ba0f48f640d1260731a73e2058aab8@62.3.12.128:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
