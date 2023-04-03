# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.8.1 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

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

**live-peers** (27)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,d7c350f9b16111f04a5fe391ec8ccbed5faee56e@86.48.1.218:26656,5ab0449599aabcf90f664003c2ef1510ecd33b1b@65.21.203.204:11656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,07c557b393b235a7b004a4a32831e54092dc24a0@91.107.147.250:26656,4bb3bb98ca32b5a0f82d445e60065601bb93a38c@86.111.48.163:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,a0476bc75ad2ade9ce8a6b2cd41ef646d3a2e3ee@85.10.193.246:28656,5b25ec3860445e50a41a80850970b3241350df72@194.233.90.134:26656,91c02af6333972f222570a73f51feccda8a3ccf1@65.109.93.58:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,cfb2b0ee7bd28ef37f8c1019727caa783a122fa3@78.107.234.44:26656,3f0eb55b386427af17829b8ec98fd367a2fc469f@135.181.183.93:11656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,7ec0007e3c24012db9d5596745db5cb7c8321b50@95.216.7.169:60956,b6e23ec5fbdf386fd65e1f195a205b00851f64c1@90.188.248.131:12656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,b753a011d9a51bc3aa8d9301afb6d427f758a330@168.119.124.188:26656,a2e229bcc7fcd1b20bafe33f0c7ec8c1ed0167fa@46.4.53.209:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
