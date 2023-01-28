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

**live-peers** (15)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,0561fed6e88f2167979e379436529861527d859d@65.109.92.148:61256,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,632bfd3276ab33ed74cbb048a1de28183b927e9c@80.85.141.179:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,7e68edc23e6c716b3248099dd1f03810a57975ef@65.109.92.150:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
