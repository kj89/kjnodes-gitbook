# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.9.8 | **Wasm**: OFF

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

**live-peers** (30)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,0f9f0fb4b9371a65bdf1c883a2a7dc52d0023019@34.233.69.21:26656,e5aff8690b3fc34f81c1792d56ba5d182cce68e9@65.109.116.204:21156,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,d3a466c4892943059b6b361e63eb0665ead5c574@147.135.222.170:55676,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,aaef3ec60834eb3248d798d5bee570b1a622e701@134.209.104.7:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,ebac611952239a3f11141f6ff69e8b241d622567@207.180.239.235:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,10ff3886c6304556101d5ffa060e32929a82769f@65.109.53.60:31656,71f6af45c867266f81d81193013fcb4137351355@194.163.155.84:56656,5d24eb95fa5974af7bb03e370382537251ab6328@95.217.158.66:26656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,75ed1e87b48d6e1ab341e3568708c9fb81743ffa@65.109.88.251:11036,d32d39aacbc8049cda4035da34d5fbaa79eb7765@161.97.175.226:20656,9872ab6a76199fcbeca1f7f791755e726aa97686@116.202.165.116:11656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,1db3eae2768388f2b613e0dae62763db1aba7994@43.204.255.101:15656,525696e557db51c4d5f5bca1d7152753c7426c2e@34.192.150.110:26656,4f9120f706512162fbe4f39aac78b9924efbec58@65.109.92.235:11036,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,ac7cefeff026e1c616035a49f3b00c78da63c2e9@18.215.128.248:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
