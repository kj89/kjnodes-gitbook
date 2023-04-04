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

**live-peers** (30)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,f642b376722d6ce104ffd4c204e78ffe811e16c3@5.75.230.221:26656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,57d64cbf5a16820aa9a0582335705f37dde4c18b@190.15.217.229:26656,67dae0d05a857065afd0286d134cbed1c8e9de40@38.242.231.22:29656,51aeaa2c757989f720c904023c2dbedfc720f75e@23.88.5.169:27656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,ffed5a0b0576302bfbeca2b15ac23698457f92a3@89.163.142.196:38656,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,cfb2b0ee7bd28ef37f8c1019727caa783a122fa3@78.107.234.44:26656,40046fe63bdaa9efde27707b0d3de0bf84fedf80@86.111.48.158:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,509eaf8341cca511c8a3127affaae2251593d514@161.97.148.146:56656,5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
