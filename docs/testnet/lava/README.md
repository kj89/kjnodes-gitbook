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
peers="dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,bebd03c6319c0930400dc564e9f5365068497322@95.217.41.15:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,95a490b4cde4c5311f7d58c3e47ee41fa039ddf4@144.76.27.79:60756,c5c98017339ce6d4d5d2a4fd0fb1aaeb966ef0f7@65.108.124.57:36656,4e0a2772bb3672e54c2ea655c30abdac62191f14@45.84.138.66:18656,84712b4b59bfdfb4d5818c6baa37ed5b5a8e87f8@85.239.243.211:26656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,20c13bd0d972acba5588493fb528b558a0317013@38.242.133.203:26656,b4d53b1e7a2fee2192a30e411ba83136c07ab595@161.97.147.107:26656,53fefce3786fa850271dbe56cd805b64c106c32f@5.196.7.58:26666,38c4ae2946fb61454e7e095940ddca373a5dcfaa@135.181.221.186:30656,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,39309f1ce3d7b6acf9714c749b67c7db6d3f615d@38.242.152.174:26656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,7022dbc496c5cc645df6a44f792b40aa150844a3@62.141.44.209:38656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,6d7ead316f354a549fe22f5ebe72d68ec0af685a@194.233.68.136:44656,4bfb0d4d945985d2cc92ea4ba3578459b80f1dab@190.2.155.67:33656,079712c11852caca22f16b8f48ea3158539125bf@65.109.164.12:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@65.109.15.19:26656,580d6c9be21f26a713881fc9dcb4ebafcc945eb6@159.65.16.202:26656,dcb7e2621a326d58184c3ad5a6e6b82b5ca0eda2@65.108.255.124:46656,79a3b530b271b1f9b5e10617fcca9041c9f8f548@65.108.45.200:26858,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
