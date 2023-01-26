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

**live-peers** (38)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,bf7aef75c35725f89f31c12197100a1dd91b3174@146.190.47.103:26656,131227f65bbc8f5b86030124fa1610a3283ebcbd@135.181.176.109:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,ddafabd9760011a797952ab62c50b758f83ea7ca@65.109.112.20:11144,b36a39d183383fa068f0db145b179bf8455a06f4@38.242.159.214:26656,20c13bd0d972acba5588493fb528b558a0317013@38.242.133.203:26656,39309f1ce3d7b6acf9714c749b67c7db6d3f615d@38.242.152.174:26656,beaedffb147f5908523589c212c971c292fef46c@65.108.226.101:28656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,be66ac74b3da437cbf4ad0103ee2717fa43f5f2e@5.75.236.114:26656,6641a193a7004447c1b49b8ffb37a90682ce0fb9@65.108.78.116:13656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,2cb465a7c919321978f89701b4ae07ac505f7ad8@194.163.184.228:26656,810bdfb3e88f4872995f9a05b6298c1bf3d20fe0@65.108.105.48:19956,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,e854d8b04c8a9b783a0a26a55077e1625c182888@5.75.194.221:26656,3fe03955c4a497e728fa0edc4bc2a9cb07604347@178.54.78.180:44656,2ba0a1c952954f37e3b14abc1e35c77f74c64c8a@161.97.136.244:36656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,bc315b3fc407b69e24900b6a170348d368141948@86.48.5.240:26656,47a18d7c304896a8afe245fa15920523c5b910a4@86.48.1.143:26656,33298ebaaa99faad4f5c9880f555340f26ff66ff@161.97.160.19:26656,474e2436e097c28472a1fe269e1825762fa340d6@38.242.128.19:26656,fb498cc17f301930cfd4d3b6e6261148c84e05e7@45.140.147.117:27656,41df4ebb2b3955288f4dad374d6646507636cc26@167.235.85.70:26656,12d6fc425a5d3c8164b41b6f5ea28168ae56f4ba@178.18.246.21:26656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,910c0e9e8299d642208ef4c4199ae9ea44d6ffe1@164.68.99.218:26656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,d60e577b6dbdac7a7cd620f71a6bff71f9f82c2e@146.19.24.242:26656,efae73b2b084b9a818e34e777917ebf923ebe617@94.130.54.253:26604"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
